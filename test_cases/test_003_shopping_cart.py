from test_cases.test_case_with_selenium import TestCaseWithSelenium
from utilities.read_properties import ReadConfig


class TestAddToCart(TestCaseWithSelenium):
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

    # test shopping cart functionality

    def test_add_to_cart(self):
        # add one item to the cart and go to the shopping cart
        self.inventory_page.click_add_to_cart()
        self.inventory_page.click_shopping_cart()

        # the item should be displayed in the cart
        condition = self.shopping_cart_page.is_any_item_displayed()
        screenshot_name = "test_add_to_cart.png"
        self.assert_and_take_screenshot_if_failed(
            condition, screenshot_name
        )

    def tearDown(self) -> None:
        self.driver.quit()
