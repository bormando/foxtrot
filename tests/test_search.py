import pytest
from pytest_bdd import scenario
from steps.main import *
from steps.article import *
import allure


@pytest.mark.smoke
@pytest.mark.run(order=1)
@allure.feature("Search")
@allure.title("Specific result found")
@scenario("../features/search.feature", "Specific result found")
def test_specific_result_found():
    pass
