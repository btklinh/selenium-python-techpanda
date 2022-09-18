from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By


class ShoppingCart(BaseDriver):
    # Locators:
    SHOPPING_CART_TITLE = "//div[@class='page-title title-buttons']/h1"
    PRODUCT_NAME_LABEL = "//h2[@class='product-name']/a"
    PRODUCT_PRICE_LABEL = "//td[@class='product-cart-price']//span[@class='price']"
    PRODUCT_QTY_TEXTBOX = "//input[@title='Qty']"
    PRODUCT_SUBTOTAL_LABEL = "//td[@class='product-cart-total']//span[@class='price']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_shopping_cart_title(self):
        self.wait_for_element_is_display(By.XPATH, self.SHOPPING_CART_TITLE)
        return self.driver.find_element(By.XPATH, self.SHOPPING_CART_TITLE).text

    def get_product_name(self):
        self.wait_for_element_is_display(By.XPATH, self.PRODUCT_NAME_LABEL)
        return self.driver.find_element(By.XPATH, self.PRODUCT_NAME_LABEL).text

    def get_produce_price(self):
        self.wait_for_element_is_display(By.XPATH, self.PRODUCT_PRICE_LABEL)
        return self.driver.find_element(By.XPATH, self.PRODUCT_PRICE_LABEL).text

    def get_produce_qty(self):
        self.wait_for_element_is_display(By.XPATH, self.PRODUCT_QTY_TEXTBOX)
        return self.driver.find_element(By.XPATH, self.PRODUCT_QTY_TEXTBOX).get_attribute("value")
