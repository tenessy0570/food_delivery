from pydantic import BaseModel


class CartItemSchema(BaseModel):
    id: int
    user_id: int
    shop_item_id: int
    count_items: int
