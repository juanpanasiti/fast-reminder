from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware import Middleware

from .routes import api_router
from .config.logger import configure_logging
from .database import db_connection
from .middlewares.jwt_middleware import JwtMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Antes de levantar el servidor
    configure_logging()
    db_connection.connect()
    yield
    db_connection.disconnect()
    # Antes de cerrar el servidor

api_middlewares = [
    Middleware(JwtMiddleware),
]

api_server = FastAPI(
    description='Proyecto Fast-Reminder del curso de Python+FastAPI 2025',
    version='0.0.0',
    title='Fast-Reminder',
    lifespan=lifespan,
    middleware=api_middlewares,
)

api_server.include_router(api_router)
