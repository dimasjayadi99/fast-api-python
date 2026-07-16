from fastapi import FastAPI

from routes.auth_router import router as auth_router
from routes.user_router import router as user_router
from routes.task_router import router as task_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(task_router)
