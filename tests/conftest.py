import pytest
import requests
import allure

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture()
def users():
    print("setup: получаю пользователей")
    response = requests.get(BASE_URL + "/users") # выполняем запрос
    yield response.json() # получает ответ, отдаём данные тесту
    print("teardown: завершаю работу")   # выполнится ПОСЛЕ теста

from core.api_client import ApiClient

@pytest.fixture()
def api():
    client = ApiClient(BASE_URL)
    yield client

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is not None:
            allure.attach(
                page.screenshot(),
                name="screenshot on failure",
                attachment_type=allure.attachment_type.PNG,
            )