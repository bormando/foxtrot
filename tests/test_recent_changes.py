import pytest
from pytest_bdd import scenario
from steps.main import *
from steps.recent_changes import *
import allure


@pytest.mark.smoke
@pytest.mark.run(order=2)
@allure.feature("Recent Changes")
@allure.title("Show selected number of changes")
@scenario("../features/recent_changes.feature", "Show selected number of changes")
def test_show_selected_number_of_changes():
    pass
