import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage
from test_cases.helpers import Helpers
from utilities.read_properties import ReadConfig


class TestDropdownMenu(unittest.TestCase):
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

        # perform a successful login and open a dropdown menu
        self.login_page.user_login(self.standard_user, self.valid_password)
        self.inventory_page.click_dropdown_menu()

        # get assertion and screenshot (if test failed) helper
        self.assertion_helper = Helpers(self.driver)

    # test dropdown menu functionality

    def test_dropdown_menu_elements_displayed(self):
        # dropdown menu should be opened and all elements visible
        condition = self.inventory_page.is_dropdown_menu_visible()
        screenshot_name = "test_dropdown_menu_elements_displayed.png"
        self.assertion_helper.assert_and_take_screenshot_if_failed(
            condition, screenshot_name
        )

    def test_dropdown_menu_close_button(self):
        # close the dropdown menu by clicking 'X' button
        self.inventory_page.click_dropdown_menu_close_button()

        # dropdown menu should be closed - not visible
        condition = self.inventory_page.is_dropdown_menu_visible()
        screenshot_name = "test_dropdown_menu_close_button.png"
        self.assertion_helper.assert_and_take_screenshot_if_failed(
            not condition, screenshot_name
        )

    def tearDown(self) -> None:
        self.driver.quit()
