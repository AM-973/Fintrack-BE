from sqlalchemy import Column, Integer, Float, String, ForeignKey, Text
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

class UserFinanceModel(BaseModel):
    __tablename__ = "user_finances"

    salary = Column(Float, nullable=False)
    expenses = Column(String, nullable=False)  # store as JSON string

    # Relationships to plans
    emergency_funds = relationship("EmergencyFundPlanModel", back_populates="user_finance")
    investment_plans = relationship("InvestmentGrowthPlanModel", back_populates="user_finance")
    hybrid_plans = relationship("DebtSavingsHybridPlanModel", back_populates="user_finance")
    bucket_plans = relationship("BucketAllocationPlanModel", back_populates="user_finance")


# 1. Emergency Fund Plan
class EmergencyFundPlanModel(BaseModel):
    __tablename__ = "emergency_fund_plans"

    months_to_cover = Column(Integer, nullable=False)
    months_to_save = Column(Integer, nullable=False)
    user_finance_id = Column(Integer, ForeignKey('user_finances.id'))

    user_finance = relationship("UserFinanceModel", back_populates="emergency_funds")


# 2. Investment Growth Plan
class InvestmentGrowthPlanModel(BaseModel):
    __tablename__ = "investment_growth_plans"

    saving_rate = Column(Float, nullable=False)  # % of disposable income
    months = Column(Integer, nullable=False)
    monthly_return = Column(Float, default=0.01)  # optional compound interest
    user_finance_id = Column(Integer, ForeignKey('user_finances.id'))

    user_finance = relationship("UserFinanceModel", back_populates="investment_plans")


# 3. Debt + Savings Hybrid Plan
class DebtSavingsHybridPlanModel(BaseModel):
    __tablename__ = "debt_savings_hybrid_plans"

    saving_rate = Column(Float, nullable=False)  # % of disposable income
    debt_rate = Column(Float, nullable=False)    # % of disposable income
    months = Column(Integer, nullable=False)
    user_finance_id = Column(Integer, ForeignKey('user_finances.id'))

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