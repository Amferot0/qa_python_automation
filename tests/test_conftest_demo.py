import pytest

def test_users_count(users):          # имя параметра = имя фикстуры
    print("пользователей > 0")
    assert len(users) > 0