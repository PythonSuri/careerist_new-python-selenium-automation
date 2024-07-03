from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.refresh()

#----------------------------------------------------------------------------------------------------------------------

# 1. Open https://www.target.com/
driver.get('https://www.target.com')

driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()

sleep(2)

expected_text = 'Your cart is empty'
sleep(2)
actual_text = driver.find_element(By.XPATH,"//h1[text()='Your cart is empty']").text
print(actual_text)

assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
print('Test case passed')

sleep(2)
