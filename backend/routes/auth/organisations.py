from typing import List
from flask_smorest import Blueprint
from flask.views import MethodView

from ...schema.auth import OrganisationSchema
from ...models.auth import Organisation
from ...models import db
from ...methods.auth.organisations import (
    fetch_organisation,
    fetch_organisations,
    edit_organisation,
    remove_organisation,
)

api = Blueprint("Auth: Organisations", __name__, description="Client Organisations")


@api.route("")
class Organisations(MethodView):
    @api.response(200, OrganisationSchema(many=True))
    def get(self):
        """Get a list of all organisations"""
        organisations: List[Organisation] = fetch_organisations()
        return organisations

    @api.arguments(OrganisationSchema)
    @api.response(201, OrganisationSchema)
    def post(self, organisation: Organisation):
        """Add a new organisation"""
        db.session.add(organisation)
        db.session.commit()
        return organisation


@api.route("/batch")
class OrganisationByBatch(MethodView):
    @api.arguments(OrganisationSchema(many=True))
    @api.response(201, OrganisationSchema(many=True))
    def post(self, organisations: list[Organisation]):
        """Add a batch of new organisations"""
        db.session.add_all(organisations)
        db.session.commit()
        return organisations


@api.route("/<int:organisation_id>")
class OrganisationsById(MethodView):
    @api.response(200, OrganisationSchema)
    def get(self, organisation_id: int):
        """Get organisation by id"""
        organisation: Organisation = fetch_organisation(organisation_id)
        return organisation

    @api.arguments(OrganisationSchema(load_instance=False))
    @api.response(200, OrganisationSchema)
    def patch(self, data: dict, organisation_id: int):
        """Edit organisation details"""
        organisation: Organisation = edit_organisation(organisation_id, data)
        db.session.commit()
        return organisation

    @api.response(200, OrganisationSchema)
    def delete(self, organisation_id: int):
        """Remove a organisation"""
        organisation: Organisation = remove_organisation(organisation_id)
        db.session.commit()
        return organisation
