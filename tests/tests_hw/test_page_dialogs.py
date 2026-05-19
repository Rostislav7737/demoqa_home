import time
import pytest
from selenium import webdriver
from pages.modal_dialogs import ModalDialogs

def test_modal_elements():
    driver = webdriver.Chrome()
    page = ModalDialogs(driver)
    page.visit()

    # Проверяем, что кнопок подменю 5 штук
    buttons = page.get_menu_buttons()
    assert len(buttons) == 5

    driver.quit()

def test_navigation_modal():
    driver = webdriver.Chrome()
    page = ModalDialogs(driver)
    page.visit()

    # Обновляем страницу
    driver.refresh()

    # Переходим на главную через иконку
    page.get_logo_icon().click()
    time.sleep(1)

    # Шаг назад стрелкой браузера
    driver.back()
    time.sleep(1)

    # Устанавливаю размер экрана 900х400
    driver.set_window_size(900, 400)
    time.sleep(1)

    # Делаю шаг вперед стрелкой браузера
    driver.forward()
    time.sleep(1)

    # Проверяем URL на главной странице
    assert driver.current_url == 'https://demoqa.com/'

    # Проверяем title на главной
    assert driver.title == 'DEMOQA'

    # Возвращение размеров
    driver.set_window_size(1000, 1000)

    driver.quit()