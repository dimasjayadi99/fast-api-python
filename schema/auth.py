from pydantic import BaseModel

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class UserLogin(BaseModel):
    email: str
    password: str