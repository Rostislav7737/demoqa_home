from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_form_validate():
    # Открываем браузер
    driver = webdriver.Chrome()

    # Переходим на страницу
    driver.get('https://demoqa.com/automation-practice-form')

    # Проверяем плейсхолдер у first_name
    first_name = driver.find_element(By.ID, 'firstName')
    assert first_name.get_attribute('placeholder') == 'First Name'

    # Проверяем плейсхолдер у last_name
    last_name = driver.find_element(By.ID, 'lastName')
    assert last_name.get_attribute('placeholder') == 'Last Name'

    # Проверяем плейсхолдер у user_email
    user_email = driver.find_element(By.ID, 'userEmail')
    assert user_email.get_attribute('placeholder') == 'name@example.com'

    # Проверяем наличие атрибута pattern у user_email
    assert user_email.get_attribute('pattern') is not None

    # Нажимаем кнопку Submit (пустая форма)
    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()

    # Находим форму и проверяем класс "was-validated"
    form = driver.find_element(By.TAG_NAME, 'form')
    assert 'was-validated' in form.get_attribute('class')

    # Закрываем браузер
    driver.quit()
