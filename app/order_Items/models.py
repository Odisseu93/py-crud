from sqlalchemy import Column, Integer, Decimal, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.core.database import Base


class OrderItems(Base):
    """
    SQLAlchemy ORM model representing the 'order_items' table.
    """

    __tablename__ = 'order_items'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid7)
    order_id = Column('order_id', ForeignKey('orders.id'))
    product_id = Column('order_id', ForeignKey('products.id'))
    quantity = Column('quantity', Integer(), default=1)
    unity_price = Column('total_pice', Decimal(10, 2), default=0)

    # constructor
    def __init__(self, order_id, product_id, unity_price, quantity=1):
        self.order_id = order_id
        self.product_id = product_id
        self.unity_price = unity_price
        self.quantity = quantity
