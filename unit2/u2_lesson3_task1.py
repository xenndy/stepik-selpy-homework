#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://stepik.org/lesson/184253/step/4?unit=158843
# Задание: принимаем alert

from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать кнопку
    browser.find_element_by_class_name("btn").click()

    # Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    
    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element_by_css_selector("#input_value").text
    y = calc(x_element)    
    browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_class_name("btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    