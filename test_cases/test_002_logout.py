import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage
from test_cases.helpers import Helpers
from utilities.read_properties import ReadConfig


class TestLogout(unittest.TestCase):
    base_url = ReadConfig.get_base_url()
    standard_user = ReadConfig.get_standard_user()
    valid_password = ReadConfig.get_valid_password()

    def setUp(self) -> None:
        # get the driver and open the browser
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.base_url)

        # create page objects for further testing
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)

        # perform a successful login and click logout
        self.login_page.user_login(self.standard_user, self.valid_password)
        self.inventory_page.click_logout()

        # get assertion and screenshot (if test failed) helper
        self.assertion_helper = Helpers(self.driver)

    # test logout functionality

    def test_logout(self):
        # the actual header value should match the expected value
        actual_logout_confirmation = self.login_page.get_logout_confirmation()
        expected_logout_confirmation = "Accepted usernames are:"
        condition = actual_logout_confirmation == expected_logout_confirmation
        screenshot_name = "test_logout.png"
        self.assertion_helper.assert_and_take_screenshot_if_failed(
            condition, screenshot_name
        )

    def test_browse_back_logout(self):
        # browse back, user should be logged out
        self.driver.execute_script("window.history.go(-1)")

        # the actual error message value should match the expected error message
        actual_logout_confirmation = self.login_page.get_login_error_message()
        expected_logout_confirmation = "Epic sadface: You can only access '/inventory.html' when you are logged in."
        condition = actual_logout_confirmation == expected_logout_confirmation
        screenshot_name = "test_browse_back_logout.png"
        self.assertion_helper.assert_and_take_screenshot_if_failed(
            condition, screenshot_name
        )

    def tearDown(self) -> None:
        self.driver.quit()
