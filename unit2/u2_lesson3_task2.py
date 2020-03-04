#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://stepik.org/lesson/184253/step/6?unit=158843
# Задание: переход на новую вкладку

# В этом задании после нажатия кнопки страница откроется в новой вкладке,
# нужно переключить WebDriver на новую вкладку и решить в ней задачу.

from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать кнопку
    browser.find_element_by_class_name("trollface").click()

    # Переключиться на новую вкладку
    wins = browser.window_handles  # (для себя - массив имён всех вкладок)
    print "windows:", wins
    new_window = browser.window_handles[1]
    print "new_window:", new_window
    browser.switch_to.window(new_window)

    # Пройти капчу для робота и получить число-ответ
    x_element = browser.find_element_by_css_selector("#input_value").text
    browser.find_element_by_css_selector("#answer").send_keys(calc(x_element))
    browser.find_element_by_class_name("btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    