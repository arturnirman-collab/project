from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models import Base

if TYPE_CHECKING:
    from database.models import User


class Sensors(Base):
    __tablename__ = 'sensors'

    id: Mapped[int] = mapped_column(primary_key=True)

    temperature: Mapped[float | None] = mapped_column()

    air_humidity: Mapped[float | None] = mapped_column()
    dirt_humidity: Mapped[float | None] = mapped_column()

    atmospheric_pressure: Mapped[float | None] = mapped_column()

    brightness: Mapped[float | None] = mapped_column()

    user: Mapped['User'] = relationship(back_populates='last_month_sensors_values')
