from ..exceptions import NotFoundError
from ...models import db
from ...models.auth import Group, User, GroupUser
from ...schema.auth import user_schema


def fetch_user_by_email(email) -> User:
    user: User = User.query.filter_by(email=email).first()
    return user


def fetch_user(user_id) -> User:
    user: User = User.query.get(user_id)
    if user is None:
        raise NotFoundError(f"User {user_id} not found")
    return user


def fetch_users() -> list[User]:
    users: list[User] = User.query.order_by("id").all()
    return users


def fetch_user_group(user: User) -> Group:
    user_group = (
        Group.query.filter_by(is_user=True)
        .join(GroupUser)
        .filter_by(user_id=user.id)
        .one()
    )
    return user_group


def new_user(data: dict) -> User:
    password = data.pop("password")
    user: User = user_schema.load(data)
    user.set_password(password)
    db.session.add(user)
    return user


def new_users(data: list[dict]) -> list[User]:
    users: list[User] = [new_user(d) for d in data]
    return users


def edit_user(user_id: int, data: dict) -> User:
    user: User = fetch_user(user_id)

    user_schema.load(data, instance=user, partial=True)
    user_group: Group = fetch_user_group(user)
    user_group.name = user.email
    return user


def remove_user(user_id) -> User:
    user: User = fetch_user(user_id)

    user_group: Group = fetch_user_group(user)
    db.session.delete(user_group)
    db.session.delete(user)
    return user


def add_user_to_group(user: User, group: Group):
    if user.organisation_id != group.organisation_id:
        raise Exception("User and Group are in different Organisations")

    user.groups.append(group)
