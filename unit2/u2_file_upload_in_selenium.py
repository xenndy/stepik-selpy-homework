#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (https://stepik.org/lesson/228249/step/7?unit=200781)
# Пример кода, который позволяет указать путь к файлу 'file.txt', 
# находящемуся в той же папке, что и скрипт, который вы запускаете

import os 
from selenium import webdriver

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
# element.send_keys(file_path)
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
print file_path
