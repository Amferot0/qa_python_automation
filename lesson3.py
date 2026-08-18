# Список кодов ответов
status_codes = [200, 201, 400, 403, 404, 500]

# Проход циклом for по каждому коду и вывод его категории через if / elif / else
for status_code in status_codes:
    if status_code < 300:
        print(f"Код {status_code}: успех")
    elif status_code < 500:
        print(f"Код {status_code}: ошибка клиента")
    else:
        print(f"Код {status_code}: ошибка сервера")

# Создай переменную expected_status = 200 и проверь первый элемент списка выведи ✅ Тест пройден, иначе — ❌ Тест провален
expected_status = 200
if status_codes[0] == expected_status:
    print("✅ Тест пройден")
else:
    print("❌ Тест провален")