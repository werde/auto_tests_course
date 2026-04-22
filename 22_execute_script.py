from functools import reduce
import math

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    
    x = int(browser.find_element(By.ID, "input_value").text)
    val = math.log(abs(12*math.sin(int(x))))
    
    input_el = browser.find_element(By.ID, "answer")
    input_el.send_keys(str(val))
    
    check_el = browser.find_element(By.ID, "robotCheckbox")
    check_el.click()
    
    radio_el = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_el)
    radio_el.click()
    
    btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()    

finally:
    time.sleep(5)
    browser.quit()
