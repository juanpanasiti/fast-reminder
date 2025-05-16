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

    # Config inner class
    class Config:
        env_file = '.env'
