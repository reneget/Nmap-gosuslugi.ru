from sqlalchemy import Column, Integer, ForeignKey, String
import logging

from DataBase.core.db_connection import Base

user_model_logger = logging.getLogger(__name__)


class Users(Base):
    """
    User table model for dataBase
    """

    __tablename__ = 'Users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, unique=False, nullable=False)
    position = Column(String, unique=False, nullable=False)
    unique_key = Column(String, unique=True, nullable=False)
    counter = Column(Integer, unique=False, nullable=False, default=0)

    def __repr__(self):
        try:
            return f'Users(user_id={self.user_id}, full_name={self.full_name}, position={self.position}, counter={self.counter})'
        except Exception as e:
            user_model_logger.error(f'Error from returning of string format User model', exc_info=True)
