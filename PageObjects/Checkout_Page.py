from playwright.sync_api import Page
import logging

class CheckoutPage:
    def __init__(self, page: Page, logger: logging.Logger):
        self.page = page
        self.logger = logger
        
        #Checkout Page Elements
        self.proceed_to_checkout_btn = page.locator("text=Proceed To Checkout")
        self.comment_textarea = page.locator("textarea[name='message']")
        self.place_order_btn = page.locator("text=Place Order")
        
        #Payment Page Elements
        self.name_on_card_input = page.locator("[data-qa='name-on-card']")
        self.card_number_input = page.locator("[data-qa='card-number']")
        self.cvc_input = page.locator("[data-qa='cvc']")
        self.expiry_month_input = page.locator("[data-qa='expiry-month']")
        self.expiry_year_input = page.locator("[data-qa='expiry-year']")
        self.pay_button = page.locator("[data-qa='pay-button']")
        
    
        self.success_alert = page.locator("text=Your order has been placed successfully!")
        self.order_placed_header = page.locator("text=ORDER PLACED!")

    def click_proceed_to_checkout(self):
        self.proceed_to_checkout_btn.click()

    def fill_order_comment(self, comment_text: str):
        self.comment_textarea.fill(comment_text)

    def click_place_order(self):
        self.place_order_btn.click()

    def fill_payment_details_and_submit(self, name: str, card_num: str, cvc: str, month: str, year: str):
        self.logger.info("Filling credit card details...")
        self.name_on_card_input.fill(name)
        self.card_number_input.fill(card_num)
        self.cvc_input.fill(cvc)
        self.expiry_month_input.fill(month)
        self.expiry_year_input.fill(year)
        
        self.logger.info("Clicking 'Pay and Confirm Order' button...")
        self.pay_button.click()