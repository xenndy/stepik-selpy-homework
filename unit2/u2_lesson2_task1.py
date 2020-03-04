#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# https://stepik.org/lesson/228249/step/3?unit=200781
# Задание: работа с выпадающим списком

try:
    link = "http://suninjuly.github.io/selects1.html"
    # link = "http://suninjuly.github.io/selects2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитать сумму заданных чисел
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    summa = int(num1) + int(num2)
    print
    print "summa =", summa
    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summa))

    # Нажать кнопку "Отправить"
    browser.find_element_by_class_name("btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    