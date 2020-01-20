from selenium.webdriver.common.by import By
from .base_page import BasePage


class LogInPageSelectors(object):
    # Check it out, 4 different methods to set selectors
    USERNAME = (By.CSS_SELECTOR, "#wpName1")
    PASSWORD = (By.ID, "wpPassword1")
    KEEP_LOGGED_IN = (By.XPATH, "//input[@id='wpRemember']")
    LOG_IN = (By.NAME, "wploginattempt")
    ERROR = (By.CSS_SELECTOR, ".errorbox > p")


class LogInPage(BasePage):
    def enter_username(self, username):
        assert self.app.is_element_present(*LogInPageSelectors.USERNAME), "Username input not found"
        username_input = self.app.wd.find_element(*LogInPageSelectors.USERNAME)
        username_input.send_keys(username)

    def enter_password(self, password):
        assert self.app.is_element_present(*LogInPageSelectors.PASSWORD), "Password input not found"
        password_input = self.app.wd.find_element(*LogInPageSelectors.PASSWORD)
        password_input.send_keys(password)

    def keep_logged_in(self):
        assert self.app.is_element_present(*LogInPageSelectors.KEEP_LOGGED_IN), "'Keep logged in' checkbox not found"
        checkbox = self.app.wd.find_element(*LogInPageSelectors.KEEP_LOGGED_IN)
        checkbox.click()

    def log_in(self):
        assert self.app.is_element_present(*LogInPageSelectors.LOG_IN), "Log in button not found"
        log_in = self.app.wd.find_element(*LogInPageSelectors.LOG_IN)
        log_in.click()

    def wrong_username_or_password_error(self):
        assert self.app.is_element_present(*LogInPageSelectors.ERROR), "Error not found"
        error = self.app.wd.find_element(*LogInPageSelectors.ERROR)
        error_text = error.text
        assert "Incorrect username or password" in error_text, F"Error text is different: '{error_text}'"
