from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.task import Task
from schema.task import TaskCreate

class TaskService:

    @staticmethod
    def create_task(db: Session, request: TaskCreate):
        task = Task(**request.model_dump())

        db.add(task)
        db.commit()
        db.refresh(task)

        return task

    @staticmethod
    def update_task(db: Session, task_id: int, request: TaskCreate):
        task = db.query(Task).filter(Task.id == task_id).first()

        if task is None:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

        task.title = request.title
        task.description = request.description
        task.is_complete = request.is_complete
        task.updated_at = datetime.now()

        db.commit()
        db.refresh(task)

        return task

    @staticmethod
    def delete_task(db: Session, task_id: int):
        task = db.query(Task).filter(Task.id == task_id).first()

        if task is None:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

        db.delete(task)
        db.commit()

        return task

    @staticmethod
    def get_task_by_id(db: Session, task_id: int):
        task = db.query(Task).filter(Task.id == task_id).first()

        if task is None:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

        return task

    @staticmethod
    def get_all_task(db: Session):
        return db.query(Task).all()