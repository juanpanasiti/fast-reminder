from .base_repository import BaseRepository
from src.database.models import UserModel


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserModel)

    async def check_password(self, user_id: int, password: str) -> bool | None:
        user: UserModel = await self._get_one({'id': user_id})
        if user is None:
            return None

        return user.check_password(password)
