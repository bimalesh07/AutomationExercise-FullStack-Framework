import pytest
from playwright.sync_api import expect
from PageObjects.Product_Page import ProductPage
from PageObjects.Checkout_Page import CheckoutPage

@pytest.mark.ui
class TestCheckoutFlow:

    def test_complete_checkout_to_payment_workflow(self, logged_in_page):
        """
        Test Case 16: Place Order: Login before Checkout (Full E2E Execution)
        """
        page, logger = logged_in_page
        logger.info("******* Starting Full Checkout & Payment Workflow *******")

        product_page = ProductPage(page, logger)
        checkout_page = CheckoutPage(page, logger)
        
    
        product_page.navigate_to_product()
        product_page.add_to_cart_first.click()
        product_page.view_cart_modal_link.click()
        
   
        checkout_page.click_proceed_to_checkout()

        checkout_page.fill_order_comment("Order ready hai, dispatch kar do!")
        checkout_page.click_place_order()
        
        checkout_page.fill_payment_details_and_submit(
            name="Mr. Bimalesh Automation",
            card_num="4111111111111111",
            cvc="455",
            month="07",
            year="2029"
        )
        
        logger.info("Verifying Order Success Page...")
        expect(checkout_page.order_placed_header).to_be_visible()
        
        logger.info("******* Test Passed! Order Placed Successfully *******")