import datetime
import uuid

from sqlalchemy import Column, String, Boolean, Date
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base


class Users(Base):
    """
    SQLAlchemy ORM model representing the 'users' table.
    """

    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid7)
    name = Column('name', String)
    email = Column('email', String, nullable=False, unique=True)
    password_hash = Column('password_hash', String)
    is_active = Column('is_active', Boolean)
    is_admin = Column('is_admin', Boolean, default=False)
    created_at = Column('created_at', Date, default=datetime.datetime.now)
    updated_at = Column('updated_at', Date, default=datetime.datetime.now)

    # constructor
    def __init__(self, name, email, hash_password, is_active=True, is_admin=False):
        self.name = name
        self.email = email
        self.hash_password = hash_password
        self.is_active = is_active
        self.is_admin = is_admin
