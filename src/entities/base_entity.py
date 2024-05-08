from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from uuid import UUID


class BaseEntity(BaseModel):
    class Config:
        orm_mode = True

    id_: UUID
    created_at: datetime
    last_updated_at: Optional[datetime]
    last_updated_by: Optional[UUID]
    deleted: Optional[bool]
