from selenium import webdriver
from pages.main_page import MainPage
from pages.elements_page import ElementsPage

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