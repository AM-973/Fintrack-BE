from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.project import ProjectModel
from models.user import UserModel
from serializers.project import ProjectSchema, ProjectCreateSchema
from typing import List
from database import get_db
from dependencies.get_current_user import get_current_user
from services.calculations import (
    calculate_savings_plan,
    calculate_investment_plan,
    calculate_hybrid_plan,
)

router = APIRouter()

# it's a variable that contains keys refer to each calculation 
# in the calculation file in the services folder
PLAN_CALCULATORS = {
    "savings": calculate_savings_plan,
    "investment": calculate_investment_plan,
    "hybrid": calculate_hybrid_plan,
}


@router.get('/projects', response_model=List[ProjectSchema])
def get_projects(db: Session = Depends(get_db)):
  projects = db.query(ProjectModel).all()
  return projects

@router.get('/projects/{project_id}', response_model=ProjectSchema)
def get_single_project(project_id: int, db: Session = Depends(get_db)):
  project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
  if project:
    return project
  else:
    raise HTTPException(status_code=404, detail="Project not found")

@router.post('/projects', response_model=ProjectSchema)
def create_project(project: ProjectCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
  new_project =  ProjectModel(**project.dict(), user_id=current_user.id)
  db.add(new_project)
  db.commit()
  db.refresh(new_project)
  calc_func = PLAN_CALCULATORS.get(new_project.plan_type)
  if calc_func:
        calculation = calc_func(new_project.budget, new_project.extra_config)
        # Attach as a dynamic attribute for serialization
        setattr(new_project, "calculation", calculation)
  else:
        setattr(new_project, "calculation", {})

    # Ensure relationships are loaded
  _ = new_project.user
  _ = new_project.categories

  return new_project



@router.put("/projects/{project_id}", response_model=ProjectSchema)
def update_project(project_id: int, project: ProjectCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
  db_project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
  
  if not db_project:
    raise HTTPException(status_code=404, detail="Project not found")

  if db_project.user_id != current_user.id:
    raise HTTPException(status_code=403, detail="Operation forbidden")

  project_data = project.dict(exclude_unset=True)
  for key, value in project_data.items():
        setattr(db_project, key, value)

  db.commit()
  db.refresh(db_project)
  return db_project


@router.delete("/projects/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not db_project:
     
      raise HTTPException(status_code=404, detail="Project not found")

    if db_project.user_id != current_user.id:
      raise HTTPException(status_code=403, detail="Operation forbidden")

    db.delete(db_project)  
    db.commit() 
    return {"message": f"Project with ID {project_id} has been deleted"}