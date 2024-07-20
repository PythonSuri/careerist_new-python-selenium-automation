from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    # find the search field and enter a text
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # click search
    context.driver.find_element(By.XPATH,"//button[@data-test='@web/Search/SearchButton']").click()
    # wait for the page with search results to load
    sleep(6)


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


