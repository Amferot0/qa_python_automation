from pages.login_page import LoginPage

import allure

@allure.title("Успешный вход стандартного пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success(page):
    products = LoginPage(page).open().login("standard_user", "secret_sauce")
    assert products.get_title_text() == "Products"

@allure.title("Провальный вход стандартного пользователя")
@allure.severity(allure.severity_level.BLOCKER)
def test_login_wrong_password(page):
    login_page = LoginPage(page).open()
    login_page.login("standard_user", "wrong_password")
    assert login_page.is_error_visible()