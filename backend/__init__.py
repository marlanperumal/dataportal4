from flask import Flask
from .models import db, migrate
from .schema import ma


def create_app(Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    return app
