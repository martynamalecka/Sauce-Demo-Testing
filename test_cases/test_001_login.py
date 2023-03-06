from test_cases.test_case_with_selenium import TestCaseWithSelenium
from utilities.read_properties import ReadConfig


class TestLogin(TestCaseWithSelenium):
    # get login credentials
    standard_user = ReadConfig.get_standard_user()
    locked_out_user = ReadConfig.get_locked_out_user()
    problem_user = ReadConfig.get_problem_user()
    performance_glitch_user = ReadConfig.performance_glitch_user()
    invalid_user = ReadConfig.invalid_user()
    valid_password = ReadConfig.get_valid_password()
    invalid_password = ReadConfig.get_invalid_password()

    # test login functionality
    def test_standard_user_login(self):
        # login with valid credentials
        self.login_page.login_user(self.standard_user, self.valid_password)

        # check if the actual header value matched the expected value
        self.assert_and_take_screenshot_if_failed(
            self.inventory_page.get_header_text() == "Products",
            "test_standard_user_login.png",
        )

    def test_problem_user_login(self):
        # login with problem user credentials
        self.login_page.login_user(self.problem_user, self.valid_password)

        # the actual header value should match the expected value
        self.assert_and_take_screenshot_if_failed(
            self.inventory_page.get_header_text() == "Products",
            "test_problem_user_login.png",
        )

    def test_performance_glitch_user_login(self):
        # login with performance glitch user credentials
        self.login_page.login_user(self.performance_glitch_user, self.valid_password)

        # the actual header value should match the expected value
        self.assert_and_take_screenshot_if_failed(
            self.inventory_page.get_header_text() == "Products",
            "test_performance_glitch_user_login.png",
        )

    def test_locked_out_user_login(self):
        # login with locked out user credentials
        self.login_page.login_user(self.locked_out_user, self.valid_password)

        # the actual header value should match the expected value
        self.assert_and_take_screenshot_if_failed(
            self.login_page.get_login_error_message()
            == "Epic sadface: Sorry, this user has been locked out.",
            "test_locked_out_user_login.png",
        )

    def test_invalid_username_login(self):
        # login with invalid username
        self.login_page.login_user(self.invalid_user, self.valid_password)

        # the actual header value should match the expected value
        self.assert_and_take_screenshot_if_failed(
            self.login_page.get_login_error_message()
            == "Epic sadface: Username and password do not match any user in this service",
            "test_invalid_username_login.png",
        )

    def test_invalid_password_login(self):
        # login with invalid password
        self.login_page.login_user(self.standard_user, self.invalid_password)

        # the actual header value should match the expected value
        self.assert_and_take_screenshot_if_failed(
            self.login_page.get_login_error_message()
            == "Epic sadface: Username and password do not match any user in this service",
            "test_invalid_password_login.png",
        )

    def test_invalid_credentials_login(self):
        # login with invalid credentials
        self.login_page.login_user(self.invalid_user, self.invalid_password)

        # the actual header value should match the expected value
        self.assert_and_take_screenshot_if_failed(
            self.login_page.get_login_error_message()
            == "Epic sadface: Username and password do not match any user in this service",
            "test_invalid_credentials_login.png",
        )

    def test_no_credentials_login(self):
        # click login button without providing credentials
        self.login_page.click_login()

        # the actual header value should match the expected value
        self.assert_and_take_screenshot_if_failed(
            self.login_page.get_login_error_message()
            == "Epic sadface: Username is required",
            "test_no_credentials_login.png",
        )

    def test_no_username_login(self):
        # login without providing a username
        self.login_page.set_password(self.invalid_password)
        self.login_page.click_login()

        # the actual header value should match the expected value
        self.assert_and_take_screenshot_if_failed(
            self.login_page.get_login_error_message()
            == "Epic sadface: Username is required",
            "test_no_username_login.png",
        )

    def test_no_password_login(self):
        # login without providing a password
        self.login_page.set_username(self.standard_user)
        self.login_page.click_login()

        # the actual header value should match the expected value
        self.assert_and_take_screenshot_if_failed(
            self.login_page.get_login_error_message()
            == "Epic sadface: Password is required",
            "test_no_password_login.png",
        )

    def test_login_using_keyboard_keys(self):
        # enter username, password and click login button using Tab and Enter only
        self.login_page.click_tab()
        self.login_page.set_username(self.standard_user)
        self.login_page.click_tab()
        self.login_page.set_password(self.valid_password)
        self.login_page.click_enter()

        # the actual header value should match the expected value
        self.assert_and_take_screenshot_if_failed(
            self.inventory_page.get_header_text() == "Products",
            "test_login_using_keyboard_keys.png",
        )

    def test_password_visibility(self):
        # set password and check if it's displayed as a text
        self.login_page.set_password(self.valid_password)

        # the actual password attribute type should match the expected attribute type
        self.assert_and_take_screenshot_if_failed(
            self.login_page.get_password_attribute_type() == "password",
            "test_password_visibility.png",
        )

    def test_password_copying_disabled(self):
        # set a password and copy it, then clear the password field and paste it, the field should be empty
        self.login_page.set_password(self.valid_password)
        self.login_page.copy_and_paste_password()

        # the password field should be empty, which means copying is disabled
        self.assert_and_take_screenshot_if_failed(
            self.login_page.is_password_field_empty() == "",
            "test_password_copying_disabled.png",
        )

    def test_browser_reload(self):
        # perform a successful login and reload the page to check if user hasn't been logged out
        self.login_page.login_user(self.standard_user, self.valid_password)
        self.driver.execute_script("location.reload()")

        # the actual header value should match the expected value
        self.assert_and_take_screenshot_if_failed(
            self.inventory_page.get_header_text() == "Products",
            "test_browser_reload.png",
        )

    def tearDown(self) -> None:
        self.driver.quit()
