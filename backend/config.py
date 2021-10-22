import os


def env2bool(name: str, default: bool = False) -> bool:
    return os.getenv(name, str(default)).lower() in ("true", "1", "t")


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
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", os.urandom(24))
    JWT_TOKEN_LOCATION = ["cookies", "headers"]
    JWT_COOKIE_CSRF_PROTECT = env2bool("JWT_COOKIE_CSRF_PROTECT", False)
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 86400))
    DATA_FOLDER = os.getenv("DATA_FOLDER", "data")
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
        "render-style": "view",
        "layout": "row",
        "schema-style": "tree",
        "default-schema-tab": "example",
        "primary-color": "#3392FF",
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
    JWT_SECRET_KEY = "TESTSECRET"
    JWT_TOKEN_LOCATION = ["cookies", "headers"]
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_ACCESS_TOKEN_EXPIRES = False
    API_TITLE = "Dataportal 4 API"
    API_VERSION = "v0.1"
    OPENAPI_VERSION = "3.0.2"
    PROPAGATE_EXCEPTIONS = False
