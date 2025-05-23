from datetime import date
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date, Integer, Boolean, ForeignKey
from .base_model import BaseModel
from .payment_model import PaymentModel


class ExpenseModel(BaseModel):
    __tablename__ = 'expenses'

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), nullable=False)
    periodicity_in_months: Mapped[int] = mapped_column(Integer(), nullable=False)
    last_payment_date: Mapped[date] = mapped_column(Date(), nullable=False)
    next_payment_date: Mapped[date] = mapped_column(Date(), nullable=False)
    estimated_next_payment_date: Mapped[date] = mapped_column(Date(), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), server_default="True", default=True, nullable=False)

    # Foreign Key
    user_id: Mapped[int] = mapped_column(Integer(), ForeignKey('users.id'))

    # Relationships
    payments: Mapped[List[PaymentModel]] = relationship(PaymentModel)

    def to_dict(self) -> dict:
        response = super().to_dict()
        response['payments'] = [payment.to_dict() for payment in self.payments]
        return response
