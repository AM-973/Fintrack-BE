from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from models.user import UserModel
from database import get_db
import jwt
from config.environment import secret

# We're using the HTTP Bearer scheme for the Authorization header
http_bearer = HTTPBearer()

# This function takes the database session and the JWT token from the request header
def get_current_user(db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(http_bearer)):
    
    try:
        # Extract the actual token string from the credentials
        token_string = token.credentials
        
        # Decode the JWT token
        payload = jwt.decode(token_string, secret, algorithms=["HS256"])
        user_id = payload.get("sub")
        
        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Get user from database
        user = db.query(UserModel).filter(UserModel.id == int(user_id)).first()
        if user is None:
            raise HTTPException(
                status_code=401,
                detail="User not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        return user
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

def get_current_active_user(current_user: UserModel = Depends(get_current_user)):
    # Add any additional user status checks here if needed
    return current_user

def require_admin(current_user: UserModel = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )
    return current_user

def get_token_payload(credentials: HTTPAuthorizationCredentials = Depends(http_bearer)):
    token_string = credentials.credentials
    
    try:
        payload = jwt.decode(token_string, secret, algorithms=["HS256"])
        return payload
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"}
        )