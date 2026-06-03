from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from app.database.connections import Base
from app.database.models.user_models import User
from sqlalchemy.orm import relationship

class Todo(Base):
    __tablename__="todos"
    id=Column(Integer,primary_key=True,autoincrement=True,index=True)
    title=Column(String(50))
    description=Column(String(100))
    is_deleted=Column(Boolean,default=False)
    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )
    user = relationship(
        "User",
        back_populates="todos"
    )