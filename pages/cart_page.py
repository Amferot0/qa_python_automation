import allure

class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator (".cart_item")
        self.checkout_button = page.locator ("#checkout")
    
    @allure.step("Получить количество товаров в корзине")
    def get_item_count(self):
        self.cart_items.first.wait_for()   # дождаться первого элемента корзины
        return self.cart_items.count()
    
    @allure.step("Перейти к оформлению заказа")
    def proceed_to_checkout(self):
        self.checkout_button.click()
        return self.page