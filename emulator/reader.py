#!/usr/bin/env python3
from crypto import generate_key, generate_entropy
import os

SECRET_FILE = 'secret_key.txt'

def load_secret_key():
    if not os.path.exists(SECRET_FILE):
        return None
    
    try:
        with open(SECRET_FILE, 'r') as f:
            secret = f.read().strip()
        if not secret:
            return None
        return secret
    except:
        return None


def verify_key(input_key: str):
    secret_key = load_secret_key()
    if not secret_key:
        return False
    
    expected_key = generate_key(secret_key, entropy)
    
    if input_key == expected_key:
        
        return True
    
    return False

def main():
    # Первая проверка
    first_key = input().strip()
    if not first_key:
        print("Доступ запрещен")
        return
    
    # Вторая проверка
    second_key = input().strip()
    if not second_key:
        print("Доступ запрещен")
        return
    
    # Проверяем оба ключа
    first_valid = verify_key(first_key)
    second_valid = verify_key(second_key)
    
    # Доступ разрешен только если оба ключа верны
    if first_valid and second_valid:
        print("Доступ разрешен")
    else:
        print("Доступ запрещен")

if __name__ == "__main__":
    main()
