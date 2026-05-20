from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_check_modal():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/modal-dialogs')

    # Находим обе кнопки
    small_modal_btn = driver.find_element(By.ID, 'showSmallModal')
    large_modal_btn = driver.find_element(By.ID, 'showLargeModal')

    # Проверяем Small modal
    small_modal_btn.click()
    time.sleep(1)
    assert driver.find_element(By.CLASS_NAME, 'modal-content').is_displayed()
    close_btn = driver.find_element(By.ID, 'closeSmallModal')
    close_btn.click()
    time.sleep(1)
    assert len(driver.find_elements(By.CLASS_NAME, 'modal-content')) == 0

    # Проверяем Large modal
    large_modal_btn.click()
    time.sleep(1)
    assert driver.find_element(By.CLASS_NAME, 'modal-content').is_displayed()
    close_btn = driver.find_element(By.ID, 'closeLargeModal')
    close_btn.click()
    time.sleep(1)
    assert len(driver.find_elements(By.CLASS_NAME, 'modal-content')) == 0

    driver.quit()