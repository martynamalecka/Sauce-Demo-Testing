from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from utilities.read_properties import ReadConfig


class LoginPage:
    # login page objects by ID
    txt_username_id = "user-name"
    txt_password_id = "password"
    btn_login_id = "login-button"

    # login page objects by XPATH
    txt_login_error_msg_xpath = '//*[@id="login_button_container"]/div/form/div[3]/h3'
    txt_logout_confirmation_xpath = '//*[@id="login_credentials"]/h4'

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, self.txt_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.btn_login_id).click()

    def get_login_error_message(self):
        return self.driver.find_element(By.XPATH, self.txt_login_error_msg_xpath).text

    def click_tab(self):
        actions = ActionChains(self.driver)
        return actions.send_keys(Keys.TAB).perform()

    def click_enter(self):
        actions = ActionChains(self.driver)
        return actions.send_keys(Keys.ENTER).perform()

    def get_logout_confirmation_text(self):
        return self.driver.find_element(
            By.XPATH, self.txt_logout_confirmation_xpath
        ).text

    def login_user(self, username, password):
        self.driver.find_element(By.ID, self.txt_username_id).send_keys(username)
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)
        self.driver.find_element(By.ID, self.btn_login_id).click()

    def login_with_standard_username_and_password(self):
        standard_user = ReadConfig.get_standard_user()
        valid_password = ReadConfig.get_valid_password()
        self.driver.find_element(By.ID, self.txt_username_id).send_keys(standard_user)
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(valid_password)
        self.driver.find_element(By.ID, self.btn_login_id).click()

    def copy_and_paste_password(self):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(
            Keys.CONTROL + "c"
        )
        self.driver.find_element(By.ID, self.txt_password_id).clear()
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(
            Keys.CONTROL + "v"
        )

    def is_password_field_empty(self):
        return self.driver.find_element(By.ID, self.txt_password_id).text

    def get_password_attribute_type(self):
        element = self.driver.find_element(By.ID, self.txt_password_id)
        element_type = element.get_attribute("type")
        return element_type
