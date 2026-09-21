import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture()
def users():
    print("setup: получаю пользователей")
    response = requests.get(BASE_URL + "/users") # выполняем запрос
    yield response.json() # получает ответ, отдаём данные тесту
    print("teardown: завершаю работу")   # выполнится ПОСЛЕ теста


def test_users_count(users):          # имя параметра = имя фикстуры
    print("10 пользователей")
    assert len(users) == 10

def test_first_user_has_email(users):
    print("ключ email есть у первого пользователя")
    assert "email" in users[0] # ключ "email" есть в словаре user