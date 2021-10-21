from flask import Flask
from flask_smorest import Api
from sqlalchemy.exc import SQLAlchemyError

from .methods import exceptions
from .models import db, migrate
from .schema import ma
from .schema.auth import UserSchema, OrganisationSchema
from .routes import api, errors
from .routes.auth import users, organisations


def register_blueprints(api: Api):
    api.register_blueprint(users.api, url_prefix="/auth/users")
    api.register_blueprint(organisations.api, url_prefix="/auth/organisations")


def register_error_handlers(app: Flask):
    app.register_error_handler(SQLAlchemyError, errors.handle_sqlalchemy_error)
    app.register_error_handler(exceptions.NotFoundError, errors.handle_not_found_error)


def register_apispec_components(api: Api):
    api.spec.components.schema("UserEdit", schema=UserSchema(partial=True))
    api.spec.components.schema(
        "OrganisationEdit", schema=OrganisationSchema(partial=True)
    )


def create_app(Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    api.init_app(app)
    register_apispec_components(api)
    register_blueprints(api)
    register_error_handlers(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    return app
