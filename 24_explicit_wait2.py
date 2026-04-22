from functools import reduce
import math

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/explicit_wait2.html"

def value_lesser_than(locator, threshold):

    def _predicate(driver):

        text = driver.find_element(*locator).text

        try:
            b = int(text[1:]) <= threshold
            print(b)
            return b
        except:
            return False

    return _predicate

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    

    
    WebDriverWait(browser, 12).until(
        value_lesser_than((By.ID, "price"), 100)
    )
    #time.sleep(1)

    btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    btn.click()
    
    x = int(browser.find_element(By.ID, "input_value").text)
    val = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(By.ID, "answer").send_keys(val)
    
    btn = browser.find_element(By.ID, "solve")
    btn.click()


finally:
    time.sleep(5)
    browser.quit()
