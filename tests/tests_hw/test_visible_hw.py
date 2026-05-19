import time
import pytest
from selenium import webdriver
from pages.accordion import Accordion


def test_visible_accordion():
    driver = webdriver.Chrome()
    page = Accordion(driver)
    page.visit()

    # Проверяем, что текст виден
    assert page.get_visible_text_element().is_displayed() == True

    # Кликает по загаловку
    page.get_section1_heading().click()

    time.sleep(3)

    # Проверяем, что текст стал невидим
    assert page.get_visible_text_element().is_displayed() == False

    driver.quit()


def test_visible_accordion_default():
    driver = webdriver.Chrome()
    page = Accordion(driver)
    page.visit()

    # Проверяем, что все три элемента по умолчанию скрыты
    assert page.get_section2_first_paragraph().is_displayed() == False
    assert page.get_section2_second_paragraph().is_displayed() == False
    assert page.get_section3_paragraph().is_displayed() == False

    driver.quit()