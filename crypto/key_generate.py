import hmac
import hashlib
import base64
import secrets

def generate_entropy(length) -> str:
    return secrets.token_hex(length)

def generate_key(shared_secret: str, entropy: str) -> str:
    """
    Генерирует ключ на основе секрета и "энтропии".
    :param shared_secret: секрет.
    :param entropy: "энтропия"
    :return: Строковый ключ.
    """
    # Конвертируем счётчик в байты (big-endian, 8 байт)
    entropy_bytes = bytes.fromhex(entropy)

    # Кодируем секрет в байты
    secret_bytes = shared_secret.encode('utf-8')

    # Вычисляем HMAC-SHA512 от энтропии с использованием секрета
    hmac_hash = hmac.new(secret_bytes, entropy_bytes, hashlib.sha512).digest()
    return base64.b64encode(hmac_hash).decode('utf-8').rstrip('='), entropy

shared_secret = str(open('crypto/secret.txt', 'r').read())
key_base64 = generate_key(shared_secret, entropy=generate_entropy(16))[0]
print(key_base64)