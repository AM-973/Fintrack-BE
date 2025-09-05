from sqlalchemy import Column, Integer, String, Text, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .base import BaseModel

class ProjectModel(BaseModel):
    __tablename__ = "projects"

    project_name = Column(String, nullable=False)
    budget = Column(Integer, nullable=False) 
    description = Column(Text)
    plan_type = Column(String, nullable=False)  
    extra_config = Column(JSON, nullable=True)

    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('UserModel', back_populates='projects')
    categories = relationship("CategoryModel", back_populates="project", cascade="all, delete-orphan")
