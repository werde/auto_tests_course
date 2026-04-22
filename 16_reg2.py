from functools import reduce
import math

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    time.sleep(1)
    
    inputs = [
        browser.find_element(By.CSS_SELECTOR, ".first_block div:nth-child(1) input"),
        browser.find_element(By.CSS_SELECTOR, ".first_block div:nth-child(2) input"),
        browser.find_element(By.CSS_SELECTOR, ".first_block div:nth-child(3) input"),
        browser.find_element(By.CSS_SELECTOR, ".second_block div:nth-child(1) input"),
        browser.find_element(By.CSS_SELECTOR, ".second_block div:nth-child(2) input")
    ]
    
    btn = browser.find_element(By.XPATH, "//button[text()='Submit']")
    
    for idx, inpt in enumerate(inputs):
        inpt.send_keys("Test" + str(idx))
        
    btn.click()

finally:
    time.sleep(5)
    browser.quit()
