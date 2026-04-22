from functools import reduce
import math

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import os 

cur_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(cur_dir, 'file.txt')

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    
    inputs = [
        browser.find_element(By.NAME, "firstname"),
        browser.find_element(By.NAME, "lastname"),
        browser.find_element(By.NAME, "email")
    ]
    
    for inp in inputs:
        inp.send_keys("test")
    
    file_el = browser.find_element(By.ID, "file")
    file_el.send_keys(file_path)
    
    btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    btn.click()    

finally:
    time.sleep(5)
    browser.quit()
