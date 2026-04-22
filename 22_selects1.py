from functools import reduce
import math

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    
    val = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)
    
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(val))


    btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    btn.click()    

finally:
    time.sleep(5)
    browser.quit()
