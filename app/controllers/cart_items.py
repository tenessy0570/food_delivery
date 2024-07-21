from typing import Annotated

from fastapi import Depends, APIRouter

from app.dependencies import get_cart_item_service
from schemas.cart_item import CartItemCreateOrUpdateSchema
from schemas.response_models.cart_item import CartItemSchema
from services.cart_item_service import CartItemService

cart_router = APIRouter(prefix="/cart")


@cart_router.post("")
async def add_shop_item_to_user_cart(
        cart_item_schema: CartItemCreateOrUpdateSchema,
        service: Annotated[CartItemService, Depends(get_cart_item_service)]
):
    id = await service.add_shop_item_to_user_cart(
        shop_item_id=cart_item_schema.shop_item_id,
        user_id=cart_item_schema.user_id,
        items_count=cart_item_schema.count_items
    )
    return {"ok": True, "cart_item_id": id}


@cart_router.get("")
async def get_user_cart_items(
        user_id: int,
        service: Annotated[CartItemService, Depends(get_cart_item_service)]
) -> list[CartItemSchema]:
    items = await service.get_all_cart_items(user_id)
    return items
