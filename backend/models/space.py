from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from . import db


class SavedWorkspace(db.Model):
    __tablename__ = "saved_workspace"
    __table_args__ = {"schema": "space"}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("auth.user.id"))

    user = relationship("User", backref="saved_workspaces")


class Pivot(db.Model):
    __tablename__ = "pivot"
    __table_args__ = {"schema": "space"}

    id = Column(Integer, primary_key=True)


class Trend(db.Model):
    __tablename__ = "trend"
    __table_args__ = {"schema": "space"}

    id = Column(Integer, primary_key=True)


class Dashboard(db.Model):
    __tablename__ = "dashboard"
    __table_args__ = {"schema": "space"}

    id = Column(Integer, primary_key=True)


class Panel(db.Model):
    __tablename__ = "panel"
    __table_args__ = {"schema": "space"}

    id = Column(Integer, primary_key=True)


class DataImport(db.Model):
    __tablename__ = "data_import"
    __table_args__ = {"schema": "space"}

    id = Column(Integer, primary_key=True)
