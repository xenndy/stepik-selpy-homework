#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://stepik.org/lesson/181384/step/8?unit=156009
# Задание: ждем нужный текст на странице

# Попробуем теперь написать программу, 
# которая будет бронировать нам дом для отдыха по строго заданной цене.
# Более высокая цена нас не устраивает, 
# а по более низкой цене объект успеет забронировать кто-то другой.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Нажать на кнопку "Book"
    browser.find_element_by_id("book").click()

    # Пройти капчу для робота и получить число-ответ
    x_element = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(calc(x_element))
    browser.find_element_by_id("solve").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    