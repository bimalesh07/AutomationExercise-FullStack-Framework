import pytest
from playwright.sync_api import sync_playwright
from Utilities.Read_Env import ReadEnv
from Utilities.Custom_Logger import CustomLogger
from API_Actions.User_Api_Action import UserAPIActions
from API_Actions.Prodduct_Api import ProductAPIActions


logger = CustomLogger.get_logger()

@pytest.fixture(scope="session")
def api_context(playwright): 
    logger.info("Backend API Request Client Context via Native Engine")
    
    base_api_url = ReadEnv.get_base_api()
    
    browser_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    request_context = playwright.request.new_context(
        base_url=base_api_url,
        extra_http_headers=browser_headers
    )
    
    yield request_context
    logger.info("Tearing down Backend API Context gracefully")
    request_context.dispose()
  

@pytest.fixture(scope="function")
def user_api(api_context):
    return UserAPIActions(api_context, logger)


@pytest.fixture(scope="function")
def product_api(api_context):
    return  ProductAPIActions(api_context, logger)





"""Manulay sart
@pytest.fixture(scope="session")
def api_context():
    logger.info("Spawning Backend API Request Client Context")
    
    playwright = sync_playwright().start()
    base_api_url = ReadEnv.get_base_api()
    
    browser_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    request_context = playwright.request.new_context(
        base_url=base_api_url,
        extra_http_headers=browser_headers
    )
    
    yield request_context
    logger.info("Tearing down Backend API Context")
    request_context.dispose()
    playwright.stop()"""