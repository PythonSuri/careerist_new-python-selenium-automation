from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_BTN = (By.XPATH, "//div[@data-test='@web/CartIcon']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    ADDED_TO_CART_MSG = (By.XPATH, "//*[@data-test='modal-drawer-heading']//span[text()='Added to cart']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[aria-label='Account, sign in']")
    SIDE_NAV_SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def search_product(self, product):
        print('POM layer:', product)
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        # wait for the page with search results to load
        sleep(6)

    def click_add_to_cart(self):
        self.wait_and_click(*self.ADD_TO_CART_BTN)

    def side_nav_click_add_to_cart(self):
        self.wait_and_click(*self.SIDE_NAV_ADD_TO_CART_BTN)
        self.wait_for_element_appear(*self.ADDED_TO_CART_MSG)

    def store_product_name(self):
        self.wait_for_element_appear(*self.SIDE_NAV_PRODUCT_NAME)

    def click_cart_icon(self):
        self.wait_and_click(*self.CART_BTN)

    def click_sign_in_icon(self):
        self.wait_and_click(*self.SIGN_IN_BTN)

    def click_side_nav_icon(self):
        self.wait_and_click(*self.SIDE_NAV_SIGN_IN_BTN)



