from pydantic import BaseModel, Field
from typing import Optional, List
from .category import CategorySchema
from .user import UserResponseSchema
from typing import Optional, List, Dict, Any


class ProjectSchema(BaseModel):
  id: Optional[int] = Field(default=None) 
  project_name: str
  budget: int  
  description: Optional[str] = None
  plan_type: str   
  extra_config: Optional[Dict[str, Any]] = None  

  # Relationships
  categories: List[CategorySchema] = []
  user: UserResponseSchema

  class Config:
    from_attributes = True

class ProjectCreateSchema(BaseModel):
    project_name: str
    budget: int  
    description: Optional[str] = None
    plan_type: str   
    extra_config: Optional[Dict[str, Any]] = None  