import uuid

from sqlalchemy import Column, String

from .base import BaseEntityModel


class User(BaseEntityModel):
    __tablename__ = "users"

    password = Column(String(50), nullable=False, unique=True, default=uuid.uuid4)
