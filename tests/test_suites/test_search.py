from core.web.Base import Base
from core.page.create_page import CreatePage
from tests.pages.search_page import SearchPage

import pytest
import allure


@allure.story("User story")
@allure.feature("feature name")
class TestSearch(Base):
    
    @allure.testcase("test case name")
    def test_search(self):
        page = CreatePage.get(SearchPage, self.driver)
        page.search("test")
        
    @allure.testcase("test case name")
    def test_search_1(self):
        page = CreatePage.get(SearchPage, self.driver)
        page.search("test")
        assert False