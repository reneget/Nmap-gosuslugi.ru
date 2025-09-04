import requests

class Database:
    
    @staticmethod
    def get_key(user_id: int):
        key = requests.get(f'http://127.0.0.1:8000/user/get/unique_key/user/{user_id}')
        return key.json()

    @staticmethod
    def update_key(user_id: int, new_key: str):
        pass

class Password:
    
    @staticmethod
    def key_verification(key: str, key_from_db: str):
        return key == key_from_db
    
    @staticmethod
    def generated_new_key():
        pass