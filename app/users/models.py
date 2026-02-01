from sqlalchemy import (
    Column,
    String,
    Boolean,
)
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.core.database import Base


class Users(Base):
    """
    SQLAlchemy ORM model representing the 'users' table.
    """

    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid7)
    name = Column('name', String)
    email = Column('email', String, nullable=False, unique=True)
    hash_password = Column('hash_password', String)
    is_active = Column('is_active', Boolean)
    is_admin = Column('is_admin', Boolean, default=False)

    # constructor
    def __init__(self, name, email, hash_password, is_active=True, is_admin=False):
        self.name = name
        self.email = email
        self.hash_password = hash_password
        self.is_active = is_active
        self.is_admin = is_admin
