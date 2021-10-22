from functools import wraps
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt
from ...models.auth import User

jwt = JWTManager()


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.get(identity)


@jwt.additional_claims_loader
def add_claims_to_access_token(user):
    return {"admin": user.is_admin, "organisation_id": user.organisation_id}


def admin_required(fn):
    @wraps(fn)
    def admin_wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        admin = claims.get("admin")
        if not admin:
            return {"msg": "Admins only!"}, 403
        else:
            return fn(*args, **kwargs)

    return admin_wrapper
