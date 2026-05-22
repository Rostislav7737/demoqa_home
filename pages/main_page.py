from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from components.base_component import BaseComponent

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'https://demoqa.com/'

    def get_footer_text(self):
        footer = BaseComponent(self.driver, 'footer')
        return footer.get_text()

    def click_elements_button(self):
        button = self.driver.find_element(By.CSS_SELECTOR, '.card-body > h5:first-child')
        button.click()