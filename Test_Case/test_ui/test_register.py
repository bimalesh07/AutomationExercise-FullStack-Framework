import random
from playwright.sync_api import Page, expect
from PageObjects.Registeration_Page import RegistrationPage
from Utilities.Read_Env import ReadEnv

class TestRegistrations:


    def test_user_registration_flow(self, ui_page):
        # Unpack fixture
        page, logger = ui_page
        page: Page = page
        
        #random email
        random_id = random.randint(1000, 9999)
        test_email = f"bimalesh_auto_{random_id}@gmail.com"
        #test_email = ReadEnv.get_email()
        test_password = ReadEnv.get_password()
        test_name = "bimalesh"

        # Initialize Page Object
        register = RegistrationPage(page, logger)
        
        logger.info("******** Start Registrations test flow ********")
        register.navigate_to_signup()
        register.fill_initial_signup(test_name, test_email)

        
        register.fill_account_and_address_info(
            password=test_password,
            first_name="Bimalesh",
            last_name="Automation",
            day="15",               
            month="August",         
            year="1996",            
            country="India",      
            address="123 Automation Lane, Tech Park",
            state="Karnataka",
            city="Bengaluru",
            zipcode="560001",
            mobile="9876543210"
        )
        logger.info("******** Registration Form Submitted Successfully ********")
        logger.info(" ********* Now Verifying Sucess Message *************")

        sucess_heading = register.verify_account_creation_heading()
        expect(sucess_heading).to_be_visible
        logger.info("Assertion Passed: 'ACCOUNT CREATED!' message is visible on screen.")

        register.click_continue()
        logger.info("******** Registration Flow Completed Successfully! ********")




