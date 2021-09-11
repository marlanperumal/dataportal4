import pytest

from ..models import db
from .. import create_app
from ..config import TestConfig

app = create_app(TestConfig)


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
            yield client

            db.session.commit()
