from typing import List, Dict, Any

from src.helpers.file_helpers import read_json_file, write_json_file
from .base_repository import BaseRepository
from src.config import app_settings

# class PaymentRepository(BaseRepository):
class PaymentRepository():
    async def _read_all(self) -> List[Dict[str, Any]]:
        data = read_json_file(app_settings.PATH_DATA)
        return data['payments']

    async def _update_db(self, data: List[Dict[str, Any]]) -> None:
        db = read_json_file(app_settings.PATH_DATA)
        db['payments'] = data
        write_json_file(app_settings.PATH_DATA, db)

    async def _get_next_id(self) -> int:
        data = await self._read_all()
        if not data:
            return 1
        return max(expense['id'] for expense in data) + 1