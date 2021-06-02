import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
