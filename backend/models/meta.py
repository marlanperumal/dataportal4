from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKeyConstraint
from . import Base


class Dataset(Base):
    __tablename__ = "dataset"
    __table_args__ = {"schema": "meta"}

    id = Column(String, primary_key=True)
    name = Column(String)
    collection = Column(String)
    priority = Column(Integer)
    is_hidden = Column(Boolean, index=True, default=False)
    is_locked = Column(Boolean, index=True, default=True)


class Service(Base):
    __tablename__ = "service"
    __table_args__ = {"schema": "meta"}

    id = Column(String, primary_key=True)
    type = Column(String)
    conn_uri = Column(String)


class Table(Base):
    __tablename__ = "table"
    __table_args__ = {"schema": "meta"}

    id = Column(String, primary_key=True)
    name = Column(String)
    dataset_id = Column(String, ForeignKey("meta.dataset.id"), index=True)
    period_type = Column(String)
    period_name = Column(String)
    period_date = Column(Date)
    service_id = Column(String, ForeignKey("meta.service.id"), index=True)
    service_handle = Column(String)
    documentation_link = Column(String)
    is_hidden = Column(Boolean, index=True, default=False)
    is_locked = Column(Boolean, index=True, default=False)
    max_filed = Column(Integer)

    dataset = relationship("Dataset", backref="tables")
    service = relationship("Service", backref="tables")


class TableHandle(Base):
    __tablename__ = "table_handle"
    __table_args__ = {"schema": "meta"}

    id = Column(Integer, primary_key=True)
    table_id = Column(String, ForeignKey("meta.table.id"), index=True)
    handle = Column(String, index=True)

    table = relationship("Table", backref="handles")


class TableWeight(Base):
    __tablename__ = "table_weight"
    __table_args__ = {"schema": "meta"}

    table_id = Column(String, ForeignKey("meta.table.id"), primary_key=True)
    weight_id = Column(String, primary_key=True)
    name = Column(String)
    weight_field = Column(String)
    index_field = Column(String)

    table = relationship("Table", backref="weights")


class Branch(Base):
    __tablename__ = "branch"
    __table_args__ = {"schema": "meta"}

    id = Column(Integer, primary_key=True)
    name = Column(String)
    table_id = Column(String, ForeignKey("meta.table.id"), index=True)
    parent_id = Column(Integer, ForeignKey("meta.branch.id"), index=True)
    is_root = Column(Boolean, index=True, default=False)
    is_multi = Column(Boolean, default=False)
    multi_type = Column(Integer)
    path = Column(String)

    parent = relationship("Branch", foreign_keys=["parent_id"], backref="children")


class Field(Base):
    __tablename__ = "field"
    __table_args__ = {"schema": "meta"}

    table_id = Column(String, ForeignKey("meta.table.id"), primary_key=True)
    field_id = Column(String, primary_key=True)
    name = Column(String)
    type = Column(String)
    table_handle_id = Column(Integer, ForeignKey("meta.table_handle.id"), index=True)
    branch_id = Column(Integer, index=True)
    is_numeric = Column(Boolean, default=False)
    numeric_type = Column(String)
    sort_order = Column(Integer)
    is_hidden = Column(Boolean, index=True, default=False)
    is_locked = Column(Boolean, index=True, default=False)
    check_weights = Column(Boolean, index=True, default=False)

    table = relationship("Table", backref="fields")
    branch = relationship("Branch", backref="fields")


class FieldWeight(Base):
    __tablename__ = "field_name"
    __table_args__ = (
        ForeignKeyConstraint(["table_id", "weight_id"], ["meta.table_weight.table_id", "meta.table_weight.weight_id"]),
        ForeignKeyConstraint(["table_id", "field_id"], ["meta.field.table_id", "meta.field.field_id"]),
        {"schema": "meta"}
    )

    table_id = Column(String, primary_key=True)
    weight_id = Column(String, primary_key=True)
    field_id = Column(String, primary_key=True)


class Translation(Base):
    __tablename__ = "translation"
    __table_args__ = (
        ForeignKeyConstraint(["table_id", "field_id"], ["meta.field.table_id", "meta.field.field_id"]),
        {"schema": "meta"}
    )

    table_id = Column(String, primary_key=True)
    field_id = Column(String, primary_key=True)
    level_id = Column(String, primary_key=True)
    level_label = Column(String)
    sort_order = Column(Integer)
    is_na = Column(Boolean, default=False)

    field = relationship("Field", backref="translations")
