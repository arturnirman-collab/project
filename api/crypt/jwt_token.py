from datetime import datetime, timedelta

import jwt

from settings import SECRET_KEY, ALGORITHM

def create_token(data: dict, created_at: datetime, expires_delta: int) -> str:
    to_encode = data.copy()

    expires_in = created_at + timedelta(days=expires_delta)
    to_encode.update({'exp': expires_in})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

    return encoded_jwt

def verify_token(token: str) -> dict:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
