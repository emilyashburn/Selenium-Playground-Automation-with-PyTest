
class BasePage:
    """ The purpose of a BasePage is to contain methods common to all Pages"""
    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        self.driver.find_element(*locator).click()

    def click(self, locator):
        self.find(*locator).click()

    def set(self, locator, value):
        self.find(*locator).send_keys("")
        self.find(*locator).send_keys(value)
