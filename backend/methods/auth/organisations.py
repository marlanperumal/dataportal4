from ..exceptions import NotFoundError
from ...models import db
from ...models.auth import Group, Organisation
from ...schema.auth import organisation_schema


def fetch_organisation(organisation_id) -> Organisation:
    organisation: Organisation = Organisation.query.get(organisation_id)
    if organisation is None:
        raise NotFoundError(f"Organisation {organisation_id} not found")
    return organisation


def fetch_organisations() -> list[Organisation]:
    organisations: list[Organisation] = Organisation.query.order_by("id").all()
    return organisations


def new_organisation(data: dict) -> Organisation:
    organisation: Organisation = organisation_schema.load(data)
    db.session.add(organisation)
    return organisation


def new_organisations(data: list[dict]) -> list[Organisation]:
    organisations: list[Organisation] = organisation_schema.load(data)
    db.session.add_all(organisations)
    return organisations


def edit_organisation(organisation_id: int, data: dict) -> Organisation:
    organisation: Organisation = fetch_organisation(organisation_id)

    organisation_schema.load(data, instance=organisation, partial=True)
    organisation_group = Group.query.filter_by(
        organisation=organisation, is_default=True
    ).one()
    organisation_group.name = organisation.name
    return organisation


def remove_organisation(organisation_id: int) -> Organisation:
    organisation: Organisation = fetch_organisation(organisation_id)

    db.session.delete(organisation)
    db.session.flush()
    return organisation
