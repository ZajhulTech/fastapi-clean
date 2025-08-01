from fastapi import FastAPI
from app.webapi.routers import user_router, customer_router


app = FastAPI(    
    title="My FastAPI App",
    version="1.0.0"
)

app.include_router(user_router.router)
app.include_router(customer_router.router)