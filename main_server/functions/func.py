import requests

import logging

from crypto import generate_key

func_logger = logging.getLogger(__name__)

class Database:
    @staticmethod
    def get_user_key_properties(user_id: int):
        func_logger.info(f'Getting a koluch from the base: {user_id}')
        key = requests.get(f'http://127.0.0.1:8000/get/key/properties/user/{user_id}')
        func_logger.info('Key received')
        return key.json()

class Password:
    @staticmethod
    def key_verification(key: str, gen_key: str) -> bool:
        func_logger.info('Checking keys')
        status = key == gen_key
        func_logger.info(f'status={status}')
        return status
    
    @staticmethod
    def generated_new_key(secret_key: str, entropy: str) -> str:
        func_logger.info('Generate a new key')
        new_key = generate_key(secret_key, entropy)
        func_logger.info('New key generated')
        return new_key