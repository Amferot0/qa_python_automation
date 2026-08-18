import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"   # константа — DRY!

@pytest.mark.parametrize("url,expected", [
    ("/users", 200),
    ("/posts/1", 200),
    ("/posts/9999", 404),
    ("/users/9999", 404),
])
def test_status_codes(url, expected):
    response = requests.get(BASE_URL + url)
    assert response.status_code == expected