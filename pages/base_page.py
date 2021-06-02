from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def switch_to_last_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[-1])
