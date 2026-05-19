from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Accordion(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'https://demoqa.com/accordian'

    # Элемент с текстом (видимый по умолчанию)
    def get_visible_text_element(self):
        return self.find_element('#section1Content > p')

    # Заголовок первой секции для клика
    def get_section1_heading(self):
        return self.find_element('#section1Heading')

    # Элемент для проверки скрытости во втором тесте
    def get_section2_first_paragraph(self):
        return self.find_element('#section2Content > p:nth-child(1)')

    def get_section2_second_paragraph(self):
        return self.find_element('#section2Content > p:nth-child(2)')

    def get_section3_paragraph(self):
        return self.find_element('#section3Content > p')
