from . import ma
from ..models.auth import User, Organisation


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True

    id = ma.auto_field(dump_only=True)


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class OrganisationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Organisation
        load_instance = True
        include_fk = True

    id = ma.auto_field(dump_only=True)


organisation_schema = OrganisationSchema()
organisations_schema = OrganisationSchema(many=True)
