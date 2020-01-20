from pytest_bdd import when
from pages.main_page import MainPage
import allure


@when("open main page")
def open_main_page(app):
    with allure.step("When open main page"):
        main_page = MainPage(app)
        main_page.open()


@when("search for <value>")
def search_for_value(app, value):
    with allure.step(F"When search for {value}"):
        main_page = MainPage(app)
        main_page.search_for(value)


@when("go to log in page")
def go_to_log_in(app):
    with allure.step("When go to log in page"):
        main_page = MainPage(app)
        main_page.go_to_log_in()


@when("go to recent changes page")
def go_to_recent_changes(app):
    with allure.step("When go to recent changes page"):
        main_page = MainPage(app)
        main_page.go_to_recent_changes()
