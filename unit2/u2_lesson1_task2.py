#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://stepik.org/lesson/165493/step/7?unit=140087

# В данной задаче вам нужно с помощью роботов решить 
# ту же математическую задачу, как и в прошлом задании. 
# Но теперь значение переменной х спрятано в "сундуке", 
# точнее, значение хранится в атрибуте valuex у картинки 
# с изображением сундука.

from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти элемент-картинку, который является изображением сундука с сокровищами
    chest = browser.find_element_by_id("treasure")
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи
    x_element = chest.get_attribute("valuex")
    print "x_element =", x_element

    # Посчитать математическую функцию от x
    y = calc(int(x_element))
    print"y =", y

    # Ввести ответ в текстовое поле
    browser.find_element_by_css_selector("#answer").send_keys(y)

    # Отметить checkbox "Подтверждаю, что являюсь роботом"
    browser.find_element_by_id("robotCheckbox").click()

    # Выбрать radiobutton "Роботы рулят!"
    browser.find_element_by_id("robotsRule").click()

    # Нажать на кнопку Отправить
    browser.find_element_by_class_name("btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

