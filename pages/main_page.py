from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPageSelectors(object):
    SEARCH_FIELD = (By.CSS_SELECTOR, "#searchInput")
    LOG_IN = (By.CSS_SELECTOR, "#pt-login > a")


class MainPage(BasePage):
    def open(self):
        self.app.wd.get("https://en.wikipedia.org")
