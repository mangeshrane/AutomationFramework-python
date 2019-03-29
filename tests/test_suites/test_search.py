from core.web.Base import Base
from core.page.create_page import CreatePage
from tests.pages.search_page import SearchPage

import allure
import pytest


@allure.story("User story")
@allure.feature("feature name")
class TestSearch(Base):

    @allure.testcase("test case name")
    def test_search(self):
        page = CreatePage.get(SearchPage, self.driver)
        page.search("test")

    def test_search_1(self, query):
        page = CreatePage.get(SearchPage, self.driver)
        page.search(query)
        assert self.driver.title.startswith(query), "title does not match"
