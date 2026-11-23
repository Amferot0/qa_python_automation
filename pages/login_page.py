import allure

from pages.products_page import ProductsPage

class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator(".error-message-container")

    @allure.step("Открыть страницу логина")
    def open(self):
        self.page.goto(self.URL, wait_until="domcontentloaded") # открыть сайт
        return self

    @allure.step("Ввести логин {username} и пароль, нажать вход")
    def login(self, username, password):
        self.username_input.fill(username) # ввести текст в поле
        self.password_input.fill(password) 
        self.login_button.click() # кликнуть
        return ProductsPage(self.page)   # после входа мы на странице товаров

    def is_error_visible(self):
        self.error_message.wait_for()
        return self.error_message.is_visible()