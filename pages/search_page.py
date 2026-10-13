from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    TITLE_LABEL = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url="https://www.saucedemo.com/"):
        self.driver.get(url)

    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
