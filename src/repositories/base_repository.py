from abc import ABC, abstractmethod
from typing import Dict, List, Any
from datetime import datetime
from typing import Type

from src.database import db_connection
from src.database.models import BaseModel


class BaseRepository(ABC):
    def __init__(self, Model: Type[BaseModel]):
        self.db = db_connection.session
        self.Model = Model

    async def count(self, criteria: dict = {}) -> int:
        # data = await self._read_all()
        # if criteria:
        #     data = [item for item in data if all(item.get(key) == value for key, value in criteria.items())]
        # return len(data)
        count = self.db.query(self.Model).filter_by(**criteria).count()
        return count

    async def get_many(self, page: int, limit: int, criteria: dict = {}) -> list[dict]:
        # data = await self._read_all()
        # if criteria:
        #     data = [item for item in data if all(item.get(key) == value for key, value in criteria.items())]
        # start = (page - 1) * limit
        # end = start + limit
        # return data[start:end]
        offset = (page - 1) * limit
        records = self.db.query(self.Model).order_by('id').filter_by(**criteria).limit(limit).offset(offset).all()
        return [record.to_dict() for record in records]

    async def create(self, data: dict) -> dict:
        # data['id'] = await self._get_next_id()
        # data['created_at'] = datetime.now().isoformat()
        # data['updated_at'] = datetime.now().isoformat()
        # db = await self._read_all()
        # db.append(data)
        # await self._update_db(db)
        # return data
        new_record = self.Model(**data)
        self.db.add(new_record)
        self.db.commit()
        self.db.refresh(new_record)
        return new_record.to_dict()

    async def get_one_by_criteria(self, criteria: dict) -> dict | None:
        # data = await self._read_all()
        # for item in data:
        #     if all(item.get(key) == value for key, value in criteria.items()):
        #         return item
        # return None
        record = self.db.query(self.Model).filter_by(**criteria).first()
        if record is None:
            return None
        return record.to_dict()

    async def update_one(self, criteria: dict, data: dict) -> dict | None:
        # db = await self._read_all()
        # for index, item in enumerate(db):
        #     if all(item.get(key) == value for key, value in criteria.items()):
        #         item.update(data)
        #         item['updated_at'] = datetime.now().isoformat()
        #         await self._update_db(db)
        #         return item
        # return None
        record = self.db.query(self.Model).filter_by(**criteria).first()
        if record is None:
            return None
        for field in data.keys():
            setattr(record, field, data[field])
        self.db.commit()
        self.db.refresh(record)
        return record.to_dict()

    async def delete_one(self, criteria: dict) -> bool:
        # data = await self._read_all()
        # for index, item in enumerate(data):
        #     if all(item.get(key) == value for key, value in criteria.items()):
        #         del data[index]
        #         await self._update_db(data)
        #         return True
        # return False
        record = self.db.query(self.Model).filter_by(**criteria).first()
        if record is None:
            return False
        self.db.delete(record)
        self.db.commit()
        return True

    # @abstractmethod
    # async def _read_all(self) -> List[Dict[str, Any]]:
    #     pass

    # @abstractmethod
    # async def _update_db(self, db: List[Dict[str, Any]]) -> None:
    #     pass

    # @abstractmethod
    # async def _get_next_id(self) -> int:
    #     pass

    # Movido al modelo
    # def _to_dict(self, record: BaseModel) -> dict:
    #     return {
    #         column.name: getattr(record, column.name)
    #         for column in self.Model.__table__.columns
    #     }
