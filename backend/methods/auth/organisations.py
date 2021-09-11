from typing import List
from ...models import db
from ...models.auth import Organisation
from ...schema.auth import organisation_schema, organisations_schema


def fetch_organisations() -> List[Organisation]:
    organisations: List[Organisation] = Organisation.query.order_by("id").all()
    return organisations


def fetch_organisation(organisation_id) -> Organisation:
    organisation: Organisation = Organisation.query.get(organisation_id)
    return organisation


def new_organisation(data) -> Organisation:
    organisation: Organisation = organisation_schema.load(data)
    db.session.add(organisation)
    db.session.flush()
    return organisation


def new_organisations(data) -> List[Organisation]:
    organisations: List[Organisation] = organisations_schema.load(data)
    db.session.bulk_save_objects(organisations)
    db.session.flush()
    return organisations


def edit_organisation(organisation_id, data) -> Organisation:
    organisation: Organisation = Organisation.query.get(organisation_id)
    if organisation is None:
        raise Exception(f"Organisation {organisation_id} not found")

    organisation_schema.load(data, instance=organisation, partial=True)
    return organisation


def remove_organisation(organisation_id) -> Organisation:
    organisation: Organisation = Organisation.query.get(organisation_id)
    if organisation is None:
        raise Exception(f"Organisation {organisation_id} not found")

    db.session.delete(organisation)
    return organisation
