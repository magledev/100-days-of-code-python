from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

FB_USERNAME = os.environ["FB_USERNAME"]
FB_PASSWORD = os.environ["FB_PASSWORD"]


# binaryPath = "/usr/bin/brave"
binaryPath = "/usr/bin/brave-browser"
driverPath = "/usr/bin/chromedriver"

options = webdriver.ChromeOptions()
options.binary_location = binaryPath
driverService = Service(driverPath)
driver = webdriver.Chrome(service=driverService, options=options)

driver.get("https://tinder.com/")
main_window = driver.current_window_handle

# Accept privacy and cookie permissions
time.sleep(3)
decline_button = driver.find_element(By.XPATH, '//*[@id="u-1650273590"]/div/div[2]/div/div/div[1]/div[2]/button')
decline_button.click()

# Login
time.sleep(3)
login_button = driver.find_element(By.XPATH, '//*[@id="u-1650273590"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()

# Login with Facebook
time.sleep(3)
fb_sso_button = driver.find_element(By.XPATH, '//*[@id="u916312630"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
fb_sso_button.click()

print(len(driver.window_handles))
# for handle in driver.window_handles:
#     if handle != main_page:
#         login_page = handle
#         driver.switch_to.window(login_page)

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

# Accept Facebook privacy options
time.sleep(6)
fb_privacy = driver.find_element(By.XPATH, '//*[text()="Allow essential and optional cookies"]')
fb_privacy.click()

# Login to Facebook
time.sleep(5)
fb_user = driver.find_element(By.XPATH, '//*[@id="email"]')
fb_user.send_keys(FB_USERNAME)
time.sleep(5)
fb_pass = driver.find_element(By.XPATH, '//*[@id="pass"]')
fb_pass.send_keys(FB_PASSWORD)
time.sleep(5)
fb_login = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
fb_login.click()

# Switch back to main window and then accept location and notification permissions pop-ups
time.sleep(15)
driver.switch_to.window(main_window)
allow_location = driver.find_element(By.XPATH, '//*[@id="u916312630"]/div/div/div/div/div[3]/button[1]')
allow_location.click()
deny_notifications = driver.find_element(By.XPATH, '//*[@id="u916312630"]/div/div/div/div/div[3]/button[2]')
deny_notifications.click()

time.sleep(6)

# Swipe left on several match suggestions to complete exercise
for n in range(20):
    try:
        ActionChains(driver).send_keys(Keys.ARROW_LEFT).perform()
        time.sleep(1)

    except ElementClickInterceptedException:
        try:
            # match found
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a").click()

        except NoSuchElementException:
            time.sleep(2)

driver.quit()
