import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import Base, auth, meta, work  # noqa: F401


SQLALCHEMY_CONNECTION_STRING = os.getenv("SQLALCHEMY_CONNECTION_STRING")

engine = create_engine(
    SQLALCHEMY_CONNECTION_STRING,
    connect_args={"check_same_thread": False},
    execution_options={"schema_translate_map": {
        "auth": None,
        "meta": None,
        "work": None,
    }}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)


def drop_db():
    Base.metadata.drop_all(bind=engine)
