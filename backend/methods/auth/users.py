from typing import List
from ...models import db
from ...models.auth import Group, User, GroupUser
from ...methods.auth.groups import new_group
from ...schema.auth import user_schema, users_schema


def fetch_user(user_id) -> User:
    user: User = User.query.get(user_id)
    return user


def fetch_users() -> List[User]:
    users: List[User] = User.query.order_by("id").all()
    return users


def new_user_group(user: User) -> Group:
    group: Group = new_group(
        {"name": user.email, "organisation_id": user.organisation_id, "is_user": True}
    )
    user.groups.append(group)
    return group


def new_user(data) -> User:
    user: User = user_schema.load(data)
    db.session.add(user)
    db.session.flush()
    add_user_to_organisation_group(user)
    db.session.add(new_user_group(user))
    db.session.flush()
    return user


def new_users(data) -> List[User]:
    users: List[User] = users_schema.load(data)
    db.session.add_all(users)
    db.session.flush()
    for user in users:
        add_user_to_organisation_group(user)
        db.session.add(new_user_group(user))
    db.session.flush()
    return users


def edit_user(user_id: int, data: dict) -> User:
    user: User = User.query.get(user_id)
    if user is None:
        raise Exception(f"User {user_id} not found")

    user_schema.load(data, instance=user, partial=True)
    db.session.flush()
    return user


def remove_user(user_id) -> User:
    user: User = User.query.get(user_id)
    if user is None:
        raise Exception(f"User {user_id} not found")

    user_group = (
        Group.query.filter_by(is_user=True)
        .join(GroupUser)
        .filter_by(user_id=user.id)
        .one()
    )
    db.session.delete(user)
    db.session.delete(user_group)
    db.session.flush()
    return user


def add_user_to_group(user: User, group: Group):
    if user.organisation_id != group.organisation_id:
        raise Exception("User and Group are in different Organisations")

    user.groups.append(group)


def add_user_to_organisation_group(user: User):
    organisation_group = Group.query.filter_by(
        organisation=user.organisation, is_default=True
    ).one()
    user.groups.append(organisation_group)
