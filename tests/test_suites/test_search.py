from core.web.Base import Base
from core.page.create_page import CreatePage
from tests.pages.search_page import SearchPage

import pytest
import allure
from core.decorators.DataProvider import data
from core.logger import log
  
  
@allure.story("User story")
@allure.feature("feature name")
class TestSearch(Base):
        
    @allure.testcase("test case name")
    def test_search(self):
        page = CreatePage.get(SearchPage, self.driver)
        page.search("test")
        assert False
        
    @data([("test",),("selenium",)])
    def test_search_1(self, query):
        log.info("test case started")
        page = CreatePage.get(SearchPage, self.driver)
        log.info("page initialized")
        page.search(query)
        assert self.driver.title.startswith(query), "title does not match"
