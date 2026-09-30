import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


DEFAULT_URL = "https://practice-automation.com/iframes/"


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser: chrome or firefox",
    )
    parser.addoption(
        "--url",
        action="store",
        default=DEFAULT_URL,
        help="URL of the page under test",
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser").lower()

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        web_driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("-headless")
        web_driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError(
            f"Unknown browser '{browser_name}'. Use chrome or firefox."
        )

    web_driver.implicitly_wait(0)
    try:
        yield web_driver
    finally:
        web_driver.quit()


@pytest.fixture
def url(request):
    return request.config.getoption("--url")
