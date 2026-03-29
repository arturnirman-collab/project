from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api import get_token
from api.crypt import validate_password, hash_password
from api.pydantic_models import UserLogin, Token
from database import get_db
from database.models import User, RefreshToken

router = APIRouter()

@router.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter_by(login=user.login).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User with this login does not exist.'
        )

    if not validate_password(user.password, db_user.password_hash): #type: ignore[assignment]
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect password.'
        )

    user_id: int = db_user.id #type: ignore[assignment]

    access_token, refresh_token, created_at, expires_in = get_token(user_id)

    refresh_hash = hash_password(refresh_token)

    refresh_token_sub = RefreshToken(
        refresh_hash=refresh_hash,
        user_id=user_id,
        created_at=created_at,
        expires_in=expires_in
    )

    db.add(refresh_token_sub)
    db.commit()

    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type='bearer'
    )
