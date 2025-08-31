from pydantic import BaseModel, Field
from typing import Optional, List
from .category import CategorySchema
from .user import UserResponseSchema

class ProjectSchema(BaseModel):
  id: Optional[int] = Field(default=None) # This makes sure you don't have to explicitly add an id when sending json data
  project_name: str
  budget: int  # Budget in cents
  description: Optional[str] = None

  # Relationships
  categories: List[CategorySchema] = []
  user: UserResponseSchema

  class Config:
    from_attributes = True

class ProjectCreateSchema(BaseModel):
    project_name: str
    budget: int  # Budget in cents
    description: Optional[str] = None