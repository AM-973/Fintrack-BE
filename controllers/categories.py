from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.category import CategoryModel
from models.project import ProjectModel
from models.user import UserModel
from serializers.category import CategorySchema, CategoryCreateSchema
from typing import List
from database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()


@router.get("/projects/{project_id}/categories", response_model=List[CategorySchema])
def get_categories_for_project(project_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if project.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Error")
    return project.categories

@router.get("/categories/{category_id}", response_model=CategorySchema)
def get_single_category(category_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    if category.project.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Error")
    return category

@router.post("/projects/{project_id}/categories", response_model=CategorySchema)
def create_category(project_id: int, category: CategoryCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if project.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Error")
    
    new_category = CategoryModel(**category.dict(), project_id=project_id)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@router.put("/categories/{category_id}", response_model=CategorySchema)
def update_category(category_id: int, category: CategoryCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    if db_category.project.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Error")

    category_data = category.dict(exclude_unset=True)
    for key, value in category_data.items():
        setattr(db_category, key, value)

    db.commit()
    db.refresh(db_category)
    return db_category


@router.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    if db_category.project.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Error")

    db.delete(db_category)
    db.commit()
    return {"message": f"Category with ID {category_id} has been deleted."}