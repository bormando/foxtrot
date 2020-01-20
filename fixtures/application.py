from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
import time


class Application(object):
    def __init__(self, browser, timeout, hub):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument("--disable-notifications")
            options.add_experimental_option("w3c", False)
            options.add_argument("--lang=en")
            self.wd = webdriver.Remote(command_executor=hub,
                                       desired_capabilities=DesiredCapabilities.CHROME,
                                       options=options)
        else:
            assert False, F"Wrong browser name: '{browser}'"
        if type(timeout) == int and timeout >= 0:
            self.wd.implicitly_wait(timeout)
        else:
            assert False, F"Wrong timeout: '{timeout}'"
        self.wd.implicitly_wait(timeout)
        self.timeout = timeout
        self.hub = hub

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(how, what)
            return True
        except NoSuchElementException:
            return False

    def is_number_of_elements_present(self, number, how, what):
        elements_found = None
        for i in range(self.timeout * 4):
            elements = self.wd.find_elements(how, what)
            elements_found = len(elements)
            if elements_found == number:
                return elements_found
            else:
                time.sleep(0.25)
        return elements_found
