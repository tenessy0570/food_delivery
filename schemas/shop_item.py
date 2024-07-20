from decimal import Decimal

from pydantic import BaseModel, field_validator


class ShopItemSchema(BaseModel):
    name: str
    tags: str | None = None
    type: str | None = None
    price_dollars: float | Decimal
    count_available: int
    is_active: bool = False

    @field_validator("count_available")
    def count_available_must_be_positive(cls, value):
        if value < 0:
            raise ValueError("count_available argument must be positive")

        return value
