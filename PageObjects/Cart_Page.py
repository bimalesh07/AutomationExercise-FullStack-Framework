from playwright.sync_api import Page
import logging

class CartPage:
    
    def __init__(self, page: Page, logger):
        self.page = page
        self.logger = logger
    
        self.quantity_input = page.locator("#quantity")
        self.add_to_cart_detail_btn = page.locator("button:has-text('Add to cart')")
        self.cart_quantity_value = page.locator("td.cart_quantity button")
        self.delete_item_btn = page.locator("a.cart_quantity_delete")
        self.empty_cart_text = page.locator("#empty_cart")


    def change_quantity_and_add(self, qty: str):
        self.logger.info(f"Changing quantity to {qty} on product detail page...")
        self.quantity_input.fill(qty)
        self.add_to_cart_detail_btn.click()

    def remove_product(self):
        self.logger.info("Clicking on 'X' button to remove product from cart...")
        self.delete_item_btn.click()