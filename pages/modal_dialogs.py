from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ModalDialogs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'https://demoqa.com/modal-dialogs'

    # Все кнопки подменю (один локатор для всех)
    def get_menu_buttons(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '.element-group .btn')

    # Иконка для перехода на главную
    def get_logo_icon(self):
        return self.find_element('.header-logo')