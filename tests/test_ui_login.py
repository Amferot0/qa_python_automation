def test_login_success(page):
    page.goto("https://www.saucedemo.com/")          # открыть сайт
    page.fill("#user-name", "standard_user")          # ввести текст в поле
    page.fill("#password", "secret_sauce")
    page.click("#login-button")                       # кликнуть
    assert page.locator("[data-test='title']").inner_text() == "Products"

def test_login_wrong_password(page):
    page.goto("https://www.saucedemo.com/")          # открыть сайт
    page.fill("#user-name", "standard_user")          # ввести текст в поле
    page.fill("#password", "wrong_password")           # невалидный пароль
    page.click("#login-button")                       # кликнуть
    assert page.locator(".error-message-container").is_visible()