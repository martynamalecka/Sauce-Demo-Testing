from selenium.webdriver.common.by import By


class ShoppingCartPage:

    # shopping cart page objects by XPATH

    txt_cart_item_xpath = '//*[@id="cart_contents_container"]/div/div[1]/div[3]'

    def __init__(self, driver):
        self.driver = driver

    def is_any_item_displayed(self):
        return self.driver.find_element(By.XPATH, self.txt_cart_item_xpath).is_displayed()
