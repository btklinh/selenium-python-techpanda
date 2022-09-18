from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.My_Account import MyAccount

class CreateAccount(BaseDriver):
    # Locators
    FIRST_NAME_TEXTBOX = "//input[@id='firstname']"
    MIDDLE_NAME_TEXTBOX = "//input[@id='middlename']"
    LAST_NAME_TEXTBOX = "//input[@id='lastname']"
    EMAIL_TEXTBOX = "//input[@id='email_address']"
    PASSWORD_TEXTBOX = "//input[@id='password']"
    CONFIRM_PASSWORD_TEXTBOX = "//input[@id='confirmation']"
    REGISTER_BUTTON = "//span[contains(text(),'Register')]"
    ERROR_MESSAGE = "//div[@id='advice-required-entry-firstname']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def input_first_name(self, firstname):
        self.wait_for_element_is_display(By.XPATH, self.FIRST_NAME_TEXTBOX)
        self.driver.find_element(By.XPATH, self.FIRST_NAME_TEXTBOX).send_keys(firstname)

    def input_middle_name(self, middlename):
        self.wait_for_element_is_display(By.XPATH, self.MIDDLE_NAME_TEXTBOX)
        self.driver.find_element(By.XPATH, self.MIDDLE_NAME_TEXTBOX).send_keys(middlename)

    def input_last_name(self, lastname):
        self.wait_for_element_is_display(By.XPATH, self.LAST_NAME_TEXTBOX)
        self.driver.find_element(By.XPATH, self.LAST_NAME_TEXTBOX).send_keys(lastname)

    def input_email(self, email):
        self.wait_for_element_is_display(By.XPATH, self.EMAIL_TEXTBOX)
        self.driver.find_element(By.XPATH, self.EMAIL_TEXTBOX).send_keys(email)

    def input_password(self, password):
        self.wait_for_element_is_display(By.XPATH, self.PASSWORD_TEXTBOX)
        self.driver.find_element(By.XPATH, self.PASSWORD_TEXTBOX).send_keys(password)

    def input_confirm_password(self, confirm_password):
        self.wait_for_element_is_display(By.XPATH, self.CONFIRM_PASSWORD_TEXTBOX)
        self.driver.find_element(By.XPATH, self.CONFIRM_PASSWORD_TEXTBOX).send_keys(confirm_password)

    def click_register_button(self):
        self.wait_for_element_is_display(By.XPATH, self.REGISTER_BUTTON)
        self.driver.find_element(By.XPATH, self.REGISTER_BUTTON).click()
        my_acc = MyAccount(self.driver)
        return my_acc

    def error_message_displayed(self):
        self.wait_for_element_is_display(By.XPATH, self.ERROR_MESSAGE)
        return self.driver.find_element(By.XPATH, self.ERROR_MESSAGE).text

    def alert_popup_displayed(self):
        self.wait_for_alert_is_display()
        return self.driver.switch_to.alert.text