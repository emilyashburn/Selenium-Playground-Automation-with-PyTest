import time
from pages.login_page import HomePage

from selenium.webdriver.common.by import By


class TestClass:

    def test_open_app_and_click(self):
        print('in test')
        time.sleep(5)
        assert True

    def test_other_thing(self):
        print('second test woop woop')
        time.sleep(4)
        assert True
