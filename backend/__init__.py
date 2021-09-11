from flask import Flask
from .models import db, migrate


def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    return app