from test_cases.test_case_with_selenium import TestCaseWithSelenium


class TestSocialMediaButtons(TestCaseWithSelenium):
    def setUp(self) -> None:
        super().setUp()

        # perform a successful login
        self.login_page.login_with_standard_username_and_password()

    # test social media buttons functionality

    def test_twitter_button(self):
        # click the Twitter button
        self.inventory_page.click_twitter_button()

        # the actual website title should match the expected title
        self.assert_and_take_screenshot_if_failed(
            self.driver.title == "Swag Labs", "test_twitter_button.png"
        )

    def test_facebook_button(self):
        # click the Facebook button
        self.inventory_page.click_facebook_button()

        # the actual website title should match the expected title
        self.assert_and_take_screenshot_if_failed(
            self.driver.title == "Swag Labs", "test_facebook_button.png"
        )

    def test_linkedin_button(self):
        # click the LinkedIn button
        self.inventory_page.click_linkedin_button()

        # the actual website title should match the expected title
        self.assert_and_take_screenshot_if_failed(
            self.driver.title == "Swag Labs", "test_linkedin_button.png"
        )

    def tearDown(self) -> None:
        self.driver.quit()
