from pages.header import Header
from pages.main_page import MainPage
from pages.base_page import Page
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.sign_in_page import SignInPage
from pages.target_app_page import TargetAppPage
from pages.privacy_policy_page import PrivacyPage
from pages.terms_and_conditions_page import TermsAndConditionsPage


class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)

        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.privacy_page = PrivacyPage(driver)
        self.terms_and_conditions_page = TermsAndConditionsPage(driver)
