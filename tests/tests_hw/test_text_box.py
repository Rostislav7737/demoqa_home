from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_text_box():
    # Открываем браузер
    driver = webdriver.Chrome()

    # Переходим на страницу
    driver.get('https://demoqa.com/text-box')

    # Сохраняем текст в переменные
    full_name_text = 'Иван Петров'
    current_address_text = 'Москва, ул. Тестерная, д.1'

    # Находим поле Full Name и вводим текст
    full_name = driver.find_element(By.ID, 'userName')
    full_name.send_keys(full_name_text)

    # Находим поле Current Address и вводим текст
    current_address = driver.find_element(By.ID, 'currentAddress')
    current_address.send_keys(current_address_text)

    # Нажимаем кнопку Submit
    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()

    # Ждём появления результата
    time.sleep(2)

    # Находим элементы с результатом
    output_name = driver.find_element(By.ID, 'name')
    output_address = driver.find_element(By.ID, 'currentAddress')

    # Проверяем, что текст из переменной есть в результате
    assert full_name_text in output_name.text
    assert current_address_text in output_address.text

    # Закрываем браузер
    driver.quit()