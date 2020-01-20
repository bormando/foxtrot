import pytest
import allure
from fixtures.application import Application


# noinspection SpellCheckingInspection
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser name")
    parser.addoption("--timeout", action="store", default="10", help="Implicitly wait timeout delay")
    parser.addoption("--hub_ip", action="store", default="localhost", help="Selenium hub IP address")
    parser.addoption("--hub_port", action="store", default="4444", help="Selenium hub port")


@pytest.fixture(autouse=True)
def app(request):
    with allure.step("Open browser"):
        browser_name = request.config.getoption("browser")
        timeout_delay = int(request.config.getoption("timeout"))
        hub_ip = request.config.getoption("hub_ip")
        hub_port = request.config.getoption("hub_port")
        hub = F"http://{hub_ip}:{hub_port}/wd/hub"
        app = Application(browser_name, timeout_delay, hub)
    yield app
    with allure.step("Quit browser"):
        app.wd.quit()
