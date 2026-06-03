from fastapi import FastAPI
from app.database.connections import engine,Base
from app.database.models import *
from app.routers.user import router as user_router
from app.routers.list import router as todo_router
app=FastAPI()

# Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(todo_router)