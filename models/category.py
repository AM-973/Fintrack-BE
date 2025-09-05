from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class CategoryModel(BaseModel):

    __tablename__ = "categories"
# dfghjjjjjjjjj
    name = Column(String, nullable=False)  
    description = Column(Text)  
    budget = Column(Integer, nullable=False)  

    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    project = relationship("ProjectModel", back_populates="categories")
    expenses = relationship("ExpenseModel", back_populates="category", cascade="all, delete-orphan")