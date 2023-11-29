from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    num_el = browser.find_element(By.ID, 'input_value').text
    num = int(num_el)
    x = calc(num)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(x)
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button2.click()
finally:
    time.sleep(5)
    browser.quit()
