import pytest

def test_users_count(users):          # имя параметра = имя фикстуры
    print("10 пользователей")
    assert len(users) == 10

def test_first_user_has_email(users):
    print("ключ email есть у первого пользователя")
    assert "email" in users[0] # ключ "email" есть в словаре user