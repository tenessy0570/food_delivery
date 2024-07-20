import asyncio

from db.models import CartItem
from repositories.base import SQLAlchemyRepository


class CartItemSQLAlchemyRepository(SQLAlchemyRepository):
    model = CartItem


async def main():
    repo = CartItemSQLAlchemyRepository()
    # obj = await repo.get_by_id(2)
    # print(vars(obj))
    # await repo.delete_by_id(id=1)
    a = await repo.fetch_all()
    for i in a:
        print(vars(i))

    # print(await repo.create_one(
    #     creation_data=CartItemSchema(
    #         user_id=1,
    #         shop_item_id=12,
    #         count_items=2
    #     )
    # ))
    #
    # print(await repo.update_by_id(
    #     id=2,
    #     **CartItemSchema(
    #         user_id=222,
    #         shop_item_id=222,
    #         count_items=222
    #     ).dict()
    # ))

if __name__ == '__main__':
    asyncio.run(main())