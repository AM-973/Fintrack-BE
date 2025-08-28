from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel


class ProjectModel(BaseModel):

   
    __tablename__ = "projects"

   
    name = Column(String, nullable=False)
    budget = Column(Integer, nullable=False) 
    description = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('UserModel', back_populates='projects')
    categories = relationship("CategoryModel", back_populates="project")