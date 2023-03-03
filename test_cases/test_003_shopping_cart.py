import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage
from page_objects.shopping_cart_page import ShoppingCartPage
from test_cases.helpers import Helpers
from utilities.read_properties import ReadConfig


class TestAddToCart(unittest.TestCase):
    base_url = ReadConfig.get_base_url()
    standard_user = ReadConfig.get_standard_user()
    valid_password = ReadConfig.get_valid_password()

    def setUp(self) -> None:
        # get the driver and open the browser
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.base_url)

        # create page objects for further testing
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.shopping_cart_page = ShoppingCartPage(self.driver)

        # perform a successful login
        self.login_page.user_login(self.standard_user, self.valid_password)

        # get assertion and screenshot (if test failed) helper
        self.assertion_helper = Helpers(self.driver)

    # test shopping cart functionality

    def test_add_to_cart(self):
        # add one item to the cart and go to the shopping cart
        self.inventory_page.click_add_to_cart()
        self.inventory_page.click_shopping_cart()

        # the item should be displayed in the cart
        condition = self.shopping_cart_page.is_any_item_displayed()
        screenshot_name = "test_add_to_cart.png"
        self.assertion_helper.assert_and_take_screenshot_if_failed(
            condition, screenshot_name
        )

    def tearDown(self) -> None:
        self.driver.quit()
