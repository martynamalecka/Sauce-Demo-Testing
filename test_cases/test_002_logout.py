from test_cases.test_case_with_selenium import TestCaseWithSelenium


class TestLogout(TestCaseWithSelenium):
    def setUp(self) -> None:
        super().setUp()

        # perform a successful login
        self.login_page.login_with_standard_username_and_password()

        # log out
        self.inventory_page.click_logout()

    # test logout functionality

    def test_logout(self):
        # the actual header value should match the expected value
        self.assert_and_take_screenshot_if_failed(
            self.login_page.get_logout_confirmation_text() == "Accepted usernames are:",
            "test_logout.png",
        )

    def test_browse_back_logout(self):
        # browse back, user should be logged out
        self.driver.execute_script("window.history.go(-1)")

        # the actual error message value should match the expected error message
        self.assert_and_take_screenshot_if_failed(
            self.login_page.get_login_error_message()
            == "Epic sadface: You can only access '/inventory.html' when you are logged in.",
            "test_browse_back_logout.png",
        )

    def tearDown(self) -> None:
        self.driver.quit()
