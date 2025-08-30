from pydantic import BaseModel, Field
from typing import Optional

class CategorySchema(BaseModel):
  id: Optional[int] = Field(default=None)
  name: str
  description: Optional[str] = None
  budget: int  # Budget in cents

  class Config:
    orm_mode = True

class CategoryCreateSchema(BaseModel):
    name: str
    description: Optional[str] = None
    budget: int  # Budget in cents

class CategoryUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    budget: Optional[int] = None