from pages.base_page import BasePage
from components.base_component import BaseComponent

class ElementsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'https://demoqa.com/elements'

    def get_center_text(self):
        center_text = BaseComponent(self.driver, '.main-header')
        return center_text.get_text()