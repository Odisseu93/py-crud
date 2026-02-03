import uuid

from sqlalchemy import (
    Column,
    String,
    Boolean,
    Float,
)
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base


class Product(Base):
    """
    SQLAlchemy ORM model representing the 'products' table.
    """

    __tablename__ = 'products'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid7)
    name = Column('name', String, nullable=False)
    price = Column('price', Float, nullable=False)
    sku = Column('sku', String, unique=True)
    is_active = Column('is_active', Boolean, default=True)

    # constructor
    def __init__(self, name, price, is_active=True, sku=None):
        self.name = name
        self.price = price
        self.is_active = is_active
        self.sku = sku
