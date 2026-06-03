from app.database.connections import Base,engine,sessionlocal
from app.schemas.todo_schemas import Todo_schemas
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.services.todo_service import TodoCreate,ViewTodo
from app.utils.dependencies import get_current_user
from app.database.models.user_models import User

router=APIRouter(prefix="/todo",tags=["Todos"])

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/')
def Createtodo(todo:Todo_schemas,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return TodoCreate(todo,db,current_user)

@router.get('/')
def get_todos(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return ViewTodo(db, current_user)

@router.get("/{todo_id}")
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return ViewTodo(db, current_user, todo_id)