from db.models import ShopItem
from repositories.base import SQLAlchemyRepository


class ShopItemSQLAlchemyRepository(SQLAlchemyRepository):
    model = ShopItem
