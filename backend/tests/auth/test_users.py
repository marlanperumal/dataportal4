import pytest
from typing import List
from flask.testing import FlaskClient

from ...models import db
from ...models.auth import Organisation, User, Group
from ...methods.auth.users import (
    add_user_to_group,
    edit_user,
    fetch_user,
    fetch_users,
    new_user,
    new_users,
    remove_user,
)
from ...methods.auth.groups import new_group
from ...schema.auth import user_schema, organisation_schema


def test_fetch_user(client: FlaskClient, regular_user: User):
    user: User = fetch_user(regular_user.id)

    assert user.id == regular_user.id
    assert user.first_name == regular_user.first_name
    assert user.last_name == regular_user.last_name
    assert user.email == regular_user.email
    assert user.organisation == regular_user.organisation
    assert user.is_admin == regular_user.is_admin
    assert user_schema.dump(user)["groups"] == [1, 2]


def test_fetch_users(client: FlaskClient, admin_user: User, regular_user: User):
    users: List[User] = fetch_users()

    assert len(users) == 2

    assert users[0].id == admin_user.id
    assert users[0].first_name == admin_user.first_name
    assert users[0].last_name == admin_user.last_name
    assert users[0].email == admin_user.email
    assert users[0].organisation == admin_user.organisation
    assert users[0].is_admin == admin_user.is_admin
    assert user_schema.dump(users[0])["groups"] == [1, 2]

    assert users[1].id == regular_user.id
    assert users[1].first_name == regular_user.first_name
    assert users[1].last_name == regular_user.last_name
    assert users[1].email == regular_user.email
    assert users[1].organisation == regular_user.organisation
    assert users[1].is_admin == regular_user.is_admin
    assert user_schema.dump(users[1])["groups"] == [1, 3]


def test_new_user(client: FlaskClient, default_organisation: Organisation):
    data = {
        "first_name": "test",
        "last_name": "user",
        "email": "test@test.com",
        "organisation_id": default_organisation.id,
        "is_admin": False,
    }

    user: User = new_user(data)

    assert user.id == 1
    assert user.first_name == data["first_name"]
    assert user.last_name == data["last_name"]
    assert user.email == data["email"]
    assert user.organisation == default_organisation
    assert user.is_admin == data["is_admin"]
    assert user_schema.dump(user)["groups"] == [1, 2]

    assert organisation_schema.dump(default_organisation)["groups"] == [1, 2]


def test_new_users(client: FlaskClient, default_organisation: Organisation):
    admin_data = {
        "first_name": "admin",
        "last_name": "user",
        "email": "admin@test.com",
        "organisation_id": default_organisation.id,
        "is_admin": True,
    }

    regular_data = {
        "first_name": "test",
        "last_name": "user",
        "email": "test@test.com",
        "organisation_id": default_organisation.id,
        "is_admin": False,
    }

    users: List[User] = new_users([admin_data, regular_data])

    assert users[0].id == 1
    assert users[0].first_name == admin_data["first_name"]
    assert users[0].last_name == admin_data["last_name"]
    assert users[0].email == admin_data["email"]
    assert users[0].organisation == default_organisation
    assert users[0].is_admin == admin_data["is_admin"]
    assert user_schema.dump(users[0])["groups"] == [1, 2]

    assert users[1].id == 2
    assert users[1].first_name == regular_data["first_name"]
    assert users[1].last_name == regular_data["last_name"]
    assert users[1].email == regular_data["email"]
    assert users[1].organisation == default_organisation
    assert users[1].is_admin == regular_data["is_admin"]
    assert user_schema.dump(users[1])["groups"] == [1, 3]

    assert organisation_schema.dump(default_organisation)["groups"] == [1, 2, 3]


def test_edit_user(client: FlaskClient, regular_user: User):
    data = {"last_name": "user updated"}

    user: User = edit_user(regular_user.id, data)

    assert user.id == regular_user.id
    assert user.first_name == regular_user.first_name
    assert user.last_name == data["last_name"]
    assert user.email == regular_user.email
    assert user.organisation == regular_user.organisation
    assert user.is_admin == regular_user.is_admin

    with pytest.raises(Exception):
        edit_user(100, data)


def test_remove_user(client: FlaskClient, regular_user: User):
    organisation: Organisation = regular_user.organisation
    assert len(organisation.users) == 1
    assert len(organisation.groups) == 2
    user = remove_user(regular_user.id)

    assert user.id == regular_user.id
    assert fetch_user(regular_user.id) is None

    db.session.refresh(organisation)
    assert len(organisation.users) == 0
    assert len(organisation.groups) == 1

    with pytest.raises(Exception):
        remove_user(100)


def test_add_group_to_user(client: FlaskClient, regular_user: User):
    assert user_schema.dump(regular_user)["groups"] == [1, 2]

    group: Group = new_group(
        {"name": "another group", "organisation_id": regular_user.organisation_id}
    )

    add_user_to_group(regular_user, group)

    assert user_schema.dump(regular_user)["groups"] == [1, 2, 3]

    external_group: Group = new_group({"name": "external group"})

    with pytest.raises(Exception):
        add_user_to_group(regular_user, external_group)
