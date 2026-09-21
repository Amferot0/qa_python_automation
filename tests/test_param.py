import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.parametrize("url, excepted", [
    ("/users", 200),
    ("/posts/1", 200),
    ("/posts/0", 404),
    ("/posts/9999", 404),
    ("/users/9999", 404),
])

def test_status_codes(url, excepted):
    response = requests.get(BASE_URL + url)
    assert response.status_code == excepted

@pytest.mark.parametrize("post_id", [1, 2, 3,])

def test_get_post(api, post_id):
    response = api.get_post(post_id) 
    assert response.status_code == 200
    assert response.json()["id"] == post_id