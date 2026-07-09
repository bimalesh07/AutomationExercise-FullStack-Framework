import pytest
from playwright.sync_api import expect
from PageObjects.Product_Page import ProductPage


@pytest.mark.ui
class TestProductCatalog:

    def test_verify_all_products_and_details(self, ui_page):
        page, logger = ui_page
        logger.info(
            "******* Starting Test Case 8: Verify All Products & Details *******"
        )
        product_page = ProductPage(page, logger)
        product_page.navigate_to_product()

        expect(product_page.all_products_header).to_be_visible()
        product_page.view_product_first.click()

        expect(product_page.product_name_detail).to_be_visible()
        expect(product_page.product_category_detail).to_be_visible()
        logger.info("******* Test Case Passed! *******")

    def test_search_product_functional(self, ui_page):
        page, logger = ui_page
        logger.info("******* Starting Test Case: Search Product *******")

        product_page = ProductPage(page, logger)
        product_page.navigate_to_product()

        product_page.search_for_item("Blue Top")

        expect(product_page.searched_header).to_be_visible()
        logger.info("******* Test Case 9 Passed! *******")


    def test_add_products_to_cart_successfully(self, ui_page):
        page, logger = ui_page
        logger.info(
            "******* Starting Test Case 12: Add Products in Cart *******"
        )

        product_page = ProductPage(page, logger)
        product_page.navigate_to_product()

        logger.info("Adding first product to cart...")
        product_page.add_to_cart_first.click()

        logger.info("Clicking 'Continue Shopping' on bootstrap modal popup...")
        product_page.continue_shopping_btn.click()

        logger.info("Adding second product to cart...")
        product_page.add_to_cart_second.click()

        logger.info("Clicking 'View Cart' link inside the modal...")
        product_page.view_cart_modal_link.click()

        logger.info("Verifying cart contains exactly 2 row elements...")
        expect(product_page.cart_product_rows).to_have_count(2)

        logger.info("******* Test Case Passed Successfully! *******")