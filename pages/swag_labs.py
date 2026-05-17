from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def exist_username(self):
        try:
            self.find_element(locator='#user-name')
        except NoSuchElementException:
            return False
        return True

    def exist_password(self):
        try:
            self.find_element(locator='#password')
        except NoSuchElementException:
            return False
        return True