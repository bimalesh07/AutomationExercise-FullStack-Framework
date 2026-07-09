import pytest
from playwright.sync_api import expect
from PageObjects.Product_Page import ProductPage
from PageObjects.Cart_Page import CartPage  # 👈 Naya POM import kiya

@pytest.mark.ui
class TestCartIndividualValidations:

    def test_verify_product_quantity_in_cart(self, ui_page):
        page, logger = ui_page
        logger.info("******* Starting Guest Test: Verify Product Quantity *******")
        
        product_page = ProductPage(page, logger)
        cart_page = CartPage(page, logger) 

        product_page.navigate_to_product()
        product_page.view_product_first.click()
        cart_page.change_quantity_and_add("4")
        
        product_page.view_cart_modal_link.click()
        expect(cart_page.cart_quantity_value).to_have_text("4")
        logger.info("Guest Quantity 4 Verification Passed")


    def test_remove_product_from_cart(self, ui_page):
        page, logger = ui_page
        logger.info("******* Starting Guest Test: Remove Product from Cart *******")
        
        product_page = ProductPage(page, logger)
        cart_page = CartPage(page, logger)

        product_page.navigate_to_product()
        product_page.add_to_cart_first.click()
        product_page.view_cart_modal_link.click()
        
        cart_page.remove_product()
        
        expect(cart_page.empty_cart_text).to_be_visible()
        expect(cart_page.empty_cart_text).to_contain_text("Cart is empty!")
        logger.info("Guest Product Removal Passed!")