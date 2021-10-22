from flask.testing import FlaskClient

from ...models.auth import User


def test_login(client: FlaskClient, regular_user: User):
    response = client.get("/auth/protected")
    assert response.status_code == 401

    data = {"email": regular_user.email, "password": "regular_password"}
    response = client.post("/auth/login", json=data)
    assert response.status_code == 200
    response_data: dict = response.get_json()

    assert response_data["id"] == regular_user.id

    response = client.get("/auth/protected")
    assert response.status_code == 200

    response = client.post("/auth/logout")
    assert response.status_code == 204

    response = client.get("/auth/protected")
    assert response.status_code == 401
