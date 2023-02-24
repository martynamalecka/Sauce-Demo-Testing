from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from page_objects.login_page import LoginPage
from page_objects.inventory_page import InventoryPage
import unittest
from test_cases.helpers import Helpers
from utilities.read_properties import ReadConfig


class TestLogin(unittest.TestCase):

    base_url = ReadConfig.get_base_url()
    standard_user = ReadConfig.get_standard_user()
    locked_out_user = ReadConfig.get_locked_out_user()
    problem_user = ReadConfig.get_problem_user()
    performance_glitch_user = ReadConfig.performance_glitch_user()
    invalid_user = ReadConfig.invalid_user()
    valid_password = ReadConfig.get_valid_password()
    invalid_password = ReadConfig.get_invalid_password()

    def setUp(self) -> None:

        # get the driver and open the browser
        options = Options()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.base_url)

        # create page objects for further testing
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)

        # TODO
        self.assertion_helper = Helpers(self.driver)

    # test login functionality

    def test_standard_user_login(self):

        # login with valid credentials
        self.login_page.user_login(self.standard_user, self.valid_password)

        # check if the actual header value matched the expected value
        actual_header = self.inventory_page.get_header_text()
        expected_header = 'PRODUCTS'
        condition = actual_header == expected_header
        screenshot_name = 'test_standard_user_login.png'
        self.assertion_helper.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def test_problem_user_login(self):

        # login with problem user credentials
        self.login_page.user_login(self.problem_user, self.valid_password)

        # the actual header value should match the expected value
        actual_header = self.inventory_page.get_header_text()
        expected_header = 'PRODUCTS'
        condition = actual_header == expected_header
        screenshot_name = 'test_problem_user_login.png'
        self.assertion_helper.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def test_performance_glitch_user_login(self):

        # login with performance glitch user credentials
        self.login_page.user_login(self.performance_glitch_user, self.valid_password)

        # the actual header value should match the expected value
        actual_header = self.inventory_page.get_header_text()
        expected_header = 'PRODUCTS'
        condition = actual_header == expected_header
        screenshot_name = 'test_performance_glitch_user_login.png'
        self.assertion_helper.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def test_locked_out_user_login(self):

        # login with locked out user credentials
        self.login_page.user_login(self.locked_out_user, self.valid_password)

        # the actual header value should match the expected value
        actual_header = self.login_page.get_login_error_message()
        expected_header = 'Epic sadface: Sorry, this user has been locked out.'
        condition = actual_header == expected_header
        screenshot_name = 'test_locked_out_user_login.png'
        self.assertion_helper.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def test_invalid_username_login(self):

        # login with invalid username
        self.login_page.user_login(self.invalid_user, self.valid_password)

        # the actual header value should match the expected value
        actual_header = self.login_page.get_login_error_message()
        expected_header = 'Epic sadface: Username and password do not match any user in this service'
        condition = actual_header == expected_header
        screenshot_name = 'test_invalid_username_login.png'
        self.assertion_helper.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def test_invalid_password_login(self):

        # login with invalid password
        self.login_page.user_login(self.standard_user, self.invalid_password)

        # the actual header value should match the expected value
        actual_header = self.login_page.get_login_error_message()
        expected_header = 'Epic sadface: Username and password do not match any user in this service'
        condition = actual_header == expected_header
        screenshot_name = 'test_invalid_password_login.png'
        self.assertion_helper.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def test_invalid_credentials_login(self):

        # login with invalid credentials
        self.login_page.user_login(self.invalid_user, self.invalid_password)

        # the actual header value should match the expected value
        actual_header = self.login_page.get_login_error_message()
        expected_header = 'Epic sadface: Username and password do not match any user in this service'
        condition = actual_header == expected_header
        screenshot_name = 'test_invalid_credentials_login.png'
        self.assertion_helper.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def test_no_credentials_login(self):

        # click login button without providing credentials
        self.login_page.click_login()

        # the actual header value should match the expected value
        actual_header = self.login_page.get_login_error_message()
        expected_header = 'Epic sadface: Username is required'
        condition = actual_header == expected_header
        screenshot_name = 'test_no_credentials_login.png'
        self.assertion_helper.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def test_no_username_login(self):

        # login without providing a username
        self.login_page.set_password(self.invalid_password)
        self.login_page.click_login()

        # the actual header value should match the expected value
        actual_header = self.login_page.get_login_error_message()
        expected_header = 'Epic sadface: Username is required'
        condition = actual_header == expected_header
        screenshot_name = 'test_no_username_login.png'
        self.assertion_helper.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def test_no_password_login(self):

        # login without providing a password
        self.login_page.set_username(self.standard_user)
        self.login_page.click_login()

        # the actual header value should match the expected value
        actual_header = self.login_page.get_login_error_message()
        expected_header = 'Epic sadface: Password is required'
        condition = actual_header == expected_header
        screenshot_name = 'test_no_password_login.png'
        self.assertion_helper.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def test_keyboard_keys_login(self):

        # enter username, password and click login button using Tab and Enter only
        self.login_page.click_tab()
        self.login_page.set_username(self.standard_user)
        self.login_page.click_tab()
        self.login_page.set_password(self.valid_password)
        self.login_page.click_enter()

        # the actual header value should match the expected value
        actual_header = self.inventory_page.get_header_text()
        expected_header = 'PRODUCTS'
        condition = actual_header == expected_header
        screenshot_name = 'test_keyboard_keys_login.png'
        self.assertion_helper.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def test_password_visibility(self):

        # set password and check if it's displayed as a text
        self.login_page.set_password(self.valid_password)

        # the actual password attribute type should match the expected attribute type
        actual_element_type = self.login_page.get_password_attribute_type()
        expected_element_type = 'password'
        condition = actual_element_type == expected_element_type
        screenshot_name = 'test_password_visibility.png'
        self.assertion_helper.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def test_password_copying_disabled(self):

        # set a password and copy it, then clear the password field and paste it, the field should be empty
        self.login_page.set_password(self.valid_password)
        self.login_page.copy_and_paste_password()

        # the password field should be empty, which means copying is disabled
        actual_data = self.login_page.is_password_field_empty()
        expected_data = ''
        condition = actual_data == expected_data
        screenshot_name = 'test_password_copying_disabled.png'
        self.assertion_helper.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def test_browser_reload(self):

        # perform a successful login and reload the page to check if user hasn't been logged out
        self.login_page.user_login(self.standard_user, self.valid_password)
        self.driver.execute_script('location.reload()')

        # the actual header value should match the expected value
        actual_header = self.inventory_page.get_header_text()
        expected_header = 'PRODUCTS'
        condition = actual_header == expected_header
        screenshot_name = 'test_browser_reload.png'
        self.assertion_helper.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def tearDown(self) -> None:
        self.driver.quit()
