import pytest
import os

from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from utils import attach

PROJECT_ROOT_PATH = os.path.dirname(__file__)
print(PROJECT_ROOT_PATH)
RESOURCE_PATH = os.path.abspath(os.path.join(PROJECT_ROOT_PATH, 'resources'))

@pytest.fixture(scope="function", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope="function")
def setup_browser():

    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1028
    browser_version = "100.0"
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
