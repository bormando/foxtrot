from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class BasePageSelectors(object):
    SEARCH_FIELD = (By.CSS_SELECTOR, "#searchInput")
    SUGGESTIONS = (By.CSS_SELECTOR, "div.suggestions")
    LOG_IN = (By.CSS_SELECTOR, "#pt-login > a")
    RECENT_CHANGES = (By.CSS_SELECTOR, "#n-recentchanges > a")


class BasePage(object):
    def __init__(self, app):
        self.app = app

    def search_for(self, value):
        assert self.app.is_element_present(*BasePageSelectors.SEARCH_FIELD), "Search field is not found"
        search_field = self.app.wd.find_element(*BasePageSelectors.SEARCH_FIELD)
        search_field.send_keys(value)
        """ If you won't wait for search suggestions to load, 
        you'll get search page instead of first article that matches search query """
        try:
            self.app.wd.find_element(*BasePageSelectors.SUGGESTIONS)
        except NoSuchElementException:
            pass
        search_field.send_keys(Keys.ENTER)

    def go_to_log_in(self):
        assert self.app.is_element_present(*BasePageSelectors.LOG_IN), "'Log In' button is not found"
        log_in = self.app.wd.find_element(*BasePageSelectors.LOG_IN)
        log_in.click()

    def go_to_recent_changes(self):
        assert self.app.is_element_present(*BasePageSelectors.RECENT_CHANGES), "'Recent Changes' menu item is not found"
        recent_changes = self.app.wd.find_element(*BasePageSelectors.RECENT_CHANGES)
        recent_changes.click()
