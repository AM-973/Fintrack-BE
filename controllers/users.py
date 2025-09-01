from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import UserModel
from serializers.user import UserSchema, UserLoginSchema, UserTokenSchema, UserResponseSchema
from dependencies.get_current_user import get_current_user, require_admin, get_current_active_user
from database import get_db

router = APIRouter()

@router.post("/register", response_model=UserResponseSchema)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    
    # Check if email already exists
    existing_user_email = db.query(UserModel).filter(UserModel.email == user.email).first()
    if existing_user_email:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    # Check if username already exists
    existing_user_username = db.query(UserModel).filter(UserModel.username == user.username).first()
    if existing_user_username:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = UserModel(username=user.username, email=user.email)
    
    new_user.set_password(user.password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login", response_model=UserTokenSchema)
def login(user: UserLoginSchema, db: Session = Depends(get_db)):

    
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()

    
    if not db_user or not db_user.verify_password(user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    token = db_user.generate_token()

    return {"token": token, "message": "Login successful"}

@router.get("/profile")
def get_user_profile(current_user: UserModel = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "is_admin": current_user.is_admin
    }

"""


Below are Admin only Routes



"""

@router.get("/admin/users")
def list_all_users(
    current_admin: UserModel = Depends(require_admin),
    db: Session = Depends(get_db)
):
    users = db.query(UserModel).all()
    return [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "is_admin": user.is_admin
        }
        for user in users
    ]

@router.delete("/admin/users/{user_id}")
def delete_user(
    user_id: int,
    current_admin: UserModel = Depends(require_admin),
    db: Session = Depends(get_db)
):
    user_to_delete = db.query(UserModel).filter(UserModel.id == user_id).first()
    
    if not user_to_delete:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Prevent admin from deleting themselves
    if user_to_delete.id == current_admin.id:
        raise HTTPException(status_code=400, detail="Cannot delete your own account")
    
    db.delete(user_to_delete)
    db.commit()
    
    return {"message": f"User {user_to_delete.username} deleted successfully"}

@router.post("/admin/users/{user_id}/make-admin")
def make_user_admin(
    user_id: int,
    current_admin: UserModel = Depends(require_admin),
    db: Session = Depends(get_db)
):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.is_admin = True
    db.commit()
    db.refresh(user)
    
    return {
        "message": f"User {user.username} is now an admin",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "is_admin": user.is_admin
        }
    }