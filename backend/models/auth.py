from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean,
    Date,
    UniqueConstraint,
    ForeignKeyConstraint,
)
from sqlalchemy.orm import relationship, backref
from . import db


class GroupUser(db.Model):
    __tablename__ = "group_user"
    __table_args__ = {"schema": "auth"}

    group_id = Column(
        Integer, ForeignKey("auth.group.id", ondelete="CASCADE"), primary_key=True
    )
    user_id = Column(
        Integer, ForeignKey("auth.user.id", ondelete="CASCADE"), primary_key=True
    )


class Organisation(db.Model):
    __tablename__ = "organisation"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Group(db.Model):
    __tablename__ = "group"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True)
    name = Column(String)
    organisation_id = Column(
        Integer, ForeignKey("auth.organisation.id", ondelete="CASCADE"), index=True
    )
    is_user = Column(Boolean, default=False)
    is_default = Column(Boolean, default=False)

    organisation = relationship(
        "Organisation",
        backref=backref("groups", cascade="all,delete", passive_deletes=True),
    )


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    organisation_id = Column(Integer, ForeignKey("auth.organisation.id"), index=True)
    is_admin = Column(Boolean)

    organisation = relationship(
        "Organisation", backref=backref("users", passive_deletes="all")
    )
    groups = relationship("Group", secondary=GroupUser.__table__, backref="users")


class Package(db.Model):
    __tablename__ = "package"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Subscription(db.Model):
    __tablename__ = "subscription"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True)
    organisation_id = Column(
        Integer, ForeignKey("auth.organisation.id", ondelete="CASCADE"), index=True
    )
    package_id = Column(Integer, ForeignKey("auth.package.id"), index=True)
    is_current = Column(Boolean, index=True, default=False)
    is_active = Column(Boolean, index=True, default=False)
    start_date = Column(Date, index=True)
    end_date = Column(Date, index=True)

    organisation = relationship(
        "Organisation",
        backref=backref("subscriptions", cascade="all,delete", passive_deletes=True),
    )
    package = relationship("Package", backref="subscriptions")


class SubscriptionGroup(db.Model):
    __tablename__ = "subscription_group"
    __table_args__ = {"schema": "auth"}

    subscription_id = Column(
        Integer,
        ForeignKey("auth.subscription.id", ondelete="CASCADE"),
        primary_key=True,
    )
    group_id = Column(
        Integer, ForeignKey("auth.group.id", ondelete="CASCADE"), primary_key=True
    )

    subscription = relationship(
        "Subscription",
        backref=backref(
            "subscription_groups", cascade="all,delete", passive_deletes=True
        ),
    )
    group = relationship(
        "Group",
        backref=backref(
            "subscription_groups", cascade="all,delete", passive_deletes=True
        ),
    )


class PackageContent(db.Model):
    __tablename__ = "package_content"
    __table_args__ = (
        ForeignKeyConstraint(
            ["table_id", "field_id"], ["meta.field.table_id", "meta.field.field_id"]
        ),
        UniqueConstraint("package_id", "dataset_id", "table_id", "field_id"),
        {"schema": "auth"},
    )

    id = Column(Integer, primary_key=True)
    package_id = Column(Integer, ForeignKey("auth.package.id"), index=True)
    dataset_id = Column(Integer, ForeignKey("meta.dataset.id"), index=True)
    table_id = Column(Integer, ForeignKey("meta.table.id"), index=True)
    field_id = Column(Integer, index=True)
