from src.config import app_settings
from .database_connection import DatabaseConnection
from .models import BaseModel


db_connection = DatabaseConnection(app_settings.DB_CONN)


def create_tables():
    # !DELETE PRINT
    print('\033[94m', 'Crear tablas en la DB', '\033[0m')
    BaseModel.metadata.create_all(bind=db_connection.engine)
