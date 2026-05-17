import pytest
from selenium import webdriver
from pages.swag_labs import SwagLabs

def test_check_icon():
    driver = webdriver.Chrome()
    swag = SwagLabs(driver)
    swag.visit()
    assert swag.exist_icon() == True
    driver.quit()

def test_check_username_field():
    driver = webdriver.Chrome()
    swag = SwagLabs(driver)
    swag.visit()
    assert swag.exist_username() == True
    driver.quit()

def test_check_password_field():
    driver = webdriver.Chrome()
    swag = SwagLabs(driver)
    swag.visit()
    assert swag.exist_password() == True
    driver.quit()