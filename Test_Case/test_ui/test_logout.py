import pytest
from playwright.sync_api import expect
from PageObjects.Login_Page import LoginPage

@pytest.mark.ui
@pytest.mark.smoke
class TestLogout:

    def test_user_can_logout_successfully(self, logged_in_page):
        page, logger = logged_in_page

        logger.info("******* Starting Test Case 4: Logout User *******")
        login_page = LoginPage(page, logger)
        login_page.click_logout()

        logger.info("Verifying user redirected back to login screen...")
        expect(page).to_have_url("https://automationexercise.com/login")

        logger.info("*******logout Passed Successfully! *******")