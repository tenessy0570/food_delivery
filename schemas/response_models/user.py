import datetime

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    login: str
    email: str
    phone_number: str
    is_active: bool

    created_at: datetime.datetime
    updated_at: datetime.datetime | None
