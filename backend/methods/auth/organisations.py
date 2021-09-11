from typing import List
from ...models import db
from ...models.auth import Group, Organisation
from ...methods.auth.groups import new_group
from ...schema.auth import organisation_schema, organisations_schema


def fetch_organisation(organisation_id) -> Organisation:
    organisation: Organisation = Organisation.query.get(organisation_id)
    return organisation


def fetch_organisations() -> List[Organisation]:
    organisations: List[Organisation] = Organisation.query.order_by("id").all()
    return organisations


def new_organisation(data) -> Organisation:
    organisation: Organisation = organisation_schema.load(data)
    db.session.add(organisation)
    db.session.flush()
    db.session.add(new_default_group(organisation))
    db.session.flush()
    return organisation


def new_organisations(data) -> List[Organisation]:
    organisations: List[Organisation] = organisations_schema.load(data)
    db.session.add_all(organisations)
    db.session.flush()
    for organisation in organisations:
        db.session.add(new_default_group(organisation))
    db.session.flush()
    return organisations


def new_default_group(organisation) -> Group:
    group: Group = new_group(
        {
            "name": organisation.name,
            "organisation_id": organisation.id,
            "is_default": True,
        }
    )
    return group


def edit_organisation(organisation_id, data) -> Organisation:
    organisation: Organisation = Organisation.query.get(organisation_id)
    if organisation is None:
        raise Exception(f"Organisation {organisation_id} not found")

    organisation_schema.load(data, instance=organisation, partial=True)
    organisation_group = Group.query.filter_by(
        organisation=organisation, is_default=True
    ).one()
    organisation_group.name = organisation.name
    return organisation


def remove_organisation(organisation_id) -> Organisation:
    organisation: Organisation = Organisation.query.get(organisation_id)
    if organisation is None:
        raise Exception(f"Organisation {organisation_id} not found")

    db.session.delete(organisation)
    db.session.flush()
    return organisation
