import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///:memory:")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "future": True,
        "execution_options": {
            "schema_translate_map": {
                "auth": None,
                "meta": None,
                "space": None,
                "sys": None,
            }
        },
    }
    JSON_SORT_KEYS = True
    DATA_FOLDER = "data"
    API_TITLE = "Dataportal 4 API"
    API_VERSION = "v0.1"
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_URL_PREFIX = "/apidocs"
    OPENAPI_SWAGGER_UI_PATH = "/swagger"
    OPENAPI_SWAGGER_UI_URL = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_URL = "https://rebilly.github.io/ReDoc/releases/v1.x.x/redoc.min.js"
    OPENAPI_RAPIDOC_PATH = "/rapidoc"
    OPENAPI_RAPIDOC_URL = "https://unpkg.com/rapidoc/dist/rapidoc-min.js"
    OPENAPI_RAPIDOC_CONFIG = {
        "theme": "dark",
        "render-style": "read",
        "layout": "row",
        "schema-style": "tree",
        "default-schema-tab": "example",
        "primary-color": "#1A79FF",
    }


class TestConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "future": True,
        "execution_options": {
            "schema_translate_map": {
                "auth": None,
                "meta": None,
                "space": None,
                "sys": None,
            }
        },
    }
    DATA_FOLDER = "data"
    API_TITLE = "Dataportal 4 API"
    API_VERSION = "v0.1"
    OPENAPI_VERSION = "3.0.2"
    PROPAGATE_EXCEPTIONS = False
