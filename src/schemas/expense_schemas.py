from typing import Optional
from datetime import date

from pydantic import BaseModel, Field


class NewExpenseRequest(BaseModel):
    name: str = Field(..., min_length=5, max_length=100)
    description: Optional[str] = Field('', max_length=500)
    periodicity_in_months: int = Field(..., ge=1, le=12)
    last_payment_date: Optional[date] = None
    next_payment_date: Optional[date] = None
    estimated_next_payment_date: Optional[date] = None


class UpdateExpenseRequest(BaseModel):
    name: Optional[str] = Field(None, min_length=5, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    periodicity_in_months: Optional[int] = Field(None, ge=1, le=12)
    last_payment_date: Optional[date] = None
    next_payment_date: Optional[date] = None
    estimated_next_payment_date: Optional[date] = None
