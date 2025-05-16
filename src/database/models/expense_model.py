from datetime import date

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, Integer
from .base_model import BaseModel


class ExpenseModel(BaseModel):
    __tablename__ = 'expenses'

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), nullable=False)
    periodicity_in_months: Mapped[int] = mapped_column(Integer(), nullable=False)
    last_payment_date: Mapped[date] = mapped_column(Date(), nullable=False)
    next_payment_date: Mapped[date] = mapped_column(Date(), nullable=False)
    estimated_next_payment_date: Mapped[date] = mapped_column(Date(), nullable=False)
