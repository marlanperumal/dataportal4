from flask.testing import FlaskClient

from ...models import db
from ...models.auth import Organisation, Group, User


def test_fetch_organisation(client: FlaskClient, default_organisation):
    response = client.get(f"/auth/organisations/{default_organisation.id}")
    response_data: dict = response.get_json()

    assert response_data["id"] == default_organisation.id
    assert response_data["name"] == default_organisation.name
    assert response_data["groups"] == [1]


def test_fetch_organisations(client: FlaskClient, default_organisation):
    response = client.get("/auth/organisations")
    response_data: list[dict] = response.get_json()

    assert response_data[0]["id"] == default_organisation.id
    assert response_data[0]["name"] == default_organisation.name
    assert response_data[0]["groups"] == [1]


def test_new_organisation(client: FlaskClient):
    request_data = {"name": "Another Organisation"}

    response = client.post("/auth/organisations", json=request_data)
    response_data: dict = response.get_json()

    assert response_data["id"] == 1
    assert response_data["name"] == request_data["name"]
    assert len(response_data["groups"]) == 1

    group: Group = Group.query.get(response_data["groups"][0])
    assert group.id == 1
    assert group.name == response_data["name"]
    assert group.is_default
    assert not group.is_user


def test_new_organisations(client: FlaskClient):
    request_data = [
        {"name": "Another Organisation"},
        {"name": "Yet Another Organisation"},
    ]

    response = client.post("/auth/organisations/batch", json=request_data)
    response_data: list[dict] = response.get_json()

    assert response_data[0]["id"] == 1
    assert response_data[0]["name"] == request_data[0]["name"]
    assert len(response_data[0]["groups"]) == 1
    group: Group = Group.query.get(response_data[0]["groups"][0])
    assert group.id == 1
    assert group.name == response_data[0]["name"]
    assert group.is_default
    assert not group.is_user

    assert response_data[1]["id"] == 2
    assert response_data[1]["name"] == request_data[1]["name"]
    assert len(response_data[1]["groups"]) == 1
    group: Group = Group.query.get(response_data[1]["groups"][0])
    assert group.id == 2
    assert group.name == response_data[1]["name"]
    assert group.is_default
    assert not group.is_user


def test_edit_organisation(client: FlaskClient, default_organisation: Organisation):
    request_data = {"name": "Another Organisation"}

    response = client.patch(
        f"/auth/organisations/{default_organisation.id}", json=request_data
    )
    response_data: dict = response.get_json()

    assert response_data["id"] == default_organisation.id
    assert response_data["name"] == request_data["name"]
    assert response_data["groups"] == [1]
    group: Group = Group.query.get(response_data["groups"][0])
    assert group.name == request_data["name"]

    response = client.patch("/auth/organisations/100", json=request_data)
    assert response.status_code == 404


def test_remove_organisation(
    client: FlaskClient, default_organisation: Organisation, regular_user: User
):
    response = client.delete("/auth/organisations/100")
    assert response.status_code == 404

    response = client.delete(f"/auth/organisations/{default_organisation.id}")
    assert response.status_code == 409

    db.session.delete(regular_user)
    db.session.commit()

    response = client.delete(f"/auth/organisations/{default_organisation.id}")
    response_body: dict = response.get_json()
    assert response.status_code == 200
    assert response_body["id"] == default_organisation.id
    assert Organisation.query.get(default_organisation.id) is None
    assert Group.query.first() is None
