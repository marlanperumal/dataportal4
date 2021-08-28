from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, UniqueConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from . import Base


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    organisation_id = Column(Integer, ForeignKey("auth.organisation.id"), index=True)

    organisation = relationship("Organisation", backref="users")


class Group(Base):
    __tablename__ = "group"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True)
    name = Column(String)
    organisation_id = Column(Integer, ForeignKey("auth.organisation.id"), index=True)
    is_user = Column(Boolean, default=False)
    is_default = Column(Boolean, default=False)

    organisation = relationship("Organisation", backref="groups")


class UserGroup(Base):
    __tablename__ = "user_group"
    __table_args__ = {"schema": "auth"}

    user_id = Column(Integer, ForeignKey("auth.user.id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("auth.group.id"), primary_key=True)

    user = relationship("User", backref="user_groups")
    group = relationship("Group", backref="user_groups")


class Organisation(Base):
    __tablename__ = "organisation"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True)
    name = Column(String)


class OrganisationGroup(Base):
    __tablename__ = "organisation_group"
    __table_args__ = {"schema": "auth"}

    organisation_id = Column(Integer, ForeignKey("auth.organisation.id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("auth.group.id"), primary_key=True)

    organisation = relationship("Organisation", backref="organisation_groups")
    group = relationship("Group", backref="organisation_groups")


class Package(Base):
    __tablename__ = "package"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Subscription(Base):
    __tablename__ = "subscription"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True)
    organisation_id = Column(Integer, ForeignKey("auth.organisation.id"), index=True)
    package_id = Column(Integer, ForeignKey("auth.package.id"), index=True)
    is_current = Column(Boolean, index=True, default=False)
    is_active = Column(Boolean, index=True, default=False)
    start_date = Column(Date, index=True)
    end_date = Column(Date, index=True)

    organisation = relationship("Organisation", backref="subscriptions")
    package = relationship("Package", backref="subscriptions")


class SubscriptionGroup(Base):
    __tablename__ = "subscription_group"
    __table_args__ = {"schema": "auth"}

    subscription_id = Column(Integer, ForeignKey("auth.subscription.id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("auth.group.id"), primary_key=True)


class PackageContent(Base):
    __tablename__ = "package_content"
    __table_args__ = (
        ForeignKeyConstraint(["table_id", "field_id"], ["meta.field.table_id", "meta.field.field_id"]),
        UniqueConstraint("package_id", "dataset_id", "table_id", "field_id"),
        {"schema": "auth"},
    )

    id = Column(Integer, primary_key=True)
    package_id = Column(Integer, ForeignKey("auth.package.id"), index=True)
    dataset_id = Column(Integer, ForeignKey("meta.dataset.id"), index=True)
    table_id = Column(Integer, ForeignKey("meta.table.id"), index=True)
    field_id = Column(Integer, index=True)
