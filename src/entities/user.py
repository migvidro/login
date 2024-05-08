from src.entities.base_entity import BaseEntity


class User(BaseEntity):
    name: str
    email: str
    password: str
