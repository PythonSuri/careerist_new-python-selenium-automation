from selenium.webdriver.common.by import By

from pages.base_page import Page


class ReturnsPage(Page):
    def verify_rtn_url(self):
        self.verify_partial_url('/Returns')