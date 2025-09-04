#!/usr/bin/env python3
import hmac
import hashlib
import base64
import os
import sys

SECRET_FILE = 'secret_key.txt'
COUNTER_FILE = 'counter.txt'

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
        sys.exit(1)
    
    try:
        with open(SECRET_FILE, 'r') as f:
            secret = f.read().strip()
        if not secret:
            sys.exit(1)
        return secret
    except:
        sys.exit(1)

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

def main():
    secret_key = load_secret_key()
    counter = load_counter()
    key_base64 = generate_key(secret_key, counter)
    counter += 1
    save_counter(counter)
    print(key_base64)

if __name__ == "__main__":
    main()
