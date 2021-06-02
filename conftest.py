import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def browser(request):
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
