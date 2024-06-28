import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# binaryPath = "/usr/bin/brave"
binaryPath = "/usr/bin/brave-browser"
driverPath = "/usr/bin/chromedriver"

options = webdriver.ChromeOptions()
options.binary_location = binaryPath
driverService = Service(driverPath)
driver = webdriver.Chrome(service=driverService, options=options)

# # Speed test function
# driver.get('https://speedtest.net')
#
# # Accept privacy popup
# time.sleep(2)
# driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
#
# # # Start speed test and check for completion
# driver.find_element(By.CLASS_NAME, 'start-text').click()
# test_in_progress = True
# while test_in_progress:
#     test_finished = driver.find_element(By.CSS_SELECTOR, '.overall-progress').text
#     if test_finished.startswith('Your speed test has completed'):
#         break
#
# # Fetch results
# dl_speed = driver.find_element(By.CSS_SELECTOR, '.download-speed').text
# ul_speed = driver.find_element(By.CSS_SELECTOR, '.upload-speed').text
# print(f"My internet speeds are:\nDOWNLOAD: {dl_speed} Mbps\nUPLOAD: {ul_speed} Mbps")


# Twitter post function
driver.get("https://twitter.com/home")
time.sleep(3)
username_input = driver.find_element(
    By.CSS_SELECTOR, 'input[autocomplete="username"]'
).send_keys("<email_address>")
confirm_username = driver.find_element(
    By.XPATH,
    '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]',
).click()
time.sleep(4)
password_input = driver.find_element(
    By.CSS_SELECTOR, 'input[name="password"]'
).send_keys("")
confirm_username = driver.find_element(
    By.XPATH,
    '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div',
).click()


# driver.find_element(By.CSS_SELECTOR, '.public-DraftEditor-content').send_keys('Test')

# driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Tweet"]').click()
