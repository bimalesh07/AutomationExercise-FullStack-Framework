import pytest
from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page:Page, logger):
        self.page = page
        self.logger = logger

        #locators
        self.login_menu_link = page.locator('.shop-menu a[href="/login"]')
        self.email_input = page.locator("data-qa=login-email")
        self.password_input = page.locator("data-qa=login-password")
        self.submit_button = page.locator("data-qa=login-button")

    def navigate_loginpage(self):
        self.logger.info("************Navigate loging Page ********")
        self.login_menu_link.click()

    def Login_with_credentials(self, email, password):
        self.logger.info("**********login Page start ***************")
        self.page.fill(self.login_email)

        