from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from DataBase.core.db_connection import Base


class Users(Base):
    __tablename__ = 'Users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(30), unique=False, nullable=False)
    position = Column(String(50), unique=False, nullable=False)
    unique_key = Column(String(100), unique=True, nullable=False) 

    def __repr__(self):
        return f'Users(user_id={self.user_id}, full_name={self.full_name}, position={self.position})'

