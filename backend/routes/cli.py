from flask import Blueprint, current_app

from ..models import db
from ..methods.auth.organisations import new_organisation
from ..methods.auth.users import new_user

api = Blueprint("database", __name__)


@api.cli.command("init_db")
def init_db():
    if current_app.config["DB_TYPE"] != "sqlite":
        db.session.execute("CREATE SCHEMA IF NOT EXISTS auth")
        db.session.execute("CREATE SCHEMA IF NOT EXISTS meta")
        db.session.execute("CREATE SCHEMA IF NOT EXISTS space")
        db.session.execute("CREATE SCHEMA IF NOT EXISTS sys")
        db.session.commit()
    db.create_all()

    organisation = new_organisation({"name": "Default Organisation"})
    print(f"Created Organisation {organisation.name}")
    user = new_user(
        {
            "first_name": "Admin",
            "last_name": "User",
            "email": "admin@eighty20.co.za",
            "password": "admin",
            "organisation_id": 1,
            "is_admin": True,
        }
    )
    print(f"Created Admin User {user.email} with password 'admin'. Please change this")
    db.session.commit()
    print("Initialised all schemas and tables")


@api.cli.command("drop_db")
def drop_db():
    db.drop_all()
    if current_app.config["DB_TYPE"] != "sqlite":
        db.session.execute("DROP SCHEMA IF EXISTS auth")
        db.session.execute("DROP SCHEMA IF EXISTS meta")
        db.session.execute("DROP SCHEMA IF EXISTS space")
        db.session.execute("DROP SCHEMA IF EXISTS sys")
        db.session.commit()
    print("Dropped all schemas and tables")


@api.cli.command("init_auth")
def create_admin():
    admin = new_user({"first_name": "Admin", "last_name": ""})
    print(admin)
