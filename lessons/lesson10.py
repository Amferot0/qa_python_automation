import requests

def check_status_code(actual, expected):
    return actual == expected   # теперь возвращает True/False, а не строки

def test_get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "Bret"

def test_post_creates_post():
    payload = {"title": "тест", "body": "привет", "userId": 1}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201
    assert "id" in response.json()