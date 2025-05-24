from typing import List

import bcrypt
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from .base_model import BaseModel
from .expense_model import ExpenseModel
from src.enums.role_enum import RoleEnum as Role


ENCODING = 'utf-8'


class UserModel(BaseModel):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    role: Mapped[str] = mapped_column(String(32), server_default=Role.COMMON.value, nullable=False)
    encrypted_password: Mapped[str] = mapped_column(String(128), nullable=False)

    # Relationships
    expenses: Mapped[List[ExpenseModel]] = relationship(ExpenseModel)

    @property
    def password(self) -> str:
        return self.encrypted_password

    @password.setter
    def password(self, plain_password: str) -> None:
        hashed_password = bcrypt.hashpw(plain_password.encode(ENCODING), bcrypt.gensalt())
        self.encrypted_password = hashed_password.decode(ENCODING)

    def check_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode(ENCODING), self.password.encode(ENCODING))
