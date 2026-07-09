import pytest
from playwright.sync_api import expect
from PageObjects.Product_Page import ProductPage
from PageObjects.Checkout_Page import CheckoutPage

@pytest.mark.ui
class TestE2EWorkflow:

    def test_execute_complete_happy_path_order(self, logged_in_page):
       
        page, logger = logged_in_page
        logger.info("Starting E2E Test")

        product_page = ProductPage(page, logger)
        checkout_page = CheckoutPage(page, logger)

        product_page.navigate_to_product()
        product_page.add_to_cart_first.click()
        product_page.view_cart_modal_link.click()

       
        checkout_page.click_proceed_to_checkout()

       
        checkout_page.fill_order_comment("Master E2E Valid Flow Order - Bimalesh Automation")
        checkout_page.click_place_order()

        checkout_page.fill_payment_details_and_submit(
            name="Mr. Bimalesh Automation",
            card_num="4111111111111111",
            cvc="455",
            month="12",
            year="2028"
        )

    
        expect(checkout_page.order_placed_header).to_be_visible()
        logger.info("Order Placed header is visible on screen!")

        logger.info("Clicking Download Invoice button...")
        
        with page.expect_download() as download_info:
            page.click("text=Download Invoice")
            
        download = download_info.value
        download_path = "./Reports/final_invoice.txt"
        download.save_as(download_path)
        
        logger.info(f"Invoice saved locally at: {download_path}")
        logger.info("E2E RUN PASSED SUCCESSFULLY!")