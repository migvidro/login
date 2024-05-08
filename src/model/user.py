from sqlalchemy import Column, String

from src.model.base_model import BaseModel
from src.core.database import Base


class User(BaseModel, Base):
    __tablename__ = "users"

    name = Column(String(100), unique=False, nullable=False)
    email = Column(String(100), unique=False, nullable=False)
    password = Column(String(100), nullable=False, unique=False)
