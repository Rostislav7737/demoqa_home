import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from components.base_component import BaseComponent

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://demoqa.com/'

    def visit(self):
        self.driver.get(self.base_url)

    def get_footer_text(self):
        footer = BaseComponent(self.driver, 'footer')
        return footer.get_text()

    def click_elements_button(self):
        button = self.driver.find_element(By.CSS_SELECTOR, '.card-body > h5:first-child')
        button.click()

class ElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://demoqa.com/elements'

    def get_center_text(self):
        center_text = BaseComponent(self.driver, '.main-header')
        return center_text.get_text()

def test_footer_text():
    driver = webdriver.Chrome()
    page = MainPage(driver)
    page.visit()
    footer_text = page.get_footer_text()
    expected_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    assert footer_text == expected_text
    driver.quit()

def test_center_text_on_elements_page():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.visit()
    main_page.click_elements_button()
    elements_page = ElementsPage(driver)
    center_text = elements_page.get_center_text()
    expected_text = 'Please select an item from left to start practice.'
    assert center_text == expected_text
    driver.quit()