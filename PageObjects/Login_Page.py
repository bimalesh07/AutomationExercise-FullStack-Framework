import pytest
from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page:Page, logger):
        self.page = page
        self.logger = logger

        #locators
        self.login_menu_link = page.locator('.shop-menu a[href="/login"]')
        self.email_input = page.locator("[data-qa='login-email']")
        self.password_input = page.locator("[data-qa='login-password']")
        self.submit_button = page.locator("[data-qa='login-button']")
        self.logout_visible = page.locator('.shop-menu a[href="/logout"]')
        self.login_Invalid_message = page.locator("[style='color: red;']")

    def navigate_loginpage(self):
        self.logger.info("************Navigate loging Page ********")
        self.login_menu_link.click()

    def Login_with_credentials(self, email, password):
        self.logger.info("**********login Page start ***************")
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()
        self.logger.info("**************Sucessfully Loin Completed ******")

    def very_the_login(self):
        self.logger.info("**********Verify the login or not ************")
        return self.logout_visible()


    def login_error_message(self):
        self.logger.info("********Error message invlid password and username ******")
        return self.login_Invalid_message

    #logout 
    def click_logout(self):
        self.logger.info("Clicking on the Logout button link...")
        self.logout_visible.click()

    