from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.category import CategoryModel
from models.user import UserModel
from serializers.expense import ExpenseSchema, ExpenseCreateSchema
from typing import List
from database import get_db
from dependencies.get_current_user import get_current_user
from models.expense import ExpenseModel


router = APIRouter()

@router.get("/categories/{category_id}/expenses", response_model=List[ExpenseSchema])
def get_expenses_for_category(category_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    if category.project.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Error")
    return category.expenses
    


@router.get("/categories/{category_id}/expenses/{expense_id}", response_model=ExpenseSchema)
def get_single_expense(category_id: int, expense_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    if category.project.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Error")
    expense = db.query(ExpenseModel).filter(ExpenseModel.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense


@router.post("/categories/{category_id}/expenses", response_model=ExpenseSchema)
def create_expense(category_id: int, expense: ExpenseCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    if category.project.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Error")
    new_expense = ExpenseModel(**expense.dict(), category_id=category_id)
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


@router.put("/expenses/{expense_id}", response_model=ExpenseSchema)
def update_expense(expense_id: int, expense: ExpenseCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_expense = db.query(ExpenseModel).filter(ExpenseModel.id == expense_id).first()
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    if db_expense.category.project.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Error")
    expense_data = expense.dict(exclude_unset=True)
    for key, value in expense_data.items():
        setattr(db_expense, key, value)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    expense = db.query(ExpenseModel).filter(ExpenseModel.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    if expense.category.project.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Error")
    db.delete(expense)
    db.commit()
    return {"message": f"Expense with ID {expense_id} has been deleted."}