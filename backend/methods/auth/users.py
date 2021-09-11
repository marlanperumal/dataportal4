from typing import List
from ...models import db
from ...models.auth import User
from ...schema.auth import user_schema, users_schema


def fetch_users() -> List[User]:
    users: List[User] = User.query.order_by("id").all()
    return users


def fetch_user(user_id) -> User:
    user: User = User.query.get(user_id)
    return user


def new_user(data) -> User:
    user: User = user_schema.load(data)
    db.session.add(user)
    db.session.flush()
    return user


def new_users(data) -> List[User]:
    users: List[User] = users_schema.load(data)
    db.session.bulk_save_objects(users)
    db.session.flush()
    return users


def edit_user(user_id: int, data: dict) -> User:
    user: User = User.query.get(user_id)
    if user is None:
        raise Exception(f"User {user_id} not found")

    user_schema.load(data, instance=user, partial=True)
    return user


def remove_user(user_id) -> User:
    user: User = User.query.get(user_id)
    if user is None:
        raise Exception(f"User {user_id} not found")

    db.session.delete(user)
    return user
