from sqlalchemy import Column, String
from database.models.base_model import Base


class User(Base):
    login = Column(String(50), primary_key=True, nullable=False)
    password = Column(String(120), nullable=False)
    email = Column(String(50), nullable=False)
