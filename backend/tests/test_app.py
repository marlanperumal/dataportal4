from ..models.auth import db, User


def test_app(client):
    assert True


def test_user(client):
    user = User()
    db.session.add(user)
    db.session.flush()
    assert user.id == 1
