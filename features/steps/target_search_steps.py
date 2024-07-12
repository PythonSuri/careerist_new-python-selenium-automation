from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for product')
def open_target(context):
    # find the search field and enter a text
    context.driver.find_element(By.ID, 'search').send_keys('coffee')
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # wait for the page with search results to load
    sleep(4)


@then('Verify search worked')
def verify_search_results(context):
    expected_text = 'coffee'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
    sleep(4)


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    sleep(4)


@then('Verify Your cart is empty message is shown')
def verify_cart_message(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
    sleep(4)


@when('Click on Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
    sleep(4)


@when('From right side navigation menu click Sign In')
def click_side_nav(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(4)


@then('Verify Sign In form opened')
def verify_signin_form(context):
    expected_text = 'Sign into your Target account'
    #actual_text = context.driver.find_element(By.XPATH, "//span").text
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
    sleep(3)

