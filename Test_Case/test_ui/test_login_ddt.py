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

        if data['expected_result'] == "success":
            expect(lp.logout_visible).to_be_visible()
            logger.info("Valid Login Scenario Passed!")
        else:
            expect(lp.login_error_message()).to_have_text(data['expected_message'])
            logger.info(f"Negative Scenario '{data['scenario']}' Passed Successfully!")

        logger.info("******************DDT TEST ARE COMPLETED**************************")