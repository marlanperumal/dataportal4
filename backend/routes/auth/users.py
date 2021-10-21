from flask_smorest import Blueprint
from flask.views import MethodView

from ...methods.auth.users import edit_user, fetch_user, fetch_users, remove_user
from ...schema.auth import UserSchema
from ...models.auth import User
from ...models import db

api = Blueprint("Auth: Users", __name__, description="Application Users")


@api.route("")
class Users(MethodView):
    @api.response(200, UserSchema(many=True))
    def get(self):
        """Get a list of all users"""
        users: list[User] = fetch_users()
        return users

    @api.arguments(UserSchema)
    @api.response(201, UserSchema)
    def post(self, user: User):
        """Add a new user"""
        db.session.add(user)
        db.session.commit()
        return user


@api.route("/batch")
class UsersByBatch(MethodView):
    @api.arguments(UserSchema(many=True))
    @api.response(201, UserSchema(many=True))
    def post(self, users: list[User]):
        """Add a batch of new users"""
        db.session.add_all(users)
        db.session.commit()
        return users


@api.route("/<user_id>")
class UsersById(MethodView):
    @api.response(200, UserSchema)
    def get(self, user_id: int):
        """Get user by id"""
        user: User = fetch_user(user_id)
        return user

    @api.arguments(UserSchema(load_instance=False, partial=True))
    @api.response(200, UserSchema)
    def patch(self, data: User, user_id: int):
        """Edit user details"""
        user: User = edit_user(user_id, data)
        db.session.commit()
        return user

    @api.response(200, UserSchema)
    def delete(self, user_id: int):
        """Remove a user"""
        user = remove_user(user_id)
        db.session.commit()
        return user
