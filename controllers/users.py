from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import UserModel
from serializers.user import UserSchema, UserLoginSchema, UserTokenSchema, UserResponseSchema
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