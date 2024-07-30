from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.app.main_page.open()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product()


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()


@then('Verify header in shown')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_utilityHeaderContainer']")


@then('Verify header has {number} links')
def verify_header_links_amount(context, number):
    number = int(number)  # "6" => 6
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
    assert len(links) == number, f'Expected {number} links but got {len(links)}'



