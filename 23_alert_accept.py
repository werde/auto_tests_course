from functools import reduce
import math

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    
    btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    btn.click()
    time.sleep(1)
    
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)
    
    x = int(browser.find_element(By.ID, "input_value").text)
    val = str(math.log(abs(12*math.sin(int(x)))))
    
    browser.find_element(By.ID, "answer").send_keys(val)
    
    btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    btn.click()
    

finally:
    time.sleep(5)
    browser.quit()
