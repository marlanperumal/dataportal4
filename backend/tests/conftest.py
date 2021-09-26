import pytest
from flask.testing import FlaskClient

from .. import create_app
from ..config import TestConfig
from ..models import db
from ..models.auth import User, Organisation
from ..models.meta import Dataset
from ..methods.auth.users import new_user
from ..methods.auth.organisations import new_organisation
from ..methods.meta.datasets import new_dataset

app = create_app(TestConfig)


@pytest.fixture
def client() -> FlaskClient:
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
            db.session.execute("pragma foreign_keys=on")
            yield client


@pytest.fixture
def default_organisation():
    data = {"name": "Default Organisation"}
    organisation: Organisation = new_organisation(data)
    return organisation


@pytest.fixture
def admin_user(default_organisation: Organisation):
    data = {
        "first_name": "admin",
        "last_name": "user",
        "email": "admin@test.com",
        "organisation_id": default_organisation.id,
        "is_admin": True,
    }
    user: User = new_user(data)
    return user


@pytest.fixture
def regular_user(default_organisation: Organisation):
    data = {
        "first_name": "test",
        "last_name": "user",
        "email": "test@test.com",
        "organisation_id": default_organisation.id,
        "is_admin": False,
    }
    user: User = new_user(data)
    return user


@pytest.fixture
def default_dataset():
    data = {
        "name": "Dataset 1",
        "collection": "Collection 1",
        "priority": 100,
        "is_hidden": False,
        "is_locked": False,
    }
    dataset: Dataset = new_dataset(data)
    return dataset
