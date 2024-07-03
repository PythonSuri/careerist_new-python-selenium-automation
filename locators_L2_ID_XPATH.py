from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

sleep(6)

# find by ID
driver.find_element(By.ID,'twotabsearchtextbox')
driver.find_element(By.ID,'nav-logo-sprites')


# find by XPATH
driver.find_element(By.XPATH,"//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH,"//input[@placeholder='Search Amazon']")

# find by attribute only
driver.find_element(By.XPATH,"//*[@aria-label='Search Amazon']")

# find by multiple attributes
driver.find_element(By.XPATH,"//input[@tabindex='0' and @type='text' and @dir='auto']")
driver.find_element(By.XPATH,"//input[@tabindex='0' and @type='text']")

# Workshop training
driver.find_element(By.ID,'searchDropdownBox')
driver.find_element(By.XPATH,"//*[@aria-describedby='searchDropdownDescription']")

# find by text() *if no other languages on web page)
driver.find_element(By.XPATH,"//a[text()='Best Sellers']")

# find by text() and attributes
driver.find_element(By.XPATH,"//a[@class='nav-a  ' and text()='Best Sellers']")

# connecting to parent node
# on web page $x("//div[@id='nav-xshop']//a[text()='Best Sellers']")
driver.find_element(By.XPATH,"//div[@id='nav-xshop']//a[text()='Best Sellers']")

# contains()
# on web page $x("//div[@id='nav-xshop']//a[contains(text(),'Best')]")
# on web page $x("//h2[contains(text(),'under $30')]")
driver.find_element(By.XPATH,"//div[@id='nav-xshop']//a[contains(text(),'Best')]")
driver.find_element(By.XPATH,"//h2[contains(text(),'under $30')]")

sleep(9)
# exit browser
#driver.quit()

