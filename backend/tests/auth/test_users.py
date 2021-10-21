import pytest
from flask.testing import FlaskClient

from ...models import db
from ...models.auth import Organisation, User, Group
from ...methods.auth.users import add_user_to_group, new_user, new_users
from ...methods.auth.groups import new_group
from ...schema.auth import user_schema, organisation_schema, group_schema


def test_fetch_user(client: FlaskClient, regular_user: User):
    response = client.get(f"/auth/users/{regular_user.id}")
    assert response.status_code == 200
    response_data: dict = response.get_json()

    assert response_data["id"] == regular_user.id
    assert response_data["first_name"] == regular_user.first_name
    assert response_data["last_name"] == regular_user.last_name
    assert response_data["email"] == regular_user.email
    assert response_data["organisation_id"] == regular_user.organisation_id
    assert response_data["is_admin"] == regular_user.is_admin
    assert response_data["groups"] == [1, 2]


def test_fetch_users(client: FlaskClient, admin_user: User, regular_user: User):
    response = client.get("/auth/users")
    assert response.status_code == 200
    response_data: list[dict] = response.get_json()

    assert len(response_data) == 2

    assert response_data[0]["id"] == admin_user.id
    assert response_data[0]["first_name"] == admin_user.first_name
    assert response_data[0]["last_name"] == admin_user.last_name
    assert response_data[0]["email"] == admin_user.email
    assert response_data[0]["organisation_id"] == admin_user.organisation_id
    assert response_data[0]["is_admin"] == admin_user.is_admin
    assert response_data[0]["groups"] == [1, 2]

    assert response_data[1]["id"] == regular_user.id
    assert response_data[1]["first_name"] == regular_user.first_name
    assert response_data[1]["last_name"] == regular_user.last_name
    assert response_data[1]["email"] == regular_user.email
    assert response_data[1]["organisation_id"] == regular_user.organisation_id
    assert response_data[1]["is_admin"] == regular_user.is_admin
    assert response_data[1]["groups"] == [1, 3]


def test_new_user(client: FlaskClient, default_organisation: Organisation):
    data = {
        "first_name": "test",
        "last_name": "user",
        "email": "test@test.com",
        "organisation_id": default_organisation.id,
        "is_admin": False,
    }

    user: User = new_user(data)
    db.session.flush()
    db.session.refresh(default_organisation)

    assert user.id == 1
    assert user.first_name == data["first_name"]
    assert user.last_name == data["last_name"]
    assert user.email == data["email"]
    assert user.organisation == default_organisation
    assert user.is_admin == data["is_admin"]
    assert user_schema.dump(user)["groups"] == [1, 2]

    assert organisation_schema.dump(default_organisation)["groups"] == [1, 2]


def test_new_user_route(client: FlaskClient, default_organisation: Organisation):
    request_data = {
        "first_name": "test",
        "last_name": "user",
        "email": "test@test.com",
        "organisation_id": default_organisation.id,
        "is_admin": False,
    }

    response = client.post("/auth/users", json=request_data)
    assert response.status_code == 201
    response_data = response.get_json()

    assert response_data["id"] == 1
    assert response_data["first_name"] == request_data["first_name"]
    assert response_data["last_name"] == request_data["last_name"]
    assert response_data["email"] == request_data["email"]
    assert response_data["organisation_id"] == default_organisation.id
    assert response_data["is_admin"] == request_data["is_admin"]


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

    users: list[User] = new_users([admin_data, regular_data])
    db.session.flush()
    db.session.refresh(default_organisation)

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


def test_new_users_route(client: FlaskClient, default_organisation: Organisation):
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

    response = client.post("/auth/users/batch", json=[admin_data, regular_data])
    assert response.status_code == 201
    response_data = response.get_json()

    assert response_data[0]["id"] == 1
    assert response_data[0]["first_name"] == admin_data["first_name"]
    assert response_data[0]["last_name"] == admin_data["last_name"]
    assert response_data[0]["email"] == admin_data["email"]
    assert response_data[0]["organisation_id"] == default_organisation.id
    assert response_data[0]["is_admin"] == admin_data["is_admin"]
    assert response_data[0]["groups"] == [1, 2]

    assert response_data[1]["id"] == 2
    assert response_data[1]["first_name"] == regular_data["first_name"]
    assert response_data[1]["last_name"] == regular_data["last_name"]
    assert response_data[1]["email"] == regular_data["email"]
    assert response_data[1]["organisation_id"] == default_organisation.id
    assert response_data[1]["is_admin"] == regular_data["is_admin"]
    assert response_data[1]["groups"] == [1, 3]

    assert organisation_schema.dump(default_organisation)["groups"] == [1, 2, 3]


def test_edit_user(client: FlaskClient, regular_user: User):
    request_data = {"last_name": "user updated"}

    response = client.patch(f"/auth/users/{regular_user.id}", json=request_data)
    assert response.status_code == 200
    response_data: dict = response.get_json()

    assert response_data["id"] == regular_user.id
    assert response_data["first_name"] == regular_user.first_name
    assert response_data["last_name"] == request_data["last_name"]
    assert response_data["email"] == regular_user.email
    assert response_data["organisation_id"] == regular_user.organisation_id
    assert response_data["is_admin"] == regular_user.is_admin

    response = client.patch("/auth/users/100", json=request_data)
    assert response.status_code == 404


def test_remove_user(client: FlaskClient, regular_user: User):
    organisation: Organisation = regular_user.organisation
    assert len(organisation.users) == 1
    assert len(organisation.groups) == 2

    response = client.delete(f"/auth/users/{regular_user.id}")
    assert response.status_code == 200
    response_data: dict = response.get_json()
    assert response_data["id"] == regular_user.id

    response = client.get(f"/auth/users/{regular_user.id}")
    assert response.status_code == 404

    db.session.refresh(organisation)
    assert len(organisation.users) == 0
    assert len(organisation.groups) == 1

    response = client.delete(f"/auth/users/{regular_user.id}")
    assert response.status_code == 404


def test_add_group_to_user(client: FlaskClient, regular_user: User):
    assert user_schema.dump(regular_user)["groups"] == [1, 2]

    group: Group = new_group(
        group_schema.load(
            {"name": "another group", "organisation_id": regular_user.organisation_id}
        )
    )

    add_user_to_group(regular_user, group)

    assert user_schema.dump(regular_user)["groups"] == [1, 2, 3]

    external_group: Group = new_group(group_schema.load({"name": "external group"}))

    with pytest.raises(Exception):
        add_user_to_group(regular_user, external_group)
