from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError
from ..models import db
from ..methods.exceptions import NotFoundError


def handle_sqlalchemy_error(e: SQLAlchemyError):
    db.session.rollback()
    return (
        jsonify(
            message=str(e._message()),
            errors={"sqlalchemy": str(e).split("\n")},
            code=409,
            status="Conflict",
        ),
        409,
    )


def handle_not_found_error(e: NotFoundError):
    return jsonify(e.to_dict()), e.status_code
