# Import ALL models to register in the metadata

# Do not use in the application only in Alembic

from app.users.models import User  # noqa
from app.orders.models import Order  # noqa
from app.order_Items.models import OrderItem  # noqa
from app.products.models import Product  # noqa
