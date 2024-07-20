from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open target circle page')
def open_circle_page(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9/')


@then('Verify circle logo in shown')
def verify_circle_logo(context):
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label='Target circle TM']")

@then('Verify page displays {number} benefit cells')
def verify_cells_number(context, number):
    number = int(number)  # "10" => 10
    benefit_cells = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")
    assert len(benefit_cells) == number, f'Expected {number} benefit cells but got {len(benefit_cells)}'

