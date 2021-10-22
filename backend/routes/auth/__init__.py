from flask.json import jsonify
from flask_jwt_extended.utils import set_access_cookies, unset_jwt_cookies
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required
from marshmallow import Schema, fields

from ...schema.auth import UserSchema
from ...methods.auth.users import fetch_user_by_email
from ...models.auth import User

api = Blueprint(
    "Auth: Login & Registration", __name__, description="Login and Registration Flows"
)


class LoginSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)


@api.route("/login")
class Login(MethodView):
    @api.arguments(LoginSchema)
    @api.alt_response(200, schema=UserSchema)
    def post(self, data: dict):
        """Login and receive an access token"""
        user: User = fetch_user_by_email(data["email"])
        if user is None or not user.check_password(data["password"]):
            abort(404, "Wrong email or password")

        response = jsonify(UserSchema().dump(user))
        access_token = create_access_token(user)
        set_access_cookies(response, access_token)

        return response


@api.route("/logout")
class Logout(MethodView):
    @api.response(204)
    def post(self):
        response = jsonify()
        unset_jwt_cookies(response)
        return response, 204


@api.route("/protected")
class DummyProtected(MethodView):
    @api.response(200)
    @jwt_required()
    def get(self):
        return jsonify()
