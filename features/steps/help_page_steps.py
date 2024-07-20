from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target help page')
def open_help_page(context):
    context.driver.get('https://help.target.com/help/')


@then('Verify Target Help title')
def verify_target_help_title(context):
    context.driver.find_element(By.XPATH, "//h2[contains(text(),'Target Help')]")


@when('Text {question} in search bar')
def text_in_search_bar(context, question):
    context.driver.find_element(By.CSS_SELECTOR, "[class='search-input']").send_keys(question)
    context.driver.find_element(By.XPATH, "//*[@alt='search']").click()
    sleep(4)


@then('Verify search returns {relevant_result}')
def verify_search_returns(context, relevant_result):
    actual_text = context.driver.find_element(By.XPATH, "//div[@id='cContainerId_info']").text
    assert relevant_result in actual_text, f'Expected {relevant_result} is not in actual {actual_text}'
    sleep(4)


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
