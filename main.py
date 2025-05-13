import uvicorn

from src.config import app_settings


if __name__ == '__main__':
    uvicorn.run('src.app:api_server', host='0.0.0.0', port=app_settings.PORT, reload=app_settings.DEV)
