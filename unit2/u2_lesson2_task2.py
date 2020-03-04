#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://stepik.org/lesson/228249/step/6?unit=200781
# Задание на execute_script

from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    x_element = browser.find_element_by_css_selector("#input_value").text
    print
    print "x =", x_element

    # Посчитать математическую функцию от x
    y = calc(x_element)
    print"y =", y

    # Ввести ответ в текстовое поле
    browser.find_element_by_css_selector("#answer").send_keys(y)

    # Проскроллить страницу вниз.
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Выбрать checkbox "I'm the robot".
    browser.find_element_by_id("robotCheckbox").click()

    # Переключить radiobutton "Robots rule!".
    browser.find_element_by_id("robotsRule").click()

    # Нажать на кнопку "Submit".
    browser.find_element_by_class_name("btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    