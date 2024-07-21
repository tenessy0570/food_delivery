import datetime
from decimal import Decimal

from pydantic import BaseModel


class ShopItemSchema(BaseModel):
    id: int
    name: str
    tags: str | None
    type: str | None
    price_dollars: float | Decimal
    count_available: int
    is_active: bool

    created_at: datetime.datetime
    updated_at: datetime.datetime | None
