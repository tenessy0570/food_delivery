from sqlalchemy import select

from db.connection import async_db_session
from db.models import CartItem
from repositories.base import SQLAlchemyRepository


class CartItemSQLAlchemyRepository(SQLAlchemyRepository):
    model = CartItem

    async def create_one(self, shop_items_count_available: int, **kwargs) -> "SQLAlchemyRepository.model":
        async with async_db_session as session:
            stmt = select(self.model).where(
                (self.model.user_id == int(kwargs.get("user_id")))
                & (self.model.shop_item_id == int(kwargs.get("shop_item_id")))
            )
            result = await session.execute(stmt)
            result = result.scalars().first()

            if not result:
                if int(kwargs.get("count_items")) > shop_items_count_available:
                    raise ValueError(f"Can't add more items to cart, only {shop_items_count_available} available")

                return await super().create_one(**kwargs)

            result.count_items += int(kwargs.get("count_items"))

            if result.count_items > shop_items_count_available:
                raise ValueError(f"Can't add more items to cart, only {shop_items_count_available} available")

            await session.flush([result])
            await session.commit()
            await session.refresh(result)

            return result
