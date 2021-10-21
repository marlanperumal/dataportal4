from flask import request, json, Response

from . import create_app
from .config import Config
from .models import db
from .models.sys import QueryLog
from . import methods, models, routes, schema, workers

app = create_app(Config)


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "methods": methods,
        "models": models,
        "routes": routes,
        "schema": schema,
        "workers": workers,
    }


@app.after_request
def log_response_info(response: Response) -> Response:
    body = request.get_json()
    query_log = QueryLog(
        request_type=request.method,
        endpoint=request.path,
        params=request.query_string.decode("utf-8"),
        body=json.dumps(body) if body else None,
        success=response.status_code < 300,
        status_code=response.status_code,
    )
    db.session.add(query_log)
    db.session.commit()
    return response
