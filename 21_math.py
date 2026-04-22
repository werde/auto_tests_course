from functools import reduce
import math

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    
    x = int(browser.find_element(By.ID, "treasure").get_attribute("valuex"))
    val = math.log(abs(12*math.sin(int(x))))
    
    input_el = browser.find_element(By.ID, "answer")
    input_el.send_keys(str(val))
    
    check_el = browser.find_element(By.ID, "robotCheckbox")
    check_el.click()
    
    radio_el = browser.find_element(By.ID, "robotsRule")
    radio_el.click()
    
    btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    btn.click()    

finally:
    time.sleep(5)
    browser.quit()
