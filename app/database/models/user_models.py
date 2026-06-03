from sqlalchemy import Column,String,Integer,Boolean
from app.database.connections import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__="users"
    id=Column(Integer,autoincrement=True,primary_key=True,index=True)
    username=Column(String(255),unique=True,index=True)
    email=Column(String(255),unique=True,index=True)
    password=Column(String(255))
    is_deleted=Column(Boolean,default=False)
    todos = relationship(
        "Todo",
        back_populates="user")
