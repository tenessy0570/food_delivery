from repositories.base import AbstractRepository
from schemas.cart_item import CartItemCreateOrUpdateSchema
from schemas.response_models.shop_item import ShopItemSchema
from schemas.response_models.user import UserSchema
from services.base import AbstractService


class CartItemService(AbstractService):
    def __init__(
            self,
            cart_item_repository: AbstractRepository,
            shop_item_repository: AbstractRepository,
            user_repository: AbstractRepository
    ):
        self.cart_item_repository = cart_item_repository
        self.shop_item_repository = shop_item_repository
        self.user_repository = user_repository

    async def add_shop_item_to_user_cart(self, shop_item_id: int, user_id: int, items_count: int = 1) -> int:
        shop_item: ShopItemSchema = await self.shop_item_repository.get_by_id(shop_item_id)

        if not shop_item:
            raise ValueError("Shop item not found")

        user: UserSchema = await self.user_repository.get_by_id(user_id)

        if not user:
            raise ValueError("User not found")

        creation_schema = CartItemCreateOrUpdateSchema(
            user_id=user_id,
            shop_item_id=shop_item_id,
            count_items=items_count,
        )
        created_item = await self.cart_item_repository.create_one(
            shop_items_count_available=shop_item.count_available,
            **creation_schema.dict()
        )
        return created_item.id
