from base.base_driver import BaseDriver
from pages.Shopping_Cart_Page import ShoppingCart
from selenium.webdriver.common.by import By

class MobilePage(BaseDriver):
    # Locators
    PRODUCT_NAME_LABEL = "//h2[@class='product-name']/a"
    PRODUCT_PRICE_LABEL = "//div[@class='price-box']//span[(@class='price') and not(contains(@id, 'old-price-3'))]"
    ADD_TO_CART_BUTTON = "//span[text()='Add to Cart']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_product_name(self):
        self.wait_for_element_is_display(By.XPATH, self.PRODUCT_NAME_LABEL)
        return self.driver.find_element(By.XPATH, self.PRODUCT_NAME_LABEL).text

    def get_produce_price(self):
        self.wait_for_element_is_display(By.XPATH, self.PRODUCT_PRICE_LABEL)
        return self.driver.find_element(By.XPATH, self.PRODUCT_PRICE_LABEL).text

    def click_to_add_to_cart(self):
        self.wait_for_element_clickable(By.XPATH, self.ADD_TO_CART_BUTTON)
        self.driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON).click()
        shopping_cart_page = ShoppingCart(self.driver)
        return shopping_cart_page

