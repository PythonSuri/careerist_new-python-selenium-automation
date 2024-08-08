from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep

SEARCH_BAR = (By.CSS_SELECTOR, "[placeholder='search help'][type='text']")
SEARCH_HLP_BTN = (By.XPATH, "//*[@alt='search']")
SEARCH_RETURNS_TXT = (By.XPATH, "//h2[@class='searchResultHead']")


@given('Open target help page')
def open_help_page(context):
    context.app.help_page.open()


@given('Open Help page for Returns')
def click_cart(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic {option}')
def select_topic(context, option):
    context.app.help_page.select_topic(option)


@when('Text {question} in search bar')
def text_in_search_bar(context, question):
    context.driver.find_element(*SEARCH_BAR).send_keys(question)
    context.driver.find_element(*SEARCH_HLP_BTN).click()
    context.driver.wait.until(EC.presence_of_all_elements_located(SEARCH_RETURNS_TXT))


@then('Verify Target Help title')
def verify_target_help_title(context):
    context.app.help_page.verify_target_help_title()


@then('Verify help {expected_text} page opened')
def verify_help_page_header(context, expected_text):
    context.app.help_page.verify_header(expected_text)

#
# @then('Verify help Current promotions page opened')
# def verify_help_page_header_promotions(context):
#     context.app.help_page.verify_promotions()


@then('Verify search returns {relevant_result}')
def verify_search_returns(context, relevant_result):
    context.app.help_page.verify_search_returns(relevant_result)


@then('Verify page displays {number} help boxes')
def verify_boxes_number(context, number):
    number = int(number)
    help_boxes = context.driver.find_elements(By.CSS_SELECTOR, "[class='grid_6']")
    assert len(help_boxes) == number, f'Expected {number} help boxes but got {len(help_boxes)}'


@then('Verify page shows {number} info cells')
def verify_info_cells_number(context, number):
    number = int(number)
    info_cells = context.driver.find_elements(By.CSS_SELECTOR, "[class='custom-h3']")
    assert len(info_cells) == number, f'Expected {number} info cells but got {len(info_cells)}'

