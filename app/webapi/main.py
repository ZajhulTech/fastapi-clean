from fastapi import FastAPI
from app.infra.api.exception_handlers import http_exception_handler, unhandled_exception_handler
from fastapi.exceptions import HTTPException
from app.webapi.routers import user_router, customer_router


app = FastAPI(    
    title="My FastAPI App",
    version="1.0.0"
)

# Registrar handlers globales
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

app.include_router(user_router.router)
app.include_router(customer_router.router)