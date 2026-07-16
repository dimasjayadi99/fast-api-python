from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from schema.message import MessageResponse
from schema.task import TaskCreate, TaskResponse, TaskUpdate
from services.task_service import TaskService

router = APIRouter(prefix="/task", tags=["task"])

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    request: TaskCreate,
    db: Session = Depends(get_db)
):
    return TaskService.create_task(
        db=db,
        request=request
    )

@router.put("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def update_task(
    task_id: int,
    request: TaskUpdate,
    db: Session = Depends(get_db)
):
    return TaskService.update_task(
        db=db,
        request=request,
        task_id=task_id
    )

@router.delete("/{task_id}", response_model=MessageResponse, status_code=status.HTTP_200_OK)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
):
    TaskService.delete_task(
        db=db,
        task_id=task_id
    )

    return {
        "message": "Delete task successfully"
    }

@router.get("/", response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
def get_tasks(
    db: Session = Depends(get_db),

):
    return TaskService.get_all_task(
        db = db
    )

@router.get("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def get_task_by_id(
    task_id: int,
    db: Session = Depends(get_db),
): 
    return TaskService.get_task_by_id(
        db=db,
        task_id=task_id
    )