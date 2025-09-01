from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from enum import Enum  
from .category import CategorySchema
from .user import UserResponseSchema


class PlanType(str, Enum):  
    savings = "savings"
    investment = "investment"
    hybrid = "hybrid"

class ProjectSchema(BaseModel):
    id: Optional[int] = Field(default=None) 
    project_name: str
    budget: int  
    description: Optional[str] = None
    plan_type: PlanType  
    extra_config: Dict[str, Any] = Field(default_factory=dict) 
    calculation: Dict[str, Any] = Field(default_factory=dict)  

    # Relationships
    categories: List[CategorySchema] = []
    user: UserResponseSchema

    class Config:
        orm_mode = True 

class ProjectCreateSchema(BaseModel):
    project_name: str
    budget: int  
    description: Optional[str] = None
    plan_type: PlanType  
    extra_config: Dict[str, Any] = Field(default_factory=dict) 

