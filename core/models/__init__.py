# Так указываются объекты для экспорта
__all__ = (
    "Base",
    "DatabaseHelper",
    "db_helper",
    "Product"
)

from .base import Base
from .db_helper import DatabaseHelper, db_helper
from .product import Product
