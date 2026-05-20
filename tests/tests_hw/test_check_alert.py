from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_check_alert():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/alerts')

    # Кнопка с таймером
    timer_btn = driver.find_element(By.ID, 'timerAlertButton')
    timer_btn.click()

    # Ждём появления алерта (до 6 секунд)
    alert = WebDriverWait(driver, 6).until(EC.alert_is_present())

    # Принимаем алерт
    alert.accept()

    driver.quit()