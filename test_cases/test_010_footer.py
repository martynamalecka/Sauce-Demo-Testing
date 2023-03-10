from test_cases.test_case_with_selenium import TestCaseWithSelenium


class TestFooter(TestCaseWithSelenium):
    def setUp(self) -> None:
        super().setUp()

        # perform a successful login
        self.login_page.login_with_standard_username_and_password()

    def test_footer_content(self):
        self.assert_and_take_screenshot_if_failed(
            self.inventory_page.get_footer_text()
            == "© 2023 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy",
            "test_footer_content.png",
        )
