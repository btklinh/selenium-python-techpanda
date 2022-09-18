from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.Create_Account import CreateAccount
from pages.Mobile_Page import MobilePage
from pages.Log_In import LogIn


class HomePage(BaseDriver):
    # Locators
    ACCOUNT_LINK = "//div[@class='account-cart-wrapper']//span[text()='Account']"
    REGISTER_LINK = "//a[contains(text(),'Register')]"
    LOGIN_LINK = "//a[contains(text(),'Log In')]"
    MOBILE_LINK = "//a[contains(text(),'Mobile')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_account_menu(self):
        self.wait_for_element_clickable(By.XPATH, self.ACCOUNT_LINK)
        self.driver.find_element(By.XPATH, self.ACCOUNT_LINK).click()

    def click_on_register_link(self):
        self.wait_for_element_clickable(By.XPATH, self.REGISTER_LINK)
        self.driver.find_element(By.XPATH, self.REGISTER_LINK).click()
        create_acc = CreateAccount(self.driver)
        return create_acc

    def click_on_login_link(self):
        self.wait_for_element_clickable(By.XPATH, self.LOGIN_LINK)
        self.driver.find_element(By.XPATH, self.LOGIN_LINK).click()
        login = LogIn(self.driver)
        return login

    def click_to_mobile_link(self):
        self.wait_for_element_clickable(By.XPATH, self.MOBILE_LINK)
        self.driver.find_element(By.XPATH, self.MOBILE_LINK).click()
        mobile_page = MobilePage(self.driver)
        return mobile_page
