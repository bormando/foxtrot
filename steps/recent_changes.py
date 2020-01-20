from pytest_bdd import when, then
from pages.recent_changes_page import RecentChangesPage
import allure


@when("select <number> changes to show")
def select_period(app, number):
    with allure.step("When select <number> changes to show"):
        recent_changes_page = RecentChangesPage(app)
        recent_changes_page.select_period(number)


@then("<number> changes shown")
def check_number_of_changes_shown(app, number):
    with allure.step("Then <number> changes shown"):
        recent_changes_page = RecentChangesPage(app)
        recent_changes_page.check_number_of_changes_shown(number)
