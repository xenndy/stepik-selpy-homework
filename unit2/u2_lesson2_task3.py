#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://stepik.org/lesson/228249/step/8?unit=200781

# Задание: загрузка файла
# В этом задании в форме регистрации требуется загрузить текстовый файл

from selenium import webdriver
import os
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Заполнить текстовые поля: имя, фамилия, email
    browser.find_element_by_name("firstname").send_keys("Petr")
    browser.find_element_by_name("lastname").send_keys("Ivanov")
    browser.find_element_by_name("email").send_keys("somemail@mail.ru")

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'test_file.txt')
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    # Нажать кнопку "Submit"
    browser.find_element_by_class_name("btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    