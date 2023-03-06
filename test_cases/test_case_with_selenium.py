import os
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage
from page_objects.shopping_cart_page import ShoppingCartPage
from utilities.read_properties import ReadConfig


class TestCaseWithSelenium(unittest.TestCase):
    def get_driver_and_open_url(self):
        base_url = ReadConfig.get_base_url()
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(base_url)
        return self.driver

    def get_page_objects(self):
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.shopping_cart_page = ShoppingCartPage(self.driver)

    def setUp(self) -> None:
        # get the driver, open the browser and open the url
        self.get_driver_and_open_url()

        # get page objects for further testing
        self.get_page_objects()

    def assert_and_take_screenshot_if_failed(self, condition, screenshot_name):
        if not condition:
            webdriver.Chrome.save_screenshot(
                self.driver,
                f"{os.path.abspath(os.curdir)}//screenshots//{screenshot_name}",
            )
            assert False
        assert True
