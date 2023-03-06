from test_cases.test_case_with_selenium import TestCaseWithSelenium
from utilities.read_properties import ReadConfig


class TestLogout(TestCaseWithSelenium):
    # get login credentials
    standard_user = ReadConfig.get_standard_user()
    valid_password = ReadConfig.get_valid_password()

    def setUp(self) -> None:
        # get the driver, open the browser and open the url
        self.get_driver_and_open_url()

        # get page objects for further testing
        self.get_page_objects()

        # perform a successful login
        self.login_page.user_login(self.standard_user, self.valid_password)

        # log out
        self.inventory_page.click_logout()

    # test logout functionality

    def test_logout(self):
        # the actual header value should match the expected value
        actual_logout_confirmation = self.login_page.get_logout_confirmation()
        expected_logout_confirmation = "Accepted usernames are:"
        condition = actual_logout_confirmation == expected_logout_confirmation
        screenshot_name = "test_logout.png"
        self.assert_and_take_screenshot_if_failed(
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
        self.assert_and_take_screenshot_if_failed(
            condition, screenshot_name
        )

    def tearDown(self) -> None:
        self.driver.quit()
