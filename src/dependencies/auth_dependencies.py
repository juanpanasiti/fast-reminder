from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError

from src.schemas.auth_schemas import DecodedJwt
from src.handlers.jwt_handler import jwt_handler
from src.exceptions.client_exceptions import Unauthorized


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/login')


async def get_token(authorization=Depends(oauth2_scheme)) -> DecodedJwt:
    try:
        payload = jwt_handler.decode(authorization)
        return DecodedJwt(**payload)
    except InvalidTokenError:
        raise Unauthorized('Token inválido')
