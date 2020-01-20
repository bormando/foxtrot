from selenium.webdriver.common.by import By
from .base_page import BasePage


class RecentChangesPageSelectors(object):
    PERIOD_SELECTOR = (By.CSS_SELECTOR, ".mw-rcfilters-ui-changesLimitAndDateButtonWidget > span > a")
    CHANGES = (By.CSS_SELECTOR, ".mw-changeslist-line-inner")


class RecentChangesPage(BasePage):
    def select_period(self, number):
        assert self.app.is_element_present(*RecentChangesPageSelectors.PERIOD_SELECTOR), "Period selector not found"
        period_selector = self.app.wd.find_element(*RecentChangesPageSelectors.PERIOD_SELECTOR)
        period_selector.click()
        period = \
            self.app.wd.find_element(
                By.XPATH,
                F"//div[contains(@class, 'mw-rcfilters-ui-changesLimitPopupWidget')]//span[.='{number}']"
            )
        period.click()

    def check_number_of_changes_shown(self, number):
        # List of recent changes updates when some time pass, so you'll have to either sleep or use this magic below
        assert self.app.is_element_present(*RecentChangesPageSelectors.CHANGES), "No changes found"
        changes_should_be = int(number)
        changes_found = self.app.is_number_of_elements_present(changes_should_be, *RecentChangesPageSelectors.CHANGES)
        assert changes_found == changes_should_be, \
            F"{changes_found} changes found, but should be {changes_should_be}"
