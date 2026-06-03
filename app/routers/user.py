from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database.models import user_models
from app.schemas.user_schemas import CreateUserSchema,UserResponseSchema,UserLoginSchema
from app.services.user_service import create_user,UserLogin
from app.database.connections import sessionlocal
from app.utils.dependencies import get_current_user
from app.utils.token import blacklisted_tokens

router=APIRouter(prefix="/user",tags=["Users"])

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/',response_model=UserResponseSchema)
def createuser(user:CreateUserSchema,db:Session=Depends(get_db)):
    return create_user(db, user)

@router.post('/login')
def Login(user:UserLoginSchema,db:Session=Depends(get_db)):
    return UserLogin(db,user)

@router.get("/me")
def current_user(
    current_user = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email}


@router.post("/logout")
def logout(token: str):

    blacklisted_tokens.add(token)

    return {
        "message": "Logged out successfully"
    }