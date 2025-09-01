from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.project import ProjectModel
from models.user import UserModel
from serializers.project import ProjectSchema, ProjectCreateSchema
from typing import List
from database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()

# the plans functions for calculating user's financial

def calculate_savings_plan(budget, extra_config):
    saving_rate = extra_config.get("saving_rate", 0.2)
    months = extra_config.get("months", 6)
    monthly_saving = budget * saving_rate
    total_saved = monthly_saving * months
    return {"monthly_saving": monthly_saving, "total_saved": total_saved, "months": months}

def calculate_investment_plan(budget, extra_config):
    monthly_contribution = extra_config.get("monthly_contribution", budget * 0.2)
    months = extra_config.get("months", 12)
    monthly_return = extra_config.get("monthly_return", 0.0)
    
    total = 0
    for _ in range(months):
        total = (total + monthly_contribution) * (1 + monthly_return)
    
    return {"monthly_contribution": monthly_contribution, "total_value": round(total, 2), "months": months}

def calculate_hybrid_plan(budget, extra_config):
    saving_rate = extra_config.get("saving_rate", 0.2)
    debt_rate = extra_config.get("debt_rate", 0.1)
    months = extra_config.get("months", 12)
    
    monthly_saving = budget * saving_rate
    monthly_debt = budget * debt_rate
    return {
        "monthly_saving": monthly_saving,
        "monthly_debt": monthly_debt,
        "total_saving": monthly_saving * months,
        "total_debt": monthly_debt * months,
        "months": months
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