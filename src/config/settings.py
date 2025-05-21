from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API
    PORT: int = 8000
    DEV: bool = True

    # Logs
    LOG_DIR: str = 'logs'
    DEBUG: bool = False

    # Database
    PATH_DATA: str = 'database/fake_db.json'
    DB_CONN: str

    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = 'HS256'
    JWT_EXPIRATION_TIME_IN_MINUTES: int = 60

    # Config inner class
    class Config:
        env_file = '.env'
