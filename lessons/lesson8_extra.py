import requests

def check_status_code(actual, expected):
    if actual == expected:
        return "✅ Тест пройден"
    else:
        return "❌ Тест провален"

# Шаг 1: JSON бывает списком

response = requests.get("https://jsonplaceholder.typicode.com/users")

users = response.json()      # response.json() возвращает данные — сохраним их
print(len(users)) # выведем число пользователей
print(users[1]['email'])     # выводит значение email второго пользователя

# Шаг 2: негативный тест
response = requests.get("https://jsonplaceholder.typicode.com/posts/9999")

print(check_status_code(response.status_code, 404))

# Шаг 3: новый метод DELETE
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(check_status_code(response.status_code, 200))