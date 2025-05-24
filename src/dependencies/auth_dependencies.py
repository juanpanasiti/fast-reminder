from typing import List
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError

from src.schemas.auth_schemas import DecodedJwt
from src.handlers.jwt_handler import jwt_handler
from src.exceptions.client_exceptions import Unauthorized, Forbidden
from src.enums.role_enum import RoleEnum as Role

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/login')


def has_permissions(allowed_roles: List[Role] = []):
    async def get_token(authorization=Depends(oauth2_scheme)) -> DecodedJwt:
        try:
            payload = jwt_handler.decode(authorization)
            response = DecodedJwt(**payload)
            if len(allowed_roles) > 0 and response.role not in [role.value for role in allowed_roles]:
                raise Forbidden('El usuario no tiene acceso a este recurso')
            return response
        except InvalidTokenError:
            raise Unauthorized('Token inválido')

    return get_token
