from abc import ABC, abstractmethod
from typing import Dict, List, Any
from datetime import datetime

class BaseRepository(ABC):
    async def count(self, criteria: dict = {}) -> int:
        data = await self._read_all()
        if criteria:
            data = [item for item in data if all(item.get(key) == value for key, value in criteria.items())]
        return len(data)

    async def get_many(self, page: int, limit: int, criteria: dict = {}) -> list[dict]:
        data = await self._read_all()
        if criteria:
            data = [item for item in data if all(item.get(key) == value for key, value in criteria.items())]
        start = (page - 1) * limit
        end = start + limit
        return data[start:end]

    async def create(self, data: dict) -> dict:
        data['id'] = await self._get_next_id()
        data['created_at'] = datetime.now().isoformat()
        data['updated_at'] = datetime.now().isoformat()
        db = await self._read_all()
        db.append(data)
        await self._update_db(db)
        return data

    async def get_one_by_criteria(self, criteria: dict) -> dict | None:
        data = await self._read_all()
        for item in data:
            if all(item.get(key) == value for key, value in criteria.items()):
                return item
        return None

    async def update_one(self, criteria: dict, data: dict) -> dict | None:
        db = await self._read_all()
        for index, item in enumerate(db):
            if all(item.get(key) == value for key, value in criteria.items()):
                item.update(data)
                item['updated_at'] = datetime.now().isoformat()
                await self._update_db(db)
                return item
        return None

    async def delete_one(self, criteria: dict) -> bool:
        data = await self._read_all()
        for index, item in enumerate(data):
            if all(item.get(key) == value for key, value in criteria.items()):
                del data[index]
                await self._update_db(data)
                return True
        return False

    @abstractmethod
    async def _read_all(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    async def _update_db(self, db: List[Dict[str, Any]]) -> None:
        pass

    @abstractmethod
    async def _get_next_id(self) -> int:
        pass
