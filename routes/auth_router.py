from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from schema.auth import TokenResponse, UserLogin
from schema.user import UserCreate, UserResponse
from services.user_service import UserService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    request: UserCreate,
    db: Session = Depends(get_db)
):
    return UserService.create_user(
        db=db,
        request=request
    )

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    request: UserLogin,
    db: Session = Depends(get_db)
):
    return UserService.login(
        db=db,
        request=request
    )