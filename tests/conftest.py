import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture()
def users():
    print("setup: получаю пользователей")
    response = requests.get(BASE_URL + "/users") # выполняем запрос
    yield response.json() # получает ответ, отдаём данные тесту
    print("teardown: завершаю работу")   # выполнится ПОСЛЕ теста