import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///:memory:")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "future": True,
        "execution_options": {
            "schema_translate_map": {"auth": None, "meta": None, "space": None}
        },
    }
    DATA_FOLDER = "data"


class TestConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///:memory:")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "future": True,
        "execution_options": {
            "schema_translate_map": {"auth": None, "meta": None, "space": None}
        },
    }
    DATA_FOLDER = "data"
