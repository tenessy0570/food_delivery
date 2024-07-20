from db.models import User
from repositories.base import SQLAlchemyRepository


class CartItemSQLAlchemyRepository(SQLAlchemyRepository):
    model = User
