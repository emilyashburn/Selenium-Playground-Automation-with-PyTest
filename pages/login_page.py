from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def get_title_of_page(self, driver):
        return driver.find_element(By.CLASS_NAME, 'app_logo')

    def set_username(self, username):
        self.set(self.username_field, username)

    def set_password(self, password):
        self.set(self.password_field, password)

    def click_login_button(self):
        self.click(self.login_button)

    def log_in_as_user(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()
