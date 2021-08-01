import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox",choices=("chrome", "firefox"))
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language")


def chrome_parametr(language ):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    return webdriver.Chrome( options=options )

def firefox_parametr (language  ):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", language)
    return webdriver.Firefox(firefox_profile=fp)

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language") 
    used_browser = { "chrome":chrome_parametr, "firefox":firefox_parametr }
    browser = used_browser[ browser_name ](language)
    yield browser
    # print(f"\nquit  browser..")
    browser.quit()