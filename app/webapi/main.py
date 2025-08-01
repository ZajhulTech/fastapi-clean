from fastapi import FastAPI
from app.webapi.routers import user_router

app = FastAPI()
app.include_router(user_router.router)
