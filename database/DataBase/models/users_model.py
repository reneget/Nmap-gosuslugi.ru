from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, DateTime
import logging
from DataBase.core.db_connection import Base

user_model_logger = logging.getLogger(__name__)


class Users(Base):
    __tablename__ = 'Users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, unique=False, nullable=False)
    position = Column(String, unique=False, nullable=False)
    secret_key = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, unique=False, nullable=False, default=True)
    create_time = Column(DateTime, unique=False, nullable=False)
    kill_time = Column(DateTime, unique=False, nullable=True)

    def __repr__(self):
        try:
            return f'Users(user_id={self.user_id}, full_name={self.full_name}, position={self.position}, is_active={self.is_active}, kill_time={self.kill_time})'
        except Exception as e:
            user_model_logger.error(f'Error from returning of string format User model', exc_info=True)
