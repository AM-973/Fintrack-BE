from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from .base import BaseModel 

class ExpenseModel(BaseModel):
   
    __tablename__ = "expenses"
    
    name = Column(String(255), nullable=False)
    amount = Column(Integer, nullable=False)  # Amount in cents to avoid floating point issues
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    
    # Relationships
    category = relationship("CategoryModel", back_populates="expenses")