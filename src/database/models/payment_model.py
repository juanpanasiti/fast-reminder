from datetime import date

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, Integer, Float, ForeignKey
from .base_model import BaseModel


class PaymentModel(BaseModel):
    __tablename__ = 'payments'

    amount: Mapped[float] = mapped_column(Float(precision=2), default=0.0)
    due_date: Mapped[date] = mapped_column(Date())
    paid_date: Mapped[date] = mapped_column(Date())
    status: Mapped[str] = mapped_column(String(20), default='pending')
    notes: Mapped[str] = mapped_column(String(2000))

    # Foreign Key
    expense_id: Mapped[int] = mapped_column(Integer(), ForeignKey('expenses.id'))
