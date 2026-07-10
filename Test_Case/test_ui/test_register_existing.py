import pytest
from playwright.sync_api import expect
from PageObjects.Registeration_Page import RegistrationPage
from PageObjects.Login_Page import LoginPage
from Utilities.Read_Env import ReadEnv

@pytest.mark.ui
class TestRegisterExistingEmail:
    #Register existing email
    def test_register_with_existing_email_error(self, ui_page):
        page, logger = ui_page

        logger.info("******* Starting Test Case 5: Register User with existing email *******")
        existing_email = ReadEnv.get_email() 

        register_page = RegistrationPage(page, logger)
        register_page.navigate_to_signup()
        register_page.fill_initial_signup("Bimalesh", existing_email)


        logger.info("Verifying 'Email Address already exist!' warning display...")
        
        expect(register_page.signup_error_message).to_be_visible()
        expect(register_page.signup_error_message).to_have_text("Email Address already exist!")

        logger.info("******* Existing Passed Successfully! *******")
