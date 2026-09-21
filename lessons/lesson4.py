# Напиши функцию get_status_category(code), 
# которая возвращает строку "успех" / "ошибка клиента" / "ошибка сервера"
def get_status_category(code):
    if code < 300:
        return "успех"
    elif code < 500:
        return "ошибка клиента"
    else:
        return "ошибка сервера"

# Напиши функцию check_status(actual, expected=200), 
# которая возвращает "✅ Тест пройден" или "❌ Тест провален"
def check_status(actual, expected=200):
    if actual == expected:
        return "✅ Тест пройден"
    else:
        return "❌ Тест провален"

# Создай список status_codes = [200, 201, 400, 403, 404, 500]
# и в цикле for выведи для каждого кода строку вида Код 404: ошибка клиента,
# получая категорию вызовом функции get_status_category
status_codes = [200, 201, 400, 403, 404, 500]

for status_code in status_codes:
    print(f"Код {status_code}: {get_status_category(status_code)}")

# Вызови check_status два раза: один раз передав только фактический код 200,
# второй раз — 404 и ожидаемый 404. Выведи оба результата
print(check_status(200))
print(check_status(404, 404))