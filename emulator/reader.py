import json
def send_to_handler(user_id, entropy, pwd):
    """
    Заглушка для отправки данных в другой обработчик
    """
    data = {
        'id': user_id,
        'entropy': entropy,
        'pwd': pwd
    }
    # Заглушка - просто выводим данные
    print(f"Отправка в обработчик: {json.dumps(data, ensure_ascii=False)}")
    
    # Здесь будет реальная отправка в другой обработчик
    # Например, через HTTP запрос, очередь сообщений и т.д.
    
    # Заглушка - возвращаем True для демонстрации
    return True

def main():
    try:
        results = []
        
        # Цикл на 2 итерации
        for i in range(2):
            # Получаем ID пользователя
            user_id = input("Введите ID пользователя: ").strip()
            if not user_id:
                print("Ошибка: ID пользователя не может быть пустым")
                return
            
            # Получаем энтропию
            entropy = input("Введите энтропию: ").strip()
            if not entropy:
                print("Ошибка: Энтропия не может быть пустой")
                return
            
            # Получаем пароль
            pwd = input("Введите пароль: ").strip()
            if not pwd:
                print("Ошибка: Пароль не может быть пустым")
                return
            
            # Отправляем данные в обработчик
            result = send_to_handler(user_id, entropy, pwd)
            results.append(result)
        
        # Проверяем результаты от обработчика
        if all(results):
            print("Доступ разрешен")
        else:
            print("Доступ запрещен")
            
    except KeyboardInterrupt:
        print("\nОперация прервана пользователем")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
