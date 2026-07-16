from dotenv import load_dotenv
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.user import User
from schema.auth import UserLogin
from schema.user import UserCreate, UserUpdate
from utils.security import create_access_token, hash_password, verify_password
class UserService:
    @staticmethod
    def create_user(db: Session, request: UserCreate):
        user_data = request.model_dump()
        user_data["password"] = hash_password(user_data.pop("password"))

        user = User(**user_data)

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    
    @staticmethod
    def update_user(db: Session, user_id: int, request: UserUpdate):
        user = db.query(User).filter(User.id == user_id).first()

        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
        )
        
        update_data = request.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)

        return user
    
    @staticmethod
    def delete_user(db: Session, user_id : int):
        user = db.query(User).filter(User.id == user_id).first()

        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
        )
        
        db.delete(user)
        db.commit()

        return user
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
        )
        return user
    
    @staticmethod
    def get_users(db: Session):
        return db.query(User).all()


    @staticmethod
    def login(
        db: Session,
        request: UserLogin
    ):
        user = db.query(User).filter(
            User.email == request.email
        ).first()

        if user is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        if not verify_password(
            request.password,
            user.password
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )
        
        token = create_access_token(
            {
                "sub": str(user.id)
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }