#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_basket_link_on_the_main_page(browser):
    browser.get(link)
    basket_btn = browser.find_element_by_css_selector(".btn-add-to-basket")
    print("\n****************")
    print(basket_btn.text)
    assert basket_btn.text != "", "Should be 'Add to busket' button"

