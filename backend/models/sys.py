from sqlalchemy import Column, Integer, String, Boolean, DateTime, func

from . import db


class QueryLog(db.Model):
    __tablename__ = "query_log"
    __table_args__ = {"schema": "sys"}

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, index=True, server_default=func.now())
    request_type = Column(String)
    endpoint = Column(String)
    params = Column(String)
    body = Column(String)
    success = Column(Boolean)
    status_code = Column(Integer)
