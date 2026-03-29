from datetime import datetime, timezone, timedelta

from typing import Tuple

from api.crypt.jwt_token import create_token
from settings import EXPIRES_ACCESS, EXPIRES_REFRESH


def get_token(user_id: int) -> Tuple[str, str, datetime, datetime]:
    created_at = datetime.now(timezone.utc)
    expires_in = created_at + timedelta(EXPIRES_REFRESH)

    data = {
        'user_id': user_id,
    }

    access_token = create_token(
        data=data,
        created_at=created_at,
        expires_delta=EXPIRES_ACCESS
    )

    refresh_token = create_token(
        data=data,
        created_at=created_at,
        expires_delta=EXPIRES_REFRESH
    )

    return access_token, refresh_token, created_at, expires_in
