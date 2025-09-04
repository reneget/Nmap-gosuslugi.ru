import hmac
import hashlib
import time
import struct
import base64

counter = int(open('crypto/counter.txt', 'r').read())
def generate_key(shared_secret: str, counter: int, output_format: str = 'base64') -> str:
    """
    Максимальная безопасность: полный HMAC-SHA512 без усечения.

    :param shared_secret: Общий секрет (строка, минимум 32 символа случайности).
    :param time_step: Интервал времени в секундах (по умолчанию 30).
    :param output_format: Формат вывода: 'hex' (hex-строка) или 'base64' (base64-строка).
    :return: Строковый ключ (полный хэш, ~86-128 символов).
    """
    if output_format not in ['hex', 'base64']:
        raise ValueError("Неверный output_format: должен быть 'hex' или 'base64'.")

    # Конвертируем счётчик в байты (big-endian, 8 байт)
    counter_bytes = struct.pack('>Q', counter)

    # Кодируем секрет в байты
    secret_bytes = shared_secret.encode('utf-8')

    # Вычисляем HMAC-SHA512 от счётчика времени с использованием секрета
    hmac_hash = hmac.new(secret_bytes, counter_bytes, hashlib.sha512).digest()
    open('crypto/counter.txt', 'w').write(str(counter + 1))
    if output_format == 'hex':
        return hmac_hash.hex()
    else:  
        return base64.b64encode(hmac_hash).decode('utf-8').rstrip('=')

shared_secret = str(open('crypto/secret.txt', 'r').read())
key_base64 = generate_key(shared_secret, counter, output_format='base64')
print(f"Сгенерированный ключ (base64): {key_base64}")