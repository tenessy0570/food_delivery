from db.models import ShopItem
from repositories.base import SQLAlchemyRepository


class CartItemSQLAlchemyRepository(SQLAlchemyRepository):
    model = ShopItem
