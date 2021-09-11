from . import ma
from ..models.auth import User, Organisation, Group, GroupUser


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True

    id = ma.auto_field(dump_only=True)
    groups = ma.auto_field(dump=True)


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class OrganisationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Organisation
        load_instance = True
        include_fk = True

    id = ma.auto_field(dump_only=True)
    groups = ma.auto_field(dump_only=True)


organisation_schema = OrganisationSchema()
organisations_schema = OrganisationSchema(many=True)


class GroupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Group
        load_instance = True
        include_fk = True

    id = ma.auto_field(dump_only=True)


group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)


class UserGroupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GroupUser
        load_instance = True
        include_fk = True

    user_id = ma.auto_field(dump_only=True)
    group_id = ma.auto_field(dump_only=True)


user_group_schema = UserGroupSchema()
user_groups_schema = UserGroupSchema(many=True)
