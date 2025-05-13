from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API
    PORT: int = 8000
    DEV: bool = True

    # Logs
    LOG_DIR: str = 'logs'
    DEBUG: bool = False

    # Config inner class
    class Config:
        env_file = '.env'
