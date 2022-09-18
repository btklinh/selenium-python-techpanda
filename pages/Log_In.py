from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.My_Account import MyAccount

class LogIn(BaseDriver):
    # Locators

    EMAIL_ADDRESS_TEXTBOX = "//input[@id='email']"
    PASSWORD_TEXTBOX = "//input[@id='pass']"
    LOGIN_BUTTON = "//button[@id='send2']"
    ERROR_TEXT = "//li[@class='error-msg']//span"
    ERROR_TEXT_EMAIL_BLANK = "//div[@id='advice-required-entry-email']"
    ERROR_TEXT_PASSWORD_BLANK = "//div[@id='advice-required-entry-pass']"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def input_email(self, email):
        self.wait_for_element_is_display(By.XPATH, self.EMAIL_ADDRESS_TEXTBOX)
        self.driver.find_element(By.XPATH, self.EMAIL_ADDRESS_TEXTBOX).send_keys(email)

    def input_password(self, password):
        self.wait_for_element_is_display(By.XPATH, self.PASSWORD_TEXTBOX)
        self.driver.find_element(By.XPATH, self.PASSWORD_TEXTBOX).send_keys(password)

    def click_login_button(self):
        self.wait_for_element_clickable(By.XPATH, self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()
        my_acc = MyAccount(self.driver)
        return my_acc


    def get_error_message(self):
        self.wait_for_element_is_display(By.XPATH, self.ERROR_TEXT)
        return self.driver.find_element(By.XPATH, self.ERROR_TEXT).text

    def get_error_message_email_blank(self):
        self.wait_for_element_is_display(By.XPATH, self.ERROR_TEXT_EMAIL_BLANK)
        return self.driver.find_element(By.XPATH, self.ERROR_TEXT_EMAIL_BLANK).text

    def get_error_message_password_blank(self):
        self.wait_for_element_is_display(By.XPATH, self.ERROR_TEXT_PASSWORD_BLANK)
        return self.driver.find_element(By.XPATH, self.ERROR_TEXT_PASSWORD_BLANK).text