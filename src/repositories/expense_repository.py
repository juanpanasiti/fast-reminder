from typing import Dict, List, Any

from .base_repository import BaseRepository
from src.helpers.file_helpers import read_json_file, write_json_file
from src.config import app_settings
from src.database.models import ExpenseModel


class ExpenseRepository(BaseRepository):
    def __init__(self):
        super().__init__(ExpenseModel)

    # async def _read_all(self) -> List[Dict[str, Any]]:
    #     data = read_json_file(app_settings.PATH_DATA)
    #     return data.get('expenses', [])

    # async def _update_db(self, db: List[Dict[str, Any]]) -> None:
    #     current = read_json_file(app_settings.PATH_DATA)
    #     current['expenses'] = db
    #     write_json_file(app_settings.PATH_DATA, current)

    # async def _get_next_id(self) -> int:
    #     data = await self._read_all()
    #     if not data:
    #         return 1
    #     return max(expense['id'] for expense in data) + 1
