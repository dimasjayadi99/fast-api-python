from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    phone: str
    address: str
    email: str
    password: str

class UserUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None
    address: str | None = None

class UserResponse(BaseModel):
    id: int
    name: str
    phone: str
    email: str
    address: str

    model_config = {
        "from_attributes" : True
    }
