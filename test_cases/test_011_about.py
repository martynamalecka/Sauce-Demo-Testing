from test_cases.test_case_with_selenium import TestCaseWithSelenium
from utilities.read_properties import ReadConfig


class TestAbout(TestCaseWithSelenium):
    def setUp(self) -> None:
        super().setUp()

        # perform a successful login
        self.login_page.login_with_standard_username_and_password()

    def test_about(self):
        # open a dropdown menu and go to About
        self.inventory_page.click_dropdown_menu()
        self.inventory_page.click_about()

        # the actual website title should match the expected title
        actual_title = self.driver.title
        expected_title = (
            "Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing"
        )
        condition = actual_title == expected_title
        screenshot_name = "test_about.png"
        self.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def tearDown(self) -> None:
        self.driver.quit()
