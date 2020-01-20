from pytest_bdd import when, then
from pages.log_in_page import LogInPage
import allure


@when("enter username <username>")
def enter_username(app, username):
    with allure.step("When enter username <username>"):
        log_in_page = LogInPage(app)
        log_in_page.enter_username(username)


@when("enter password <password>")
def enter_password(app, password):
    with allure.step("When enter password <password>"):
        log_in_page = LogInPage(app)
        log_in_page.enter_password(password)


@when("check option to keep logged in")
def keep_logged_in(app):
    with allure.step("When check option to keep logged in"):
        log_in_page = LogInPage(app)
        log_in_page.keep_logged_in()


@when("press log in button")
def log_in(app):
    with allure.step("When press log in button"):
        log_in_page = LogInPage(app)
        log_in_page.log_in()


@then("log in error pops up")
def log_in(app):
    with allure.step("Then log in error pops up"):
        log_in_page = LogInPage(app)
        log_in_page.wrong_username_or_password_error()
