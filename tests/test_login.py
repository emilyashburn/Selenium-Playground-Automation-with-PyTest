from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestLogin(BaseTest):

    def test_standard_user_login(self):
        login_page = LoginPage(self.driver)
        login_page.log_in_as_user("standard_user", "secret_sauce")
        actual_title = login_page.get_title_of_page()
        assert actual_title == "Swag Labs"
