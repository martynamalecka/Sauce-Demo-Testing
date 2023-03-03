from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage
from test_cases.helpers import Helpers
from utilities.read_properties import ReadConfig
import unittest


class TestSocialMediaButtons(unittest.TestCase):
    # get the base url and login credentials
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
        login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)

        # log in using standard_user credentials
        login_page.user_login(self.standard_user, self.valid_password)

        # get assertion and screenshot (if test failed) helper
        self.assertion_helper = Helpers(self.driver)

    # test social media buttons functionality

    def test_twitter_button(self):
        # click the Twitter button and get the actual website title
        self.inventory_page.click_twitter_button()
        actual_title = self.driver.title

        # the actual website title should match the expected title
        expected_title = "Swag Labs"
        condition = actual_title == expected_title
        screenshot_name = "test_twitter_button.png"
        self.assertion_helper.assert_and_take_screenshot_if_failed(
            condition, screenshot_name
        )

    def test_facebook_button(self):
        # click the Facebook button and get the actual website title
        self.inventory_page.click_facebook_button()
        actual_title = self.driver.title

        # the actual website title should match the expected title
        expected_title = "Swag Labs"
        condition = actual_title == expected_title
        screenshot_name = "test_facebook_button.png"
        self.assertion_helper.assert_and_take_screenshot_if_failed(
            condition, screenshot_name
        )

    def test_linkedin_button(self):
        # click the LinkedIn button and get the actual website title
        self.inventory_page.click_linkedin_button()
        actual_title = self.driver.title

        # the actual website title should match the expected title
        expected_title = "Swag Labs"
        condition = actual_title == expected_title
        screenshot_name = "test_linkedin_button.png"
        self.assertion_helper.assert_and_take_screenshot_if_failed(
            condition, screenshot_name
        )

    def tearDown(self) -> None:
        self.driver.quit()
