from enum import Enum


class RoleEnum(str, Enum):
    SUPERADMIN = 'superadmin'
    ADMIN = 'admin'
    COMMON = 'common'


ALL_ROLES = [RoleEnum.COMMON, RoleEnum.ADMIN, RoleEnum.SUPERADMIN]
ADMIN_ROLES = [RoleEnum.ADMIN, RoleEnum.SUPERADMIN]
