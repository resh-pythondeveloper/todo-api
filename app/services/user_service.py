from app.database.models.user_models import User
from app.utils.hash import hashpassword,verify_password
from app.utils.token import create_access_token,create_refresh_token
from fastapi import HTTPException, status

def create_user(db,user_data):
    existing_username = db.query(User).filter(
        User.username == user_data.username
    ).first()
    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    # Check email
    existing_email = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    hashed_password=hashpassword(user_data.password)
    new_user=User(username=user_data.username,password=hashed_password,email=user_data.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def UserLogin(db,user_data):
    user=db.query(User).filter(User.username==user_data.username).first()
    if not user:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="username not found")
    if not verify_password(user_data.password,user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid password")
    access_token=create_access_token(data={"sub":user.username})
    refresh_token = create_refresh_token(
        data={"sub": user.username}
    )
    return {
        "access_token": access_token,
        "refresh_token":refresh_token,
        "token_type": "bearer"
    }
