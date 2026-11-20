import allure

class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.add_to_cart_button = page.locator ("[data-test^='add-to-cart']")
        self.cart_badge = page.locator (".shopping_cart_badge")

    def get_title_text(self):
        return self.title.inner_text()

    @allure.step("Добавить товар №{index} в корзину")
    def add_item_to_cart(self, index):
        self.add_to_cart_button.nth(index).click()

    @allure.step("Получить количество товаров в корзине")
    def get_cart_count(self):
        return int(self.cart_badge.inner_text())