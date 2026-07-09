import pytest
from playwright.sync_api import Page, expect


class RegistrationPage:

    def __init__(self, page: Page, logger):
        self.page = page
        self.logger = logger

        # SELECTORS (Initial Signup)
        self.signup_login_link = page.locator('.shop-menu a[href="/login"]')
        self.signup_name_input = page.locator('input[data-qa="signup-name"]')
        self.signup_email_input = page.locator('input[data-qa="signup-email"]')
        self.signup_button = page.locator('button[data-qa="signup-button"]')

        # SCREEN 2 SELECTORS (Account Information)
        self.gender_mr_radio = page.locator('input[id="id_gender1"]')
        self.password_input = page.locator('input[id="password"]')

        # DROPDOWN MAIN PATHS
        self.days_dropdown = page.locator('select[id="days"]')
        self.months_dropdown = page.locator('select[id="months"]')
        self.years_dropdown = page.locator('select[id="years"]')
        self.country_dropdown = page.locator('select[id="country"]')

        # Address Fields
        self.first_name_input = page.locator('input[id="first_name"]')
        self.last_name_input = page.locator('input[id="last_name"]')
        self.address_input = page.locator('input[id="address1"]')
        self.state_input = page.locator('input[id="state"]')
        self.city_input = page.locator('input[id="city"]')
        self.zipcode_input = page.locator('input[id="zipcode"]')
        self.mobile_input = page.locator('input[id="mobile_number"]')
        self.create_account_button = page.locator(
            'button[data-qa="create-account"]'
        )

        # Assertion locators
        self.account_created_heading = page.locator(
            'h2[data-qa="account-created"]'
        )
        self.continue_button = page.locator('a[data-qa="continue-button"]')

        self.signup_error_message = page.locator("[style='color: red;']").first

    def navigate_to_signup(self):
        self.logger.info("Navigate to initial signup page")
        self.signup_login_link.click()

    def fill_initial_signup(self, name: str, email: str):
        self.logger.info(
            f"Submitting initial signup for Name: {name}, Email: {email}"
        )
        self.signup_name_input.fill(name)
        self.signup_email_input.fill(email)
        self.signup_button.click()


    def fill_account_and_address_info(
        self,
        password,
        first_name,
        last_name,
        day,
        month,
        year,
        country,
        address,
        state,
        city,
        zipcode,
        mobile,
    ):
        self.logger.info(
            "Filling detailed form with data passed from Test File..."
        )

        # Radio & Password
        self.gender_mr_radio.check()
        self.password_input.fill(password)

        #Dropdowns
        self.days_dropdown.select_option(day)
        self.months_dropdown.select_option(month)
        self.years_dropdown.select_option(year)

        # 3. Names & Address Fields
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.address_input.fill(address)

        # Country Dropdown
        self.country_dropdown.select_option(country)

        #Remaining Address Fields
        self.state_input.fill(state)
        self.city_input.fill(city)
        self.zipcode_input.fill(zipcode)
        self.mobile_input.fill(mobile)
        self.create_account_button.click()

    def verify_account_creation_heading(self):
        self.logger.info("Returning the account created heading locator")
        return self.account_created_heading

    def click_continue(self):
        self.logger.info("Clicking on Continue button after registration")
        self.continue_button.click()
