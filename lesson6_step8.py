from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
    input1.send_keys("Rabbit")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
    input2.send_keys("Holmes")
    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
    input3.send_keys("dsds@gmail.com")
    input4 = browser.find_element(By.CSS_SELECTOR, "div.second_block input.first")
    input4.send_keys("+89676597548")
    input5 = browser.find_element(By.CSS_SELECTOR, "div.second_block input.second")
    input5.send_keys("Moscow")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла