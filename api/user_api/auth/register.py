from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from api import login
from api.crypt import hash_password
from api.pydantic_models import UserRegister, UserLogin
from database import get_db
from database.models import User

router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserRegister, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter_by(login=user.login).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='User with this login already exists.')

    hashed_password = hash_password(user.password)
    new_user = User(
        login=user.login,
        password_hash=hashed_password,
        email=user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return await login(
        UserLogin(
            login=user.login,
            password=user.password,
        ),
        db=db
    )