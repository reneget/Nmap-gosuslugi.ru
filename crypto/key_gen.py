import hmac
import hashlib
import base64
import os

COUNTER_FILE = 'counter.txt'

def load_counter():
    if os.path.exists(COUNTER_FILE):
        return int(open(COUNTER_FILE).read())
    return 0

def save_counter(counter):
    with open(COUNTER_FILE, 'w') as f:
        f.write(str(counter))

def generate_entropy(shared_secret: str, counter: int) -> bytes:
    return hmac.new(shared_secret.encode('utf-8'), counter.to_bytes(8, 'big'), hashlib.sha512).digest()

def generate_key(shared_secret: str, counter: int) -> str:
    entropy_bytes = generate_entropy(shared_secret, counter)
    hmac_hash = hmac.new(shared_secret.encode('utf-8'), entropy_bytes, hashlib.sha512).digest()
    return base64.b64encode(hmac_hash).decode('utf-8').rstrip('=')

shared_secret = open('secret.txt').read().strip()
counter = load_counter()
key_base64 = generate_key(shared_secret, counter)
counter += 1
save_counter(counter)
print("Ключ сгенерирован:", key_base64)