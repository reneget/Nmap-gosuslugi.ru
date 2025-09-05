from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from configurations import main_config
import logging

db_logger = logging.getLogger(__name__)
engine = create_engine(main_config.db.db_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def create_tables():
    """
    Creating all tables in the DataBase
    """
    Base.metadata.create_all(bind=engine)


def get_db():
    """
    Creating DataBase connection session
    """
    db = SessionLocal()
    try:
        db_logger.info(f'DataBase connection session has been created')
        yield db

    except HTTPException:
        db_logger.error(f'DataBase connection went wrong', exc_info=True)
        raise
    except Exception as e:
        db_logger.error(f'DataBase connection went wrong', exc_info=True)
    finally:
        db_logger.info(f'DataBase connection session has been closed')
        db.close()
