from datetime import datetime, timedelta, timezone

import jwt

from src.config import app_settings
from src.exceptions.client_exceptions import Unauthorized


class JwtHandler:
    def __init__(self):
        self.secret_key: str = app_settings.JWT_SECRET_KEY
        self.algorithm: str = app_settings.JWT_ALGORITHM

        self.expires_delta = timedelta(minutes=app_settings.JWT_EXPIRATION_TIME_IN_MINUTES)

    def encode(self, data: dict) -> str:
        payload = data.copy()
        expire = datetime.now(timezone.utc) + self.expires_delta
        payload.update(exp=expire)
        return jwt.encode(payload, self.secret_key, self.algorithm)

    def decode(self, token: str) -> dict:
        try:
            payload: dict = jwt.decode(token, self.secret_key, self.algorithm)
            return payload
        except jwt.ExpiredSignatureError:
            raise Unauthorized('Token expirado')
        except jwt.InvalidSignatureError:
            raise Unauthorized('Firma del token inválida')
        except jwt.InvalidTokenError:
            raise Unauthorized('Token inválido')


jwt_handler = JwtHandler()
