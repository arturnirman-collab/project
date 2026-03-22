from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from sqlalchemy.orm import Session

from api.pydantic_models.user import UserRegister, UserLogin
from database.models.user import User

from database.run_database import get_db
from crypt.password_hashing import hash_password

router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserRegister, db: Session = Depends(get_db)):
    if not user.is_valid_login:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Login must contain only numbers, _, or '
                                                                            'letters and must be from 5 to 30 characters long.')
    if not user.is_valid_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Password must be at least 8 characters long'
                                                                            'and contain at least one uppercase letter,'
                                                                            'one lowercase letter, and one digit.')

    existing_user = db.query(User).filter_by(login=user.login).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='User with this login already exists.')

    hashed_password = hash_password(user.password)
    new_user = User(
        login=user.login,
        password=hashed_password,
        email=user.email
    )

    db.add(new_user)
    db.commit()

    return {"message": f"User {user.login} registered successfully!"}

@router.post("/login")
async def login(user: UserLogin):
    pass
