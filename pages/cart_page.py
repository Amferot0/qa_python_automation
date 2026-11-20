class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator (".cart_item")
        self.checkout_button = page.locator ("#checkout")

def get_item_count(self):
    return self.cart_item.count()

def proceed_to_checkout(self):
    self.checkout_button.click()
    return self.page