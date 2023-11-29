from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time 
import os 


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys('Denis')
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys('ZHorov')
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys('zhrovda@gmail.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    fileupload = browser.find_element(By.ID, "file")
    fileupload.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()
