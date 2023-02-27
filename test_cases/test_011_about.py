from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test_cases.helpers import Helpers


class TestAbout(unittest.TestCase):
    base_url = ReadConfig.get_base_url()
    standard_user = ReadConfig.get_standard_user()
    valid_password = ReadConfig.get_valid_password()

    # test About functionality

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

    def test_about(self):
        # open a dropdown menu and go to About
        self.inventory_page.click_dropdown_menu()
        self.inventory_page.click_about()

        # the website title should match the expected title
        actual_title = self.driver.title
        expected_title = (
            "Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing"
        )
        condition = actual_title == expected_title
        screenshot_name = "test_about.png"
        self.assertion_helper.assert_and_take_screenshot_if_failed(
            condition, screenshot_name
        )

    def tearDown(self) -> None:
        self.driver.quit()
