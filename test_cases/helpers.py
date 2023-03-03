import os

from selenium import webdriver


class Helpers:
    def __init__(self, driver):
        self.driver = driver

    def assert_and_take_screenshot_if_failed(self, condition, screenshot_name):
        if not condition:
            webdriver.Chrome.save_screenshot(
                self.driver,
                f"{os.path.abspath(os.curdir)}//screenshots//{screenshot_name}",
            )
            assert False
        assert True
