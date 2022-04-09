import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Enter browser language: example 'es', 'ru' etc.")


@pytest.fixture()
def browser(request):
    browser_language = request.config.getoption("language")
    browser_option = Options()
    browser_option.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    service = Service(executable_path="webdrivers/chromedriver.exe")
    browser = webdriver.Chrome(service=service, options=browser_option)
    yield browser
    browser.quit()
