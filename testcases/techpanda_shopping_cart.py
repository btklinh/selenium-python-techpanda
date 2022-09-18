import pytest
from pages.Home_Page import HomePage

@pytest.mark.usefixtures("setup")
class TestShoppingCart:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.home_page = HomePage(self.driver)

    def test_01_Add_a_product_to_cart_from_product_list(self):
        # Click to mobile link
        mobile_page = self.home_page.click_to_mobile_link()
        # Get the mobile name to add to the cart
        mobile_name = mobile_page.get_product_name()
        mobile_price = mobile_page.get_produce_price()
        # Click Add to Cart button
        shopping_cart_page = mobile_page.click_to_add_to_cart()
        # Verify Shopping cart page
        # --Check product is added to cart (Product Name, Price, Qty)
        assert shopping_cart_page.get_shopping_cart_title() == "SHOPPING CART"
        assert shopping_cart_page.get_product_name() == mobile_name
        assert shopping_cart_page.get_produce_price() == mobile_price
        assert shopping_cart_page.get_produce_qty() == '1'





