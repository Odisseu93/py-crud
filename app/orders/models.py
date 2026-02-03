import datetime
import uuid

from sqlalchemy import Column, String, Date, DECIMAL, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_utils import ChoiceType

from app.core.database import Base


class Order(Base):
    """
    SQLAlchemy ORM model representing the 'orders' table.
    """

    __tablename__ = 'orders'

    ORDER_STATUS = (
        ('PENDING', 'PENDING'),
        ('CANCELED', 'CANCELED'),
        ('COMPLETED', 'COMPLETED'),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid7)
    user_id = Column('user_id', ForeignKey('users.id'))
    status = Column(
        'status', String, ChoiceType(choices=ORDER_STATUS)
    )  # PENDING | CANCELED | COMPLETED
    total_price = Column('total_pice', DECIMAL(10, 2), default=0)
    created_at = Column('created_at', Date, default=datetime.datetime.now)
    updated_at = Column('updated_at', Date, default=datetime.datetime.now)

    # constructor
    def __init__(self, user_id, price=0, status='PENDING', total_pice=0):
        self.user_id = user_id
        self.status = status
        self.total_price = total_pice
