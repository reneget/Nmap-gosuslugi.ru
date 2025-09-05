#!/usr/bin/env python3
import hmac
import hashlib
import base64
import os

SECRET_FILE = 'secret_key.txt'
COUNTER_FILE = 'counter_reader.txt'

def load_counter():
    if os.path.exists(COUNTER_FILE):
        try:
            return int(open(COUNTER_FILE).read().strip())
        except ValueError:
            return 0
    return 0

def save_counter(counter):
    with open(COUNTER_FILE, 'w') as f:
        f.write(str(counter))

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

def generate_entropy(shared_secret: str, counter: int) -> bytes:
    return hmac.new(
        shared_secret.encode('utf-8'), 
        counter.to_bytes(8, 'big'), 
        hashlib.sha512
    ).digest()

def generate_key(shared_secret: str, counter: int) -> str:
    entropy_bytes = generate_entropy(shared_secret, counter)
    hmac_hash = hmac.new(
        shared_secret.encode('utf-8'), 
        entropy_bytes, 
        hashlib.sha512
    ).digest()
    return base64.b64encode(hmac_hash).decode('utf-8').rstrip('=')

def verify_key(input_key: str):
    secret_key = load_secret_key()
    if not secret_key:
        return False
    
    current_counter = load_counter()
    expected_key = generate_key(secret_key, current_counter)
    
    if input_key == expected_key:
        new_counter = current_counter + 1
        save_counter(new_counter)
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
