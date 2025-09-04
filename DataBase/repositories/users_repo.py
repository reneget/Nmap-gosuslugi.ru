from typing import Optional, Type

from sqlalchemy.orm import Session

from DataBase.models import Users


class UserRepo:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, full_name: str, position: str, unique_key: str) -> Users:
        user = Users(full_name=full_name, position=position, unique_key=unique_key)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_id(self, user_id: int) -> Optional[Users] | None:
        return self.db.query(Users).filter(Users.user_id == user_id).first()

    def get_all_users(self) -> list[Type[Users]] | None:
        return self.db.query(Users).all()

    def update_user(self, user_id: int, **new_values) -> Type[Users] | None:
        user = self.get_user_by_id(user_id)
        if user:
            for key, value in new_values.items():
                if hasattr(user, key) and value is not None:
                    setattr(user, key, value)
            self.db.commit()
            self.db.refresh(user)
        return user
    
    def update_user_key(self, user_id: int, new_key: str) -> Type[Users] | None:
        user = self.get_user_by_id(user_id)
        user.unique_key = new_key
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user_id: int) -> Type[Users] | None:
        user = self.get_user_by_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
        return user
