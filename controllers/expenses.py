from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.project import ProjectModel
from models.user import UserModel
from serializers.expense import ExpenseSchema, ExpenseCreateSchema
from typing import List
from database import get_db
from dependencies.get_current_user import get_current_user
from models.expense import ExpenseModel


router = APIRouter()

@router.get("/projects/{project_id}/expenses", response_model=List[ExpenseSchema])
def get_expenses_for_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project.expenses


@router.get("/expenses/{expense_id}", response_model=ExpenseSchema)
def get_single_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(ExpenseModel).filter(ExpenseModel.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense


@router.post("/projects/{project_id}/expenses", response_model=ExpenseSchema)
def create_expense(project_id: int, expense: ExpenseCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project.expenses


@router.put("/expenses/{expense_id}", response_model=ExpenseSchema)
def update_expense(expense_id: int, expense: ExpenseCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    expense = db.query(ExpenseModel).filter(ExpenseModel.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    expense = db.query(ExpenseModel).filter(ExpenseModel.id == expense_id).first()