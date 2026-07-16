from typing import TYPE_CHECKING, List
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

if TYPE_CHECKING:
    from models.task import Task

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    phone: Mapped[str] = mapped_column(String(20), unique=True)
    address: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))

    task: Mapped[List["Task"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )
