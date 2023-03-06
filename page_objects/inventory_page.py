from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class InventoryPage:
    # inventory page objects by ID

    btn_dropdown_menu_id = "react-burger-menu-btn"
    btn_logout_id = "logout_sidebar_link"
    lnk_about_id = "about_sidebar_link"
    btn_add_to_cart_id = "add-to-cart-sauce-labs-backpack"
    lnk_shopping_cart_id = "shopping_cart_container"
    btn_dropdown_menu_close_id = "react-burger-cross-btn"

    # inventory page objects by XPATH

    txt_header_xpath = '//*[@id="header_container"]/div[2]/span'
    lnk_dropdown_menu_container_xpath = (
        '//*[@id="menu_button_container"]/div/div[2]/div[1]/nav/a'
    )
    lnk_twitter_xpath = '//*[@id="page_wrapper"]/footer/ul/li[1]/a'
    lnk_facebook_xpath = '//*[@id="page_wrapper"]/footer/ul/li[2]/a'
    lnk_linkedin_xpath = '//*[@id="page_wrapper"]/footer/ul/li[3]/a'
    txt_footer_text_xpath = '//*[@id="page_wrapper"]/footer/div'

    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        self.driver.find_element(By.ID, self.btn_dropdown_menu_id).click()
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, self.btn_logout_id))
        )
        self.driver.find_element(By.ID, self.btn_logout_id).click()

    def get_header_text(self):
        return self.driver.find_element(By.XPATH, self.txt_header_xpath).text

    def click_add_to_cart(self):
        self.driver.find_element(By.ID, self.btn_add_to_cart_id).click()

    def click_shopping_cart(self):
        self.driver.find_element(By.ID, self.lnk_shopping_cart_id).click()

    def click_dropdown_menu(self):
        self.driver.find_element(By.ID, self.btn_dropdown_menu_id).click()
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, self.lnk_about_id))
        )

    def click_about(self):
        self.driver.find_element(By.ID, self.lnk_about_id).click()

    def click_dropdown_menu_close_button(self):
        self.driver.find_element(By.ID, self.btn_dropdown_menu_close_id).click()
        menu = self.driver.find_element(By.ID, self.lnk_about_id)
        WebDriverWait(self.driver, 10).until(ec.invisibility_of_element(menu))

    def check_if_dropdown_menu_visible(self):
        dropdown_menu_container = self.driver.find_element(
            By.XPATH, '//*[@id="menu_button_container"]/div/div[2]'
        )
        return self.driver.find_element(
            By.XPATH, self.lnk_dropdown_menu_container_xpath
        ).is_displayed() and not dropdown_menu_container.get_attribute("hidden")

    def click_twitter_button(self):
        self.driver.find_element(By.XPATH, self.lnk_twitter_xpath).click()

    def click_facebook_button(self):
        self.driver.find_element(By.XPATH, self.lnk_facebook_xpath).click()

    def click_linkedin_button(self):
        self.driver.find_element(By.XPATH, self.lnk_linkedin_xpath).click()

    def get_footer_text(self):
        return self.driver.find_element(By.XPATH, self.txt_footer_text_xpath).text
