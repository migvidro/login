import uuid

from sqlalchemy import Boolean, Column, DateTime, String, func

from ..core.database import Base


class BaseEntityModel(Base):
    id_ = Column(
        String(36), nullable=False, unique=True, default=uuid.uuid4, primary_key=True
    )
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    last_updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=True
    )
    last_updated_by = Column(
        String(36), nullable=False, unique=True, default=uuid.uuid4
    )
    deleted = Column(Boolean(), default=False, nullable=True)
