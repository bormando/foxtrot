from selenium.webdriver.common.by import By
from .base_page import BasePage


class ArticlePageSelectors(object):
    NAME = (By.CSS_SELECTOR, ".firstHeading")


class ArticlePage(BasePage):
    def check_article_name(self, name_to_find):
        assert self.app.is_element_present(*ArticlePageSelectors.NAME), "Error not found"
        article_name = self.app.wd.find_element(*ArticlePageSelectors.NAME)
        name_found = article_name.text
        assert name_found == name_to_find, F"Article name is '{name_found}', but should be '{name_to_find}'"
