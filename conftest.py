import pytest
from Utilities.Custom_Logger import CustomLogger
logger = CustomLogger.get_logger()

def pytest_html_results_summary(prefix, summary, postfix):
    #custom subtitle
    prefix.extend(["<p><b>Automation Framework:</b> Playwright API Testing Lifecycle</p>"])

def pytest_metadata(metadata):
    # Remove unnecessary default system
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
    metadata.pop("Platform", None)
    
    #Add own custom,
    metadata["Project Name"] = "Automation Exercise API"
    metadata["Tester Name"] = "Bimalesh Kumar"
    metadata["Environment"] = "QA/Production"