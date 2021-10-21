from . import create_app
from .config import Config
from .models import db

app = create_app(Config)


@app.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
    db.session.remove()
