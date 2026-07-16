from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from database import get_db
from models.user import User
from schema.message import MessageResponse
from schema.user import UserCreate, UserResponse, UserUpdate
from services.user_service import UserService
from utils.security import get_current_user

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    request: UserCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return UserService.create_user(
        db=db,
        request=request
    )

@router.put("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def update_user(
    user_id: int,
    request: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
): 
    return UserService.update_user(
        db=db,
        request=request,
        user_id=user_id
    )

@router.delete("/{user_id}", response_model=MessageResponse, status_code=status.HTTP_200_OK)
def delete_user(
    user_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    UserService.delete_user(
        db=db,
        user_id=user_id
    )

    return {
        "message": "Delete user successfully"
    }

@router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def get_users(
    current_user: User = Depends(get_current_user),
    db:Session = Depends(get_db)
):
    return UserService.get_users(db=db)

@router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user_by_id(
    user_id: int,
    current_user: User = Depends(get_current_user),
    db:Session = Depends(get_db),
):
    return UserService.get_user_by_id(
        db=db,
        user_id=user_id
    )