from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class TaskCreate(BaseModel):
    user_id:int
    title: str
    description: str
    is_complete: bool

class TaskUpdate(BaseModel):
    title: str
    description: str
    is_complete: bool

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    is_complete: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    user_id: int

    model_config = {
        "from_attributes": True
    }