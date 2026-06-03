from pydantic import BaseModel

class Todo_schemas(BaseModel):
    title:str
    description:str

class UpdateTodoSchema(BaseModel):
    title: str | None = None
    description: str | None = None