from test_cases.test_case_with_selenium import TestCaseWithSelenium
from utilities.read_properties import ReadConfig


class TestFooter(TestCaseWithSelenium):
    def setUp(self) -> None:
        super().setUp()

        # perform a successful login
        self.login_page.login_with_standard_username_and_password()

    def test_footer_content(self):
        # the actual footer data should match the expected data
        actual_footer_text = self.inventory_page.get_footer_text()
        expected_footer_text = (
            "© 2023 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
        )
        condition = actual_footer_text == expected_footer_text
        screenshot_name = "test_footer_content.png"
        self.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def tearDown(self) -> None:
        self.driver.quit()
