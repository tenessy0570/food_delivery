from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError

import config
from app.dependencies import get_cart_item_service
from schemas.cart_item import CartItemCreateOrUpdateSchema
from services.cart_item_service import CartItemService

router = APIRouter()


@router.post("/cart_item")
async def add_shop_item_to_user_cart(
        cart_item_schema: CartItemCreateOrUpdateSchema,
        service: Annotated[CartItemService, Depends(get_cart_item_service)]
):
    try:
        id = await service.add_shop_item_to_user_cart(
            shop_item_id=cart_item_schema.shop_item_id,
            user_id=cart_item_schema.user_id,
            items_count=cart_item_schema.count_items
        )
    except SQLAlchemyError as exc:
        config.logger.error(f"An error while adding shop item to user cart: {repr(exc)}")
        raise HTTPException(status_code=500, detail="Database error")
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    return {"ok": True, "cart_item_id": id}
