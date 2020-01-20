from pytest_bdd import then
from pages.article_page import ArticlePage
import allure


@then("found <result>")
def check_number_of_changes_shown(app, result):
    with allure.step("Then found <result>"):
        article_page = ArticlePage(app)
        article_page.check_article_name(result)
