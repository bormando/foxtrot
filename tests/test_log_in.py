import pytest
from pytest_bdd import scenario
from steps.main import *
from steps.log_in import *
import allure


@pytest.mark.smoke
@pytest.mark.run(order=3)
@allure.feature("Log In")
@allure.title("Log in with wrong login and password")
@scenario("../features/log_in.feature", "Log in with wrong login and password")
def test_log_in_with_wrong_login_and_password():
    pass
