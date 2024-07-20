from db.models import CartItem
from repositories.base import SQLAlchemyRepository


class CartItemSQLAlchemyRepository(SQLAlchemyRepository):
    model = CartItem
