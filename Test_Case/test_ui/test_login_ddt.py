import pytest
import json
from PageObjects.Login_Page import LoginPage
from playwright.sync_api import Page, expect

def load_json():
    with open("Test_Data/login.json", "r") as file:
        return json.load(file)


class TestLoginDDT:
    @pytest.mark.parametrize("data", load_json())
    def test_login_from(self, ui_page, data):
        page, logger = ui_page
        
        logger.info(f" ********* Start DDT Test: Scenario: {data['scenario']} ***********")
        lp = LoginPage(page, logger)
        lp.navigate_loginpage()
        lp.Login_with_credentials(data['email'], data['password'])

       #if  Data Valid hai 
        if data['is_valid']:
            expect(lp.logout_visible).to_be_visible()
            logger.info("Valid Login Scenario Passed!")

        #if Data Invalid hai
        else:
            # text validation hai
            if data['error_type'] == "page":
                expect(lp.login_error_message()).to_have_text(data['expected_message'])
                logger.info(f"Red Page Error Verified for: {data['scenario']}")
            
            #  tooltip validation hai
            elif data['error_type'] == "browser":
                target_element = data['error_element']
                actual_tooltip = page.locator(target_element).evaluate("el => el.validationMessage")
                
                #assertion
                assert actual_tooltip == data['expected_message'], f"Expected '{data['expected_message']}' but got '{actual_tooltip}'"
                logger.info(f"Browser Tooltip Verified for: {data['scenario']}")