from pydantic import BaseModel, Field
from typing import Optional

class ExpenseSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str
    amount: int  # Amount in cents

    class Config:
        from_attributes = True

class ExpenseCreateSchema(BaseModel):
    name: str
    amount: int  # Amount in cents
