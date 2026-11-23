import allure
from pages.login_page import LoginPage
#from pages.cart_page import CartPage

@allure.title("Добавление товара в корзину")
def test_add_to_cart(page):
    products_page = LoginPage(page).open().login("standard_user", "secret_sauce")
    products_page.add_item_to_cart(0)
    assert products_page.get_cart_count() == 1

@allure.title("Содержимое корзины")
def test_items_in_cart(page):
    products_page = LoginPage(page).open().login("standard_user", "secret_sauce")
    products_page.add_item_to_cart(0)
    cart_page = products_page.open_cart() 
    assert cart_page.get_item_count() == 1