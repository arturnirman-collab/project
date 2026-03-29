from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models import Base

if TYPE_CHECKING:
    from database.models import Sensors, RefreshToken


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(String(50), unique=True)
    password_hash: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(50), unique=True)

    last_month_sensors_values: Mapped[list['Sensors']] = relationship(back_populates='user')
    refresh_tokens: Mapped[list['RefreshToken']] = relationship(back_populates='user')
