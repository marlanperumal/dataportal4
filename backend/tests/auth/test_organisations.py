import pytest
from typing import List
from flask.testing import FlaskClient

from ...models import db
from ...models.auth import Organisation, Group, User
from ...methods.auth.organisations import (
    fetch_organisation,
    fetch_organisations,
    new_organisation,
    new_organisations,
    edit_organisation,
    remove_organisation,
)
from ...methods.auth.users import remove_user
from ...schema.auth import organisation_schema


def test_fetch_organisation(client: FlaskClient, default_organisation):
    organisation: Organisation = fetch_organisation(default_organisation.id)

    assert organisation.id == default_organisation.id
    assert organisation.name == default_organisation.name
    assert organisation_schema.dump(organisation)["groups"] == [1]


def test_fetch_organisations(client: FlaskClient, default_organisation):
    organisations: List[Organisation] = fetch_organisations()

    assert organisations[0].id == default_organisation.id
    assert organisations[0].name == default_organisation.name
    assert organisation_schema.dump(organisations[0])["groups"] == [1]


def test_new_organisation(client: FlaskClient):
    data = {"name": "Another Organisation"}

    organisation: Organisation = new_organisation(data)

    assert organisation.id == 1
    assert organisation.name == data["name"]
    assert len(organisation.groups) == 1
    group: Group = organisation.groups[0]
    assert group.id == 1
    assert group.name == organisation.name
    assert group.is_default
    assert not group.is_user


def test_new_organisations(client: FlaskClient):
    data = [{"name": "Another Organisation"}, {"name": "Yet Another Organisation"}]

    organisations: List[Organisation] = new_organisations(data)

    assert organisations[0].id == 1
    assert organisations[0].name == data[0]["name"]
    assert len(organisations[0].groups) == 1
    group: Group = organisations[0].groups[0]
    assert group.id == 1
    assert group.name == organisations[0].name
    assert group.is_default
    assert not group.is_user

    assert organisations[1].id == 2
    assert organisations[1].name == data[1]["name"]
    assert len(organisations[1].groups) == 1
    group: Group = organisations[1].groups[0]
    assert group.id == 2
    assert group.name == organisations[1].name
    assert group.is_default
    assert not group.is_user


def test_edit_organisation(client: FlaskClient, default_organisation: Organisation):
    data = {"name": "Another Organisation"}

    organisation: Organisation = edit_organisation(default_organisation.id, data)

    assert organisation.id == default_organisation.id
    assert organisation.name == data["name"]
    assert organisation_schema.dump(organisation)["groups"] == [1]
    assert organisation.groups[0].name == data["name"]

    with pytest.raises(Exception):
        edit_organisation(100, data)


def test_remove_organisation(
    client: FlaskClient, default_organisation: Organisation, regular_user: User
):
    db.session.commit()
    with pytest.raises(Exception):
        remove_organisation(100)

    with pytest.raises(Exception):
        remove_organisation(default_organisation.id)

    db.session.rollback()
    remove_user(regular_user.id)
    organisation = remove_organisation(default_organisation.id)
    assert organisation.id == default_organisation.id
    assert fetch_organisation(default_organisation.id) is None
    assert Group.query.first() is None
