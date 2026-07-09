import pytest
from playwright.sync_api import expect, Page
from PageObjects.Login_Page import LoginPage

class TestInvalidLogin:
    def test_login_with_incorrect(self, ui_page):
        page, logger = ui_page
        page:Page = page

        logger.info("*********Starting Test login user with incorrect email and password")
        login_page = LoginPage(page, logger)
        login_page.navigate_loginpage()


        login_page.Login_with_credentials("wrong@gamil.com", "wrongpassword123")
        logger.info("Verify error message text display ")
        expect(login_page.login_error_message()).to_be_visible()
        
        expect(login_page.login_error_message()).to_have_text(
            "Your email or password is incorrect!"
        )
        logger.info( "******* Test Case 3 Passed! Error message verified successfully. *******")