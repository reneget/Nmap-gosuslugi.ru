from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from . import pydantic_models as pd_md 
from DataBase.core.db_connection import get_db 
from DataBase.repositories import UserRepo
from ..functions import FunctionsAPI as Func_API

import logging

user_logger = logging.getLogger(__name__)

user_router = APIRouter(
    prefix='/user',
    tags=['user']
)

@user_router.post('/create/user')
async def create_user_route(user: pd_md.User_create, db: Session = Depends(get_db)):
    """
    Api router what creating new User
    """
    try:
        user_logger.info('Request to create a new employee')
        created_user = UserRepo(db).create_user(**user.__dict__)

        if created_user is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not unique'
            )
        user_logger.debug(f'{repr(created_user)}')
        user_logger.info('New employee created')
        user_logger.info(f'Employee {created_user.full_name} was issued a new token')

        return pd_md.User(**created_user.__dict__)
    except HTTPException:
        user_logger.error('An error occurred while creating the employee', exc_info=True)
        raise
    except:
        user_logger.error('An error occurred while creating the employee', exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@user_router.get('/get/user/{user_id}')
async def get_user_by_id_api(user_id: int, db: Session = Depends(get_db)):
    try:
        user_logger.info(f'Request to get user: user_id={user_id}')
        user = UserRepo(db).get_user_by_id(user_id)
        user_logger.info('User received')
        user_logger.debug(repr(user))

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User not found'
            )

        return pd_md.User(**user.__dict__)
    except HTTPException:
        user_logger.error('Error getting user', exc_info=True)
        raise
    except:
        user_logger.error('Error getting user', exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
@user_router.get('/get/key/properties/user/{user_id}')
async def get_user_properties_key_api(user_id: int, db: Session = Depends(get_db)):
    try:
        user_logger.info(f'Request to get user unique key: user_id={user_id}')
        secret_key, is_active = UserRepo(db).get_user_key_properties(user_id)
        user_logger.info('User unique key received')

        if secret_key is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User not found'
            )

        return {'secret_key': secret_key, 'is_active': is_active}
    except HTTPException:
        user_logger.error('Error getting user unique key', exc_info=True)
        raise
    except:
        user_logger.error('Error getting user unique key', exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@user_router.get('/get/all/users')
async def get_all_user_api(db: Session = Depends(get_db)):
    try:
        user_logger.info('Request to get all users')
        list_users = UserRepo(db).get_all_users()
        user_logger.info('All users received')

        new_list = Func_API.convert_list_users(list_users)
        user_logger.info('Users converted to pydantic model')

        return new_list
    except:
        user_logger.error('Error getting all users', exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@user_router.put('/update/user/{user_id}')
async def update_user_api(user_id: int, user: pd_md.User_update, db: Session = Depends(get_db)):
    try:
        user_logger.info(f'User update request: user_id={user_id}')
        new_user = UserRepo(db).update_user(user_id, **user.__dict__)
        user_logger.info('User updated')

        if new_user is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User not found'
            )

        return  pd_md.User(**new_user.__dict__)
    except HTTPException:
        user_logger.error('Error updating user', exc_info=True)
        raise
    except:
        user_logger.error('Error updating user', exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
@user_router.delete('/delete/user/{user_id}')
async def delete_user_api(user_id: int, db: Session = Depends(get_db)):
    try:
        user_logger.info(f'Request to delete user: user_id={user_id}')
        user = UserRepo(db).delete_user(user_id)
        user_logger.info('User deleted')

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User not found'
            )
        return pd_md.User(**user.__dict__)
    except HTTPException:
        user_logger.error('Error deleting user', exc_info=True)
        raise
    except:
        user_logger.error('Error deleting user', exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


