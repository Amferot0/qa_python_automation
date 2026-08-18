import requests

def test_get_len_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    assert len(response.json()) == 10

def test_get_negative():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/9999")
    assert response.status_code == 404

def test_delete_user():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200