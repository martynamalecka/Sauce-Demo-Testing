from test_cases.test_case_with_selenium import TestCaseWithSelenium
from utilities.read_properties import ReadConfig


class TestFooter(TestCaseWithSelenium):
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

    def test_footer_content(self):
        # the actual footer data should match the expected data
        actual_footer_text = self.inventory_page.get_footer_text()
        expected_footer_text = (
            "© 2023 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
        )
        condition = actual_footer_text == expected_footer_text
        screenshot_name = "test_footer_content.png"
        self.assert_and_take_screenshot_if_failed(
            condition, screenshot_name
        )

    def tearDown(self) -> None:
        self.driver.quit()
