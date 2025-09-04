import hmac
import hashlib
import struct
import base64

def generate_key(shared_secret: str, counter: int) -> str:
    """
    Генерирует ключ на основе секрета и счётчика.
    :param shared_secret: секрет.
    :param counter: счётчик (кол-во считываний).
    :return: Строковый ключ (полный хэш, ~86-128 символов).
    """
    # Конвертируем счётчик в байты (big-endian, 8 байт)
    counter_bytes = struct.pack('>Q', counter)

    # Кодируем секрет в байты
    secret_bytes = shared_secret.encode('utf-8')

    # Вычисляем HMAC-SHA512 от счётчика с использованием секрета
    hmac_hash = hmac.new(secret_bytes, counter_bytes, hashlib.sha512).digest()
    open('crypto/counter.txt', 'w').write(str(counter + 1))
    return base64.b64encode(hmac_hash).decode('utf-8').rstrip('=')

counter = int(open('crypto/counter.txt', 'r').read())
shared_secret = str(open('crypto/secret.txt', 'r').read())
key_base64 = generate_key(shared_secret, counter)
