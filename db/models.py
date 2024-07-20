import datetime

from sqlalchemy import ForeignKey, Float, Integer, Boolean, DateTime, func
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from db.connection import engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, server_default="0")
    cart_items: Mapped[list["CartItem"]] = relationship(
        back_populates="user", cascade="all"
    )

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=False), server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=False), onupdate=func.now())


class ShopItem(Base):
    __tablename__ = "shop_items"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    tags: Mapped[str] = mapped_column(String(255), nullable=True)
    type: Mapped[str] = mapped_column(String(255), nullable=True)
    price_dollars: Mapped[float] = mapped_column(Float, nullable=False)
    count_available: Mapped[int] = mapped_column(Integer, default=0, server_default="0")
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, server_default="0")

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=False), server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=False), onupdate=func.now())


class CartItem(Base):
    __tablename__ = "cart_items"
    id: Mapped[int] = mapped_column(primary_key=True)
    count_items: Mapped[int] = mapped_column(Integer, default=1, server_default="1")
    user: Mapped["User"] = relationship(back_populates="cart_items")
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    shop_item_id: Mapped[int] = mapped_column(ForeignKey(ShopItem.id))


if __name__ == '__main__':
    Base.metadata.create_all(engine)
