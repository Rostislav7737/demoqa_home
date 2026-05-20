from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_webtables():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/webtables')
    wait = WebDriverWait(driver, 5)

    # Данные для новой записи
    first_name = 'Иван'
    last_name = 'Тестов'
    age = '30'
    email = 'ivan@test.com'
    salary = '50000'
    department = 'IT'

    # 1a. Нажимаем кнопку Add
    add_button = driver.find_element(By.ID, 'addNewRecordButton')
    add_button.click()

    # Ждём появления диалога
    time.sleep(1)

    # Проверка 1c: пустую форму нельзя сохранить
    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()
    time.sleep(1)
    # Диалог всё ещё открыт (проверяем, что форма существует)
    assert driver.find_element(By.CLASS_NAME, 'modal-content').is_displayed()

    # 1d. Заполняем все поля
    driver.find_element(By.ID, 'firstName').send_keys(first_name)
    driver.find_element(By.ID, 'lastName').send_keys(last_name)
    driver.find_element(By.ID, 'age').send_keys(age)
    driver.find_element(By.ID, 'userEmail').send_keys(email)
    driver.find_element(By.ID, 'salary').send_keys(salary)
    driver.find_element(By.ID, 'department').send_keys(department)

    # Нажимаем Submit
    submit_button.click()

    # 1d(i). Диалог закрылся
    time.sleep(1)
    assert len(driver.find_elements(By.CLASS_NAME, 'modal-content')) == 0

    # 1d(ii). В таблице появилась новая запись
    table_rows = driver.find_elements(By.CSS_SELECTOR, '.rt-tr-group')
    last_row = table_rows[-1]
    assert first_name in last_row.text
    assert last_name in last_row.text
    assert age in last_row.text
    assert email in last_row.text
    assert salary in last_row.text
    assert department in last_row.text

    # 1e. Кликаем на карандаш (Edit) у последней записи
    edit_buttons = driver.find_elements(By.CSS_SELECTOR, 'span[title="Edit"]')
    edit_buttons[-1].click()
    time.sleep(1)

    # Проверяем, что в диалоге наши данные
    assert driver.find_element(By.ID, 'firstName').get_attribute('value') == first_name

    # 1f. Меняем имя и сохраняем
    new_first_name = 'Петр'
    name_field = driver.find_element(By.ID, 'firstName')
    name_field.clear()
    name_field.send_keys(new_first_name)
    driver.find_element(By.ID, 'submit').click()
    time.sleep(1)

    # Проверяем, что в таблице имя обновилось
    last_row = driver.find_elements(By.CSS_SELECTOR, '.rt-tr-group')[-1]
    assert new_first_name in last_row.text
    assert first_name not in last_row.text

    # 1g. Удаляем запись (корзина)
    delete_buttons = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
    delete_buttons[-1].click()
    time.sleep(1)

    # Проверяем, что запись удалена
    table_rows_after = driver.find_elements(By.CSS_SELECTOR, '.rt-tr-group')
    assert new_first_name not in table_rows_after[-1].text

    driver.quit()