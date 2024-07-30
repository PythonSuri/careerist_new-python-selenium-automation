from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_BTN = (By.XPATH, "//div[@data-test='@web/CartIcon']")

    def search_product(self):
        self.input_text('coffee', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        # wait for the page with search results to load
        sleep(6)

    def click_cart_icon(self):
        self.click(*self.CART_BTN)