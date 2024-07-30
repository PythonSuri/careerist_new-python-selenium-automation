from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    def open(self):
        self.open_url('https://www.target.com/cart')


class CartPage(Page):
    CART_TXT = (By.XPATH, "//h1[text()='Your cart is empty']")

    def verify_cart_message(self):
        actual_text = self.driver.find_element(*self.CART_TXT).text
        assert 'Your cart is empty' in actual_text, f'Expected "Your cart is empty" not in actual {actual_text}'
