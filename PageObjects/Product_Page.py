import pytest
from playwright.sync_api import expect, Page
class ProductPage:

    def __init__(self, page:Page, logger):
        self.page = page
        self.logger = logger

        # Navigation Link
        self.products_nav_link = page.locator('.shop-menu a[href="/products"]')
        self.all_products_header = page.locator("text=All Products")

        #Search Locators
        self.search_input = page.locator("[id='search_product']")
        self.search_button = page.locator("[id='submit_search']")
        self.searched_header = page.locator("text=Searched Products")

        # Product Detail Locators
        self.view_product_first = page.locator(".choose a").first
        self.product_name_detail = page.locator(".product-information h2")
        self.product_category_detail = page.locator(
            ".product-information p:has-text('Category:')"
        )

        #Add to Cart 
        self.add_to_cart_first = page.locator("(//a[@data-product-id='1'])[1]")
        self.add_to_cart_second = page.locator("(//a[@data-product-id='2'])[1]")
        self.continue_shopping_btn = page.locator(
            "button:has-text('Continue Shopping')"
        )
        self.view_cart_modal_link = page.locator("u:has-text('View Cart')")

        # Cart Table rows
        self.cart_product_rows = page.locator("table#cart_info_table tbody tr")



    def navigate_to_product(self):
        self.logger.info(
            "************ Navigate to Products Page *************"
        )
        self.products_nav_link.click()

    def search_for_item(self, item_name):
        self.logger.info(f"Searching for item: {item_name}")
        self.search_input.fill(item_name)
        self.search_button.click()