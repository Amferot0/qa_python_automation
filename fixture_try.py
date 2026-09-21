import pytest

@pytest.fixture()
def my_data():
    print("1) setup: фикстура готовит данные")
    yield {"number": 42}
    print("3) teardown: фикстура прибирается")

def test_one(my_data):
    print("2) test_one: мне приехало", my_data["number"])
    assert my_data["number"] == 42

def test_two(my_data):
    print("2) test_two: мне приехало", my_data["number"])
    assert my_data["number"] == 42
