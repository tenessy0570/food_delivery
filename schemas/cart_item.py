from pydantic import BaseModel, field_validator


class CartItemSchema(BaseModel):
    user_id: int
    shop_item_id: int
    count_items: int

    @field_validator("count_items")
    def count_must_be_greater_than_zero(cls, value):
        if value < 1:
            raise ValueError("count_items argument must be greater than 0")

        return value
