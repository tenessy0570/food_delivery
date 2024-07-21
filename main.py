from fastapi import FastAPI

from app.controllers.cart_items import cart_router

app = FastAPI()
app.include_router(cart_router)

