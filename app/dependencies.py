from repositories.cart_item_repository import CartItemSQLAlchemyRepository
from repositories.shop_item_repository import ShopItemSQLAlchemyRepository
from repositories.user_repository import UserSQLAlchemyRepository
from services.cart_item_service import CartItemService


def get_cart_item_service():
    return CartItemService(
        cart_item_repository=CartItemSQLAlchemyRepository(),
        shop_item_repository=ShopItemSQLAlchemyRepository(),
        user_repository=UserSQLAlchemyRepository()
    )
