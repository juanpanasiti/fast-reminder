from typing import Optional
from datetime import date

from pydantic import BaseModel, Field


class NewPaymentRequest(BaseModel):
    expense_id: int = Field(..., ge=1)
    amount: float = Field(..., gt=0)
    due_date: Optional[date] = None
    paid_date: Optional[date] = None
    notes: Optional[str] = Field('', max_length=500)


class UpdatePaymentRequest(BaseModel):
    expense_id: Optional[int] = Field(None, ge=1)
    amount: Optional[float] = Field(None, gt=0)
    due_date: Optional[date] = None
    paid_date: Optional[date] = None
    notes: Optional[str] = Field(None, max_length=500)
