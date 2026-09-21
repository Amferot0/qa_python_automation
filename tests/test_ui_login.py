from pages.login_page import LoginPage

def test_login_success(page):
    products = LoginPage(page).open().login("standard_user", "secret_sauce")
    assert page.locator("[data-test='title']").inner_text() == "Products"

def test_login_wrong_password(page):
    products = LoginPage(page).open().login("standard_user", "wrong_password")
    assert page.locator(".error-message-container").is_visible()