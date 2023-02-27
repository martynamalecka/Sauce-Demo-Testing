import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage
from test_cases.helpers import Helpers
from utilities.read_properties import ReadConfig


class TestFooter(unittest.TestCase):
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

        # perform a successful login
        self.login_page.user_login(self.standard_user, self.valid_password)

        # get assertion and screenshot (if test failed) helper
        self.assertion_helper = Helpers(self.driver)

    def test_footer_content(self):
        # the actual footer data should match the expected data
        actual_footer_text = self.inventory_page.get_footer_text()
        expected_footer_text = (
            "© 2023 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
        )
        condition = actual_footer_text == expected_footer_text
        screenshot_name = "test_footer_content.png"
        self.assertion_helper.assert_and_take_screenshot_if_failed(
            condition, screenshot_name
        )

    def tearDown(self) -> None:
        self.driver.quit()
