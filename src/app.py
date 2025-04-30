from fastapi import FastAPI

from .routes import api_router


api_server = FastAPI(
    description='Proyecto Fast-Reminder del curso de Python+FastAPI 2025',
    version='0.0.0',
    title='Fast-Reminder'
)

api_server.include_router(api_router)
