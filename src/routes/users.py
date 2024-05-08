from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.entities.user import User
from src.core.database import get_db
from src.services import user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}", response_model=User)
async def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
    return user_service.get_user_by_id(db, user_id)
