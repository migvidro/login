from uuid import UUID

from sqlalchemy.orm import Session


from src.model.user import User


def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id_ == user_id).first()
