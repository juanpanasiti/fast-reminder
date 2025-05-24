from typing import Annotated

from fastapi import APIRouter, Path, Query, Depends

from src.dependencies.auth_dependencies import has_permissions
from src.schemas.user_schemas import UserPaginatedResponse
from src.schemas.auth_schemas import DecodedJwt
from src.enums.role_enum import ADMIN_ROLES
from .dependencies import user_controller


router = APIRouter(prefix='/users')


@router.get('')
async def get_paginated(
    page: Annotated[int, Query(ge=1)] = 1,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
    token: DecodedJwt = Depends(has_permissions(ADMIN_ROLES))
) -> UserPaginatedResponse:
    return await user_controller.get_paginated(page, limit)
