#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://stepik.org/lesson/165493/step/5?unit=140087
# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)

from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    print
    print "x =", x

    # Посчитать математическую функцию от x
    y = calc(x)
    print"y =", y

    # Ввести ответ в текстовое поле
    browser.find_element_by_css_selector("#answer").send_keys(y)

    # Отметить checkbox "Подтверждаю, что являюсь роботом"
    browser.find_element_by_css_selector('[for="robotCheckbox"]').click()

    # Выбрать radiobutton "Роботы рулят!"
    browser.find_element_by_id("robotsRule").click()

    # Нажать на кнопку Отправить
    browser.find_element_by_class_name("btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    