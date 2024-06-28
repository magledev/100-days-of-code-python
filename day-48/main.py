from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

binaryPath = "/usr/bin/brave"
# binaryPath = "/usr/bin/brave-browser"
driverPath = "/usr/bin/chromedriver"

options = webdriver.ChromeOptions()
options.binary_location = binaryPath
driverService = Service(driverPath)
driver = webdriver.Chrome(service=driverService, options=options)

driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

for time in event_times:
    print(time.text)
for name in event_names:
    print(name.text)

events = {}
for n in range(len(event_times)):
    events[n] = {"time": event_times[n].text, "name": event_names[n].text}
print(events)

driver.close()
