products = ["Сумка", "Брюки", "Жилет"]

# Выведи первый и последний элементы
print(products[0], products[-1]) 

# Добавь четвёртый товар и выведи длину списка
products.append("Рубашка")
print(len(products))

# Создай словарь api_response с ключами
api_response = {
    "status_code": 200,
    "message": "success",
    "is_cached": False
}

# Выведи значение ключа "message"
print(api_response["message"])

# Добавь в словарь ключ "response_time_ms" с любым числом
api_response["response_time_ms"] = 300

# Выведи весь словарь целиком
print(api_response)