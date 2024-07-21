from fastapi import FastAPI
from app.controllers.cart_items import cart_router
from app.middlewares import catch_exceptions_middleware

app = FastAPI()

app.middleware('http')(catch_exceptions_middleware)
app.include_router(cart_router)
