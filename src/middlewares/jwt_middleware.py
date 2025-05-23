import logging
import time

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint as Callback

from src.handlers.jwt_handler import jwt_handler
from src.config import app_settings


logger = logging.getLogger(__name__)


class JwtMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: Callback) -> Response:
        # 1. Obtener el token que viene en el Header de la request
        token = request.headers.get('Authorization')

        # 2. Ejecutar la función del endpoint
        response = await call_next(request)  # <-- Aca se llama al endpoint

        # 3. Tabajamos con el token
        if token is None or not token.startswith('Bearer'):
            return response

        # 4. Renovar el token (si aplica)
        try:
            # Token original del request header -> "Bearer dsfgdfgdf.dfgdfg.dfgdfgdf"
            payload = jwt_handler.decode(token.split(' ')[1])

            expired_timestamp = payload['exp']
            current_timestamp = int(time.time())

            time_left: float = (expired_timestamp - current_timestamp) / 60
            if time_left <= (app_settings.JWT_EXPIRATION_TIME_IN_MINUTES * 0.5):
                del payload['exp']
                new_token = jwt_handler.encode(payload)
                response.headers['renewed-token'] = new_token
        except Exception as ex:
            logger.error(str(ex))
            # raise ex

        # 5. Retornamos la respuesta del endpoint
        return response
