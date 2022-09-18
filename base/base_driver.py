from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((locator_type, locator)))

    def wait_for_element_is_display(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((locator_type, locator)))

    def wait_for_alert_is_display(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.alert_is_present())