# project.py
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel


class ProjectModel(BaseModel):

   
    __tablename__ = "projects"

   
    project_name = Column(String, nullable=False)
    budget = Column(Integer, nullable=False) 
    description = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    user_finance = relationship("UserFinanceModel", back_populates="hybrid_plans")


# 4. Bucket Allocation Plan
class BucketAllocationPlanModel(BaseModel):
    __tablename__ = "bucket_allocation_plans"

    short_term_percent = Column(Float, default=0.5)
    long_term_percent = Column(Float, default=0.3)
    leisure_percent = Column(Float, default=0.2)
    months = Column(Integer, nullable=False)
    user_finance_id = Column(Integer, ForeignKey('user_finances.id'))

    user_finance = relationship("UserFinanceModel", back_populates="bucket_plans")
