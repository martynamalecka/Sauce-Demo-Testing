from test_cases.test_case_with_selenium import TestCaseWithSelenium
from utilities.read_properties import ReadConfig


class TestSocialMediaButtons(TestCaseWithSelenium):
    def setUp(self) -> None:
        super().setUp()

        # perform a successful login
        self.login_page.login_with_standard_username_and_password()

    # test social media buttons functionality

    def test_twitter_button(self):
        # click the Twitter button and get the actual website title
        self.inventory_page.click_twitter_button()
        actual_title = self.driver.title

        # the actual website title should match the expected title
        expected_title = "Swag Labs"
        condition = actual_title == expected_title
        screenshot_name = "test_twitter_button.png"
        self.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def test_facebook_button(self):
        # click the Facebook button and get the actual website title
        self.inventory_page.click_facebook_button()
        actual_title = self.driver.title

        # the actual website title should match the expected title
        expected_title = "Swag Labs"
        condition = actual_title == expected_title
        screenshot_name = "test_facebook_button.png"
        self.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def test_linkedin_button(self):
        # click the LinkedIn button and get the actual website title
        self.inventory_page.click_linkedin_button()
        actual_title = self.driver.title

        # the actual website title should match the expected title
        expected_title = "Swag Labs"
        condition = actual_title == expected_title
        screenshot_name = "test_linkedin_button.png"
        self.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def tearDown(self) -> None:
        self.driver.quit()
