from typing import List
from flask.testing import FlaskClient

from ...models.auth import User
from ...methods.auth.users import fetch_users


def test_fetch_users(client: FlaskClient, admin_user: User, regular_user: User):
    users: List[User] = fetch_users()
    assert len(users) == 2

    assert users[0].first_name == admin_user.first_name
    assert users[0].last_name == admin_user.last_name
    assert users[0].email == admin_user.email
    assert users[0].organisation == admin_user.organisation
    assert users[0].is_admin == admin_user.is_admin

    assert users[1].first_name == regular_user.first_name
    assert users[1].last_name == regular_user.last_name
    assert users[1].email == regular_user.email
    assert users[1].organisation == regular_user.organisation
    assert users[1].is_admin == regular_user.is_admin
