from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class MyAccount(BaseDriver):
    # Locators
    ACCOUNT_INFORMATION_LINK = "//a[text()='Account Information']"
    ACCOUNT_NAME_LABEL = "//div[@class='store-language-container']/following-sibling::p"
    FIRSTNAME_TEXTBOX = "//input[@id='firstname']"
    MIDDLENAME_TEXTBOX = "//input[@id='middlename']"
    LASTNAME_TEXTBOX = "//input[@id='lastname']"
    EMAIL_ADDRESS_TEXTBOX = "//input[@id='email']"
    SUCCESS_MESSAGE = "//li[@class='success-msg']//span"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def create_account_success_message(self):
        self.wait_for_element_is_display(By.XPATH, self.SUCCESS_MESSAGE)
        return self.driver.find_element(By.XPATH, self.SUCCESS_MESSAGE).text

    def click_account_information_link(self):
        self.wait_for_element_clickable(By.XPATH, self.ACCOUNT_INFORMATION_LINK)
        self.driver.find_element(By.XPATH, self.ACCOUNT_INFORMATION_LINK).click()

    def get_firstname_text(self):
        self.wait_for_element_is_display(By.XPATH, self.FIRSTNAME_TEXTBOX)
        self.driver.find_element(By.XPATH, self.FIRSTNAME_TEXTBOX).text

    def get_middlename_text(self):
        self.wait_for_element_is_display(By.XPATH, self.MIDDLENAME_TEXTBOX)
        self.driver.find_element(By.XPATH, self.MIDDLENAME_TEXTBOX).text

    def get_lastname_text(self):
        self.wait_for_element_is_display(By.XPATH, self.LASTNAME_TEXTBOX)
        self.driver.find_element(By.XPATH, self.LASTNAME_TEXTBOX).text

    def get_email_address_text(self):
        self.wait_for_element_is_display(By.XPATH, self.EMAIL_ADDRESS_TEXTBOX)
        self.driver.find_element(By.XPATH, self.EMAIL_ADDRESS_TEXTBOX).text

    def get_account_name_header(self):
        self.wait_for_element_is_display(By.XPATH, self.ACCOUNT_NAME_LABEL)
        # return self.driver.execute_script("document.getElementsByClassName('welcome-msg').item(0).textContent")
        return self.driver.find_element(By.XPATH, self.ACCOUNT_NAME_LABEL).text
