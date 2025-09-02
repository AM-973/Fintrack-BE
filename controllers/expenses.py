from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.category import CategoryModel
from models.project import ProjectModel
from models.user import UserModel
from serializers.expense import ExpenseSchema, ExpenseCreateSchema
from typing import List
from database import get_db
from dependencies.get_current_user import get_current_user
from models.expense import ExpenseModel

router = APIRouter()


@router.get("/projects/{project_id}/categories/{category_id}/expenses", response_model=List[ExpenseSchema])
def get_expenses_for_category(project_id: int, category_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):

    project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if project.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Error")
    
    category = db.query(CategoryModel).filter(
        CategoryModel.id == category_id,
        CategoryModel.project_id == project_id
    ).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    return category.expenses


@router.get("/projects/{project_id}/categories/{category_id}/expenses/{expense_id}", response_model=ExpenseSchema)
def get_single_expense(project_id: int, category_id: int, expense_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
   
    project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if project.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Error")
    
    category = db.query(CategoryModel).filter(
        CategoryModel.id == category_id,
        CategoryModel.project_id == project_id
    ).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    expense = db.query(ExpenseModel).filter(
        ExpenseModel.id == expense_id,
        ExpenseModel.category_id == category_id
    ).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    return expense


@router.post("/projects/{project_id}/categories/{category_id}/expenses", response_model=ExpenseSchema)
def create_expense(project_id: int, category_id: int, expense: ExpenseCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
 
    project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if project.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Error")
    
    category = db.query(CategoryModel).filter(
        CategoryModel.id == category_id,
        CategoryModel.project_id == project_id
    ).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    new_expense = ExpenseModel(**expense.dict(), category_id=category_id)
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


@router.put("/projects/{project_id}/categories/{category_id}/expenses/{expense_id}", response_model=ExpenseSchema)
def update_expense(project_id: int, category_id: int, expense_id: int, expense: ExpenseCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
   
    project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if project.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Error")
    
    category = db.query(CategoryModel).filter(
        CategoryModel.id == category_id,
        CategoryModel.project_id == project_id
    ).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    db_expense = db.query(ExpenseModel).filter(
        ExpenseModel.id == expense_id,
        ExpenseModel.category_id == category_id
    ).first()
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    expense_data = expense.dict(exclude_unset=True)
    for key, value in expense_data.items():
        setattr(db_expense, key, value)
    
    db.commit()
    db.refresh(db_expense)
    return db_expense


@router.delete("/projects/{project_id}/categories/{category_id}/expenses/{expense_id}")
def delete_expense(project_id: int, category_id: int, expense_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
  
    project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if project.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Error")
    
    category = db.query(CategoryModel).filter(
        CategoryModel.id == category_id,
        CategoryModel.project_id == project_id
    ).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    expense = db.query(ExpenseModel).filter(
        ExpenseModel.id == expense_id,
        ExpenseModel.category_id == category_id
    ).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(expense)
    db.commit()
    return {"message": f"Expense with ID {expense_id} has been deleted."}