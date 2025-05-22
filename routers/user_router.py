# app/routers/user_router.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.repositories.user_repository import UserRepository
from app.services.user_services import UserService
from app.schemas.user_schema import UserCreate, UserSchema
from app.schemas.auth_schema import AuthRequest

router = APIRouter(prefix="/users", tags=["Users"])

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repo = UserRepository(db)
    return UserService(repo)

@router.post("/register", response_model=UserSchema)
def register_user(
    user_create: UserCreate,
    service: UserService = Depends(get_user_service)
):
    
    return service.create(user_create.name , user_create.email , user_create.password , user_create.age)

@router.post("/authenticate")
def authenticate_user(
    auth_request: AuthRequest,
    service: UserService = Depends(get_user_service)
):
    authenticated = service.authenticate(auth_request.email, auth_request.password)

    if not authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    return {"message": "Authentication successful"}

@router.get("/{user_id}", response_model=UserSchema)
def find_user_by_id(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    user = service.find_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user
