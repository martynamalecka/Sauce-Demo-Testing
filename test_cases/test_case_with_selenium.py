import os
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage
from page_objects.shopping_cart_page import ShoppingCartPage
from utilities.read_properties import ReadConfig


class TestCaseWithSelenium(unittest.TestCase):
    # set default browser
    DEFAULT_BROWSER = "chrome"

    def get_driver_and_open_url(self):
        # get base URL
        base_url = ReadConfig.get_base_url()

        # set browser options - Chrome
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")

        # set browser options - Firefox
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--start-maximized")

        # set browser options - Edge
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless")
        edge_options.add_argument("--start-maximized")

        # get the environment variable - BROWSER
        browser = os.environ.get("BROWSER", self.DEFAULT_BROWSER)

        # open the browser
        if browser == "edge":
            self.driver = webdriver.Edge(options=edge_options)
        elif browser == "firefox":
            self.driver = webdriver.Firefox(options=firefox_options)
        else:
            self.driver = webdriver.Chrome(options=chrome_options)

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

    def tearDown(self) -> None:
        self.driver.quit()
