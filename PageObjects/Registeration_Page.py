import pytest
from playwright.sync_api import expect, Page

class RegistrationPage:
    def __init__(self, page:Page, logger):
        self.page = page
        self.logger = logger
        
        #SELECTORS (Initial Signup)

        self.signup_login_link = '.shop-menu a[href="/login"]'
        self.signup_name_input = 'input[data-qa="signup-name"]'
        self.signup_email_input = 'input[data-qa="signup-email"]'
        self.signup_button = 'button[data-qa="signup-button"]'

        #SCREEN 2 SELECTORS (Account Information)

        self.gender_mr_radio = 'input[id="id_gender1"]'
        self.password_input = 'input[id="password"]'

        # DROPDOWN MAIN PATHS
        self.days_dropdown = 'select[id="days"]'
        self.months_dropdown = 'select[id="months"]'
        self.years_dropdown = 'select[id="years"]'
        self.country_dropdown = 'select[id="country"]'

        # Address Fields
        self.first_name_input = 'input[id="first_name"]'
        self.last_name_input = 'input[id="last_name"]'
        self.address_input = 'input[id="address1"]'
        self.state_input = 'input[id="state"]'
        self.city_input = 'input[id="city"]'
        self.zipcode_input = 'input[id="zipcode"]'
        self.mobile_input = 'input[id="mobile_number"]'
        self.create_account_button = 'button[data-qa="create-account"]'

        #assertion locaters
        self.account_created_heading = 'h2[data-qa="account-created"]'
        self.continue_button = 'a[data-qa="continue-button"]'

    def navigate_to_signup(self):
        self.logger.info("Navigate to initial signup page")
        self.page.click(self.signup_login_link)

    def fill_initial_signup(self, name: str, email: str):
        self.logger.info(f"Submitting initial signup for Name: {name}, Email: {email}")
        self.page.fill(self.signup_name_input, name)
        self.page.fill(self.signup_email_input, email)
        self.page.click(self.signup_button)

    def fill_account_and_address_info(
        self, password, first_name, last_name, day, month, year, country, address, state, city, zipcode, mobile
    ):
        self.logger.info("Filling detailed form with data passed from Test File...")
        
        # 1. Radio & Password
        self.page.check(self.gender_mr_radio)
        self.page.fill(self.password_input, password)
        
        # 2. Dropdowns (Main Path + Value)
        self.page.select_option(self.days_dropdown, day)
        self.page.select_option(self.months_dropdown, month)
        self.page.select_option(self.years_dropdown, year)
        
        # 3. Names & Address Fields
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.address_input, address)
        
        # 4. Country Dropdown
        self.page.select_option(self.country_dropdown, country)
        
        # 5. Remaining Address Fields
        self.page.fill(self.state_input, state)
        self.page.fill(self.city_input, city)
        self.page.fill(self.zipcode_input, zipcode)
        self.page.fill(self.mobile_input, mobile)
        self.page.click(self.create_account_button)


    def verify_account_creation_heading(self):
        self.logger.info("Getting the account created heading locators")
        return self.page.locator(self.account_created_heading)


    def click_continue(self):
        self.logger.info("Clicking on Continue button after registration")
        self.page.click(self.continue_button)





    


    








