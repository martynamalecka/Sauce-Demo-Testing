from test_cases.test_case_with_selenium import TestCaseWithSelenium
from utilities.read_properties import ReadConfig


class TestAbout(TestCaseWithSelenium):
    # get login credentials
    standard_user = ReadConfig.get_standard_user()
    valid_password = ReadConfig.get_valid_password()

    # test About functionality

    def setUp(self) -> None:
        # get the driver, open the browser and open the url
        self.get_driver_and_open_url()

        # get page objects for further testing
        self.get_page_objects()

        # perform a successful login
        self.login_page.user_login(self.standard_user, self.valid_password)

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
        self.assert_and_take_screenshot_if_failed(
            condition, screenshot_name
        )

    def tearDown(self) -> None:
        self.driver.quit()
