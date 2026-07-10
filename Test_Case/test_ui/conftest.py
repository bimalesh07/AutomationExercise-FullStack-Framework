import pytest
import os
from playwright.sync_api import sync_playwright
from Utilities.Read_Env import ReadEnv
from Utilities.Custom_Logger import CustomLogger
from PageObjects.Login_Page import LoginPage

logger = CustomLogger.get_logger()

@pytest.fixture(scope="function")
def ui_page():
    logger.info("[UI FIXTURE] Opening Isolated Browser Tab Context")
    playwright_instance = sync_playwright().start()
    base_ui_url = ReadEnv.get_base_url()
    
    browser = playwright_instance.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(base_ui_url)
    
    yield page, logger 
    
    logger.info("[UI FIXTURE] Closing Browser Tab")
    context.close()
    browser.close()
    playwright_instance.stop()


#Login 
@pytest.fixture(scope="function")
def logged_in_page(ui_page):
    page, logger = ui_page

    logger.info("Logging in for background setup ===")
    email = ReadEnv.get_email()
    password = ReadEnv.get_password()

    login_page = LoginPage(page, logger)
    login_page.navigate_loginpage()
    login_page.Login_with_credentials(email, password)

    logger.info("Browser session is authenticated ===")
    yield page, logger

    logger.info("Cleaning up session ")














#SCREENSHOT HOOK
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
   
    if report.when == "call" and report.failed:
        logger.info(f"[UI REPORT HOOK] Test Failed: {item.name}. Taking screenshot...")
        
        # ui_page fixture se page object nikaala
        ui_page_tuple = item.funcargs.get("ui_page")
        if ui_page_tuple:
            page = ui_page_tuple[0] 
            
            screenshot_dir = "Screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            
            # Playwright savescreeshots
            page.screenshot(path=screenshot_path)
            
            # in HTML  report scressn shots add
            pytest_html = item.config.pluginmanager.getplugin('html')
            if pytest_html:
                extra = getattr(report, 'extra', [])
                extra.append(pytest_html.extras.image(screenshot_path))
                report.extra = extra
                logger.info(f"[UI REPORT HOOK] Screenshot attached to HTML report.")