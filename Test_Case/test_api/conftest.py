import pytest
from playwright.sync_api import sync_playwright
from Utilities.Read_Env import ReadEnv
from Utilities.Custom_Logger import CustomLogger
from API_Actions.User_Api_Action import UserAPIActions

# Root wale logger ko yahan import kiya
logger = CustomLogger.get_logger()

@pytest.fixture(scope="session")
def api_context():
    logger.info("[API FIXTURE] Spawning Backend API Request Client Context")
    
    playwright_instance = sync_playwright().start()
    base_api_url = ReadEnv.get_base_api()
    request_context = playwright_instance.request.new_context(base_url=base_api_url)
    
    yield request_context
    
    logger.info("[API FIXTURE] Tearing down Backend API Context")
    request_context.dispose()
    playwright_instance.stop()



@pytest.fixture(scope="function")
def user_api(api_context):
    return UserAPIActions(api_context, logger)