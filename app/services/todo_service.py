from app.database.models.todo_models import Todo
from fastapi import HTTPException,Depends

def TodoCreate(todo,db,current_user):
    todo_data=Todo(title=todo.title,description=todo.description,user_id=current_user.id)
    db.add(todo_data)
    db.commit()
    db.refresh(todo_data)
    return todo_data


def ViewTodo(db,current_user,todo_id=None):
    if todo_id:
        todo=db.query(Todo).filter(Todo.user_id == current_user.id,Todo.id==todo_id).first()
        if not todo:
            raise HTTPException(
                status_code=404,
                detail="Todo not found"
            )

        return todo
    todos=db.query(Todo).filter(Todo.user_id == current_user.id,Todo.is_deleted == False).all()
    if not todos:
        raise HTTPException(status_code=404,
            detail="No todos found")
    return todos

def Updatetodo(todo,db,current_user,todo_id):
    todo_data=db.query(Todo).filter(Todo.id==todo_id,Todo.user_id==current_user.id).first()
    if not todo_data:
        raise HTTPException(status_code=404,detail='Todo not found')
    update_data = todo.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(todo_data, key, value)

    db.commit()
    db.refresh(todo_data)

    return todo_data

def DeleteTodo(db,current_user,todo_id):
    todo_data=db.query(Todo).filter(Todo.id==todo_id,Todo.user_id==current_user.id).first()
    if not todo_data:
        raise HTTPException(status_code=404,detail="todo not found")
    db.delete(todo_data)
    db.commit()
    return {
        "message": "Todo deleted successfully"
    }

def SoftdeleteTodo(db,current_user,todo_id):
    todo = db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == current_user.id,
        Todo.is_deleted == False
    ).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    todo.is_deleted = True

    db.commit()

    return {
        "message": "Todo task finish successfully"
    }