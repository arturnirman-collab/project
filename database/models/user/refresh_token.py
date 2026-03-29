from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models import Base

if TYPE_CHECKING:
    from database.models import User


class RefreshToken(Base):
    __tablename__ = "refresh_token"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    refresh_hash: Mapped[str] = mapped_column(String(255))

    created_at: Mapped[datetime] = mapped_column()
    expires_in: Mapped[datetime] = mapped_column()

    user: Mapped['User'] = relationship(back_populates='refresh_tokens')
