import pytest
from PageObjects.Login_Page import LoginPage
from playwright.sync_api import Page, expect
from Utilities.Read_Env import ReadEnv

@pytest.mark.ui
@pytest.mark.smoke
class TestLogin:
    def test_user_login(self, ui_page):
        page, logger = ui_page

        email_l = ReadEnv.get_email()
        password_l = ReadEnv.get_password()

        logger.info("******* Start login execution *******")
        login_page = LoginPage(page, logger)
        login_page.navigate_loginpage()
        login_page.Login_with_credentials(email_l, password_l)

        logger.info("*********Verifying sucessful login via logout button visibility")
        expect(login_page.logout_visible).to_be_visible()
        logger.info("******* Login Successful! *******")



        

