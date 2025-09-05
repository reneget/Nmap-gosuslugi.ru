from fastapi import APIRouter, status, HTTPException

import logging

from .pydantic import UserProperties
from functions import Password, Database

server_router = APIRouter(
    prefix='/server',
    tags=['server']
)

server_logger = logging.getLogger(__name__)

@server_router.post('/chek/password')
async def operation_emulation(user_properties: UserProperties):
    try:
        server_logger.info('Password verification request')

        # params
        user_id = user_properties.user_id
        unique_key = user_properties.key
        entropy = user_properties.entropy

        server_logger.info('Getting parameters for generation')
        properties = Database.get_user_key_properties(user_id)
        secret_key, is_active = properties['secret_key'], properties['is_active'] 

        if is_active is None:
            return False

        server_logger.info('Parameters received')

        gen_key = Password.generated_new_key(secret_key, entropy)
        server_logger.info('Generate a key to check against the reader key')
        
        check_keys = Password.key_verification(unique_key, gen_key[0])
        server_logger.info(f'status={check_keys}')

        return check_keys
    except:
        server_logger.error('Error checking key', exc_info=True)
