from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from selenium import webdriver

@pytest.fixture(scope="class", autouse=True)
def setup(request, browser, url):
    if browser == "chrome":
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif browser == "edge":
        service = Service(executable_path=EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")

# @pytest.fixture(scope="function", autouse=True)
# def setup(request):
#     service = Service(executable_path=ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#     driver.get("http://live.techpanda.org/")
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.close()