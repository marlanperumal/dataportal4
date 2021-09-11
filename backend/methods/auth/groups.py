from typing import List
from ...models import db
from ...models.auth import Group
from ...schema.auth import group_schema, groups_schema


def fetch_group(group_id) -> Group:
    group: Group = Group.query.get(group_id)
    return group


def fetch_groups() -> List[Group]:
    groups: List[Group] = Group.query.order_by("id").all()
    return groups


def new_group(data) -> Group:
    group: Group = group_schema.load(data)
    db.session.add(group)
    db.session.flush()
    return group


def new_groups(data) -> List[Group]:
    groups: List[Group] = groups_schema.load(data)
    db.session.add_all(groups)
    db.session.flush()
    return groups


def edit_group(group_id: int, data: dict) -> Group:
    group: Group = Group.query.get(group_id)
    if group is None:
        raise Exception(f"Group {group_id} not found")

    group_schema.load(data, instance=group, partial=True)
    db.session.flush()
    return group


def remove_group(group_id) -> Group:
    group: Group = Group.query.get(group_id)
    if group is None:
        raise Exception(f"Group {group_id} not found")

    if group.is_default:
        raise Exception(
            "Cannot remove Organisation Default Group. Will cascade with Organisation"
        )
    if group.is_user:
        raise Exception("Cannot remove User Group. Will cascade with User")

    db.session.delete(group)
    db.session.flush()
    return group
