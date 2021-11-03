import os
from time import time, sleep
from selenium import webdriver


os.system("chmod +x geckodriver")

options = webdriver.FirefoxOptions()
#profile = webdriver.FirefoxProfile()
driver_path = 'geckodriver'
browser= webdriver.Firefox(options=options, executable_path=driver_path)
browser.get("https://www.google.com/")
print("CURRENT URL:", browser.current_url
