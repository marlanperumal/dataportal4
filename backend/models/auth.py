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
    name = Column(String, unique=True, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        group = Group(name=self.name, organisation=self, is_default=True)
        db.session.add(group)
        db.session.flush()


class Group(db.Model):
    __tablename__ = "group"
    __table_args__ = (UniqueConstraint("organisation_id", "name"), {"schema": "auth"})

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    organisation_id = Column(
        Integer, ForeignKey("auth.organisation.id", ondelete="CASCADE"), index=True
    )
    is_user = Column(Boolean, default=False)
    is_default = Column(Boolean, default=False)

    organisation = relationship(
        "Organisation",
        backref=backref(
            "groups",
            cascade="all,delete",
            passive_deletes=True,
            lazy="subquery",
            order_by="Group.id",
        ),
    )


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, nullable=False)
    organisation_id = Column(Integer, ForeignKey("auth.organisation.id"), index=True)
    is_admin = Column(Boolean, default=False)

    organisation = relationship(
        "Organisation", backref=backref("users", passive_deletes="all")
    )
    groups = relationship(
        "Group", secondary=GroupUser.__table__, backref="users", order_by="Group.id"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        organisation_group: Group = Group.query.filter_by(
            organisation_id=self.organisation_id, is_default=True
        ).one()
        user_group: Group = Group(
            name=self.email, organisation_id=self.organisation_id, is_user=True
        )
        self.groups.append(organisation_group)
        self.groups.append(user_group)


class Package(db.Model):
    __tablename__ = "package"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)


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
