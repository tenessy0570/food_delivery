from fastapi import FastAPI

from app.controllers import router

app = FastAPI()
app.include_router(router)

