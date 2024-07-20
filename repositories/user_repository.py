from db.models import User
from repositories.base import SQLAlchemyRepository


class UserSQLAlchemyRepository(SQLAlchemyRepository):
    model = User
