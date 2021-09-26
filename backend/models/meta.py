from __future__ import annotations
from datetime import date
from typing import List, Optional
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship, backref
from . import db


class Dataset(db.Model):
    __tablename__ = "dataset"
    __table_args__ = {"schema": "meta"}

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    collection: str = Column(String)
    priority: Optional[int] = Column(Integer)
    is_hidden: bool = Column(Boolean, index=True, default=False)
    is_locked: bool = Column(Boolean, index=True, default=True)

    tables: List[Table]


class Service(db.Model):
    __tablename__ = "service"
    __table_args__ = {"schema": "meta"}

    id: int = Column(Integer, primary_key=True)
    type: Optional[str] = Column(String)
    conn_uri: Optional[str] = Column(String)

    tables: List[Table]


class Table(db.Model):
    __tablename__ = "table"
    __table_args__ = {"schema": "meta"}

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    dataset_id: Optional[int] = Column(
        Integer, ForeignKey("meta.dataset.id"), index=True
    )
    period_type: Optional[str] = Column(String)
    period_name: Optional[str] = Column(String)
    period_date: Optional[date] = Column(Date)
    service_id: Optional[int] = Column(
        Integer, ForeignKey("meta.service.id"), index=True
    )
    service_handle: Optional[str] = Column(String)
    documentation_link: Optional[str] = Column(String)
    is_hidden: bool = Column(Boolean, index=True, default=False)
    is_locked: bool = Column(Boolean, index=True, default=False)
    max_fields: Optional[int] = Column(Integer)

    dataset: Dataset = relationship("Dataset", backref="tables")
    service: Service = relationship("Service", backref="tables")

    handles: List[TableHandle]
    branches: List[Branch]
    fields: List[Field]
    table_weights: List[TableWeight]


class TableHandle(db.Model):
    __tablename__ = "table_handle"
    __table_args__ = {"schema": "meta"}

    id: int = Column(Integer, primary_key=True)
    table_id: int = Column(Integer, ForeignKey("meta.table.id"), index=True)
    handle: str = Column(String, index=True)
    index_handle: str = Column(String)

    table: Table = relationship("Table", backref="handles")

    fields: List[Field]


class Branch(db.Model):
    __tablename__ = "branch"
    __table_args__ = {"schema": "meta"}

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    table_id: int = Column(Integer, ForeignKey("meta.table.id"), index=True)
    parent_id: int = Column(Integer, ForeignKey("meta.branch.id"), index=True)
    is_root: bool = Column(Boolean, index=True, default=False)
    is_multi: bool = Column(Boolean, default=False)
    multi_type: int = Column(Integer)
    path: str = Column(String)

    children: List[Branch] = relationship(
        "Branch", backref=backref("parent", remote_side=[id])
    )
    table: Table = relationship("Table", backref="branches")

    parent: Branch
    fields: List[Field]


class Field(db.Model):
    __tablename__ = "field"
    __table_args__ = {"schema": "meta"}

    id: int = Column(Integer, primary_key=True)
    table_id: str = Column(String, ForeignKey("meta.table.id"), index=True)
    name: str = Column(String)
    type: str = Column(String)
    handle: str = Column(String)
    table_handle_id: int = Column(
        Integer, ForeignKey("meta.table_handle.id"), index=True
    )
    branch_id: int = Column(Integer, ForeignKey("meta.branch.id"), index=True)
    is_numeric: bool = Column(Boolean, default=False)
    numeric_type: str = Column(String)
    sort_order: int = Column(Integer)
    is_hidden: bool = Column(Boolean, index=True, default=False)
    is_locked: bool = Column(Boolean, index=True, default=False)
    check_weights: bool = Column(Boolean, index=True, default=False)

    table: Table = relationship("Table", backref="fields")
    table_handle: TableHandle = relationship(
        "TableHandle",
        primaryjoin="Field.table_handle_id == TableHandle.id",
        backref="fields",
    )
    branch: Branch = relationship("Branch", backref="fields")

    weight_table_weights: List[TableWeight]
    index_table_weights: List[TableWeight]
    field_weights: List[FieldWeight]
    translations: List[Translation]


class TableWeight(db.Model):
    __tablename__ = "table_weight"
    __table_args__ = {"schema": "meta"}

    id: int = Column(Integer, primary_key=True)
    table_id: int = Column(Integer, ForeignKey("meta.table.id"), index=True)
    name: str = Column(String)
    weight_field_id: int = Column(Integer, ForeignKey("meta.field.id"), index=True)
    index_field_id: int = Column(Integer, ForeignKey("meta.field.id"), index=True)

    table: Table = relationship("Table", backref="table_weights")
    weight_field: Field = relationship(
        "Field",
        primaryjoin="TableWeight.weight_field_id == Field.id",
        backref="weight_table_weights",
    )
    index_field: Field = relationship(
        "Field",
        primaryjoin="TableWeight.index_field_id == Field.id",
        backref="index_table_weights",
    )

    field_weights: List[FieldWeight]


class FieldWeight(db.Model):
    __tablename__ = "field_name"
    __table_args__ = {"schema": "meta"}

    id: int = Column(Integer, primary_key=True)
    field_id: int = Column(Integer, ForeignKey("meta.field.id"), index=True)
    table_weight_id: int = Column(
        Integer, ForeignKey("meta.table_weight.id"), index=True
    )

    field: Field = relationship("Field", backref="field_weights")
    table_weight: TableWeight = relationship("TableWeight", backref="field_weights")


class Translation(db.Model):
    __tablename__ = "translation"
    __table_args__ = {"schema": "meta"}

    id: int = Column(Integer, primary_key=True)
    field_id: int = Column(Integer, ForeignKey("meta.field.id"), index=True)
    level: str = Column(String, index=True)
    level_label: str = Column(String)
    sort_order: Optional[int] = Column(Integer)
    is_na: bool = Column(Boolean, default=False)

    field: Field = relationship("Field", backref="translations")
