from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time 
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))
    price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()
   

    num_el = browser.find_element(By.ID, 'input_value').text
    num = int(num_el)
    x = calc(num)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(x)
    button2 = browser.find_element(By.ID, "solve")
    button2.click()
finally:
    time.sleep(5)
    browser.quit()
