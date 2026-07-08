import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from Utilities.Custom_Logger import CustomLogger


logger = CustomLogger.get_logger()
load_dotenv()

@pytest.fixture(scope="session")
def api_context():
    logger.info("[SESSION FIXTURE] Spawning Backend API Request Client Context")
    with sync_playwright() as p:
        base_api_url = os.getenv("API_BASE_URL")
        request_context = p.request.new_context(base_url=base_api_url)
        yield request_context
        logger.info("[SESSION FIXTURE] Tearing down Backend API Context")
        request_context.dispose()


@pytest.fixture(scope="function")
def ui_page():
    logger.info("[FUNCTION FIXTURE] Opening Isolated Browser Tab Context")
    with sync_playwright() as p:
        base_ui_url = os.getenv("BASE_URL")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(base_ui_url)
        
        yield page, logger
        
        logger.info("[FUNCTION FIXTURE] Closing Browser Tab and Clearing State")
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def logged_in_page(ui_page):
    page, logger = ui_page
    logger.info("[FIXTURE HELP] Automatically authenticating user via Page Object...")
    
    login_page = LoginPage(page, logger)
    login_page.login_to_application("bhai_test@gmail.com", "secure_password123")
    
    yield page, logger