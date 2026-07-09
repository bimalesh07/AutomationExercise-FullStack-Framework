import pytest
from playwright.sync_api import expect
from PageObjects.Login_Page import LoginPage  # Purana Login POM re-use kiya
from PageObjects.Product_Page import ProductPage  # Purana Product POM re-use kiya
from PageObjects.Checkout_Page import CheckoutPage  # Naya Checkout POM


@pytest.mark.ui
class TestEndToEndOrderFlow:

    def test_place_order_successfully_e2e(self, logged_in_page):
        # 1. SETUP: Humne 'logged_in_page' fixture use kiya, toh browser direct LOGIN hokar hi khulega!
        page, logger = logged_in_page
        logger.info(
            "******* STARTING COMPLETE END-TO-END ORDER PLACEMENT TEST *******"
        )

        # Saare Page Objects ko initialize karo
        product_page = ProductPage(page, logger)
        checkout_page = CheckoutPage(page, logger)

        # 2. STEP: Products page par jao aur items add karo (Re-using existing methods!)
        product_page.navigate_to_product()

        logger.info("E2E Step: Adding item to cart...")
        product_page.add_to_cart_first.click()
        product_page.continue_shopping_btn.click()

        # 3. STEP: Cart page kholo
        logger.info("E2E Step: Navigating to cart screen...")
        product_page.add_to_cart_second.click()
        product_page.view_cart_modal_link.click()

        # 4. STEP: Checkout Page par jump karo (Naya functional part)
        logger.info("E2E Step: Clicking Proceed to Checkout...")
        checkout_page.proceed_to_checkout_btn.click()

        # Delivery address aur description verify karo
        expect(checkout_page.delivery_address_header).to_be_visible()
        checkout_page.order_comment_textarea.fill(
            "Please deliver by evening. Thanks!"
        )
        checkout_page.place_order_btn.click()

        # 5. STEP: Payment Engine complete karo
        logger.info("E2E Step: Entering Fake Payment Details...")
        checkout_page.payment_name.fill("Bimalesh Kumar")
        checkout_page.payment_card_number.fill("1234567890123456")
        checkout_page.payment_cvc.fill("123")
        checkout_page.payment_expiry_month.fill("12")
        checkout_page.payment_expiry_year.fill("2030")
        checkout_page.submit_payment_btn.click()

        # 6. FINAL ASSERTION: Order success validation
        logger.info("E2E Step: Verifying Order Placed Message...")
        expect(checkout_page.order_success_message).to_be_visible()
        expect(checkout_page.order_success_message).to_have_text(
            "ORDER PLACED!"
        )

        logger.info(
            "******* E2E TEST PASSED: Full Order Cycle Completed Successfully! *******"
        )