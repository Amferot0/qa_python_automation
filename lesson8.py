import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(response.status_code) # выводит код ответа
data = response.json()      # response.json() возвращает словарь — сохраним его
print(data["username"])     # достань значение по ключу, как в уроке 2

payload = {"title": "Первый пост", "body": "Что творится", "userId": 1,}
response = requests.post("https://jsonplaceholder.typicode.com/posts",json=payload)

actual_response_code = response.status_code
expected_code = 201
def check_status_code(actual, expected):
    if actual == expected:
        return "✅ Тест пройден"
    else:
        return "❌ Тест провален"

print(response.status_code) # выводит код ответа
print(response.json()["id"]) # выводит значение ключа ответа, видимо без сохранения данных
print(check_status_code(actual_response_code, expected_code))