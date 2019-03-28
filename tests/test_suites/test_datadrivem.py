'''
Created on Mar 28, 2019

@author: mrane
'''
import pytest
from core.page.create_page import CreatePage
from tests.pages.search_page import SearchPage
from core.web.Base import Base


class TestSearch(Base):
 
    @pytest.mark.parametrize('query, test', [("selenium", 12),
                                             ("QTP, 0")])
    def test_search_1(self, query, test):
        page = CreatePage.get(SearchPage, self.driver)
        page.search(query)
        assert self.driver.title.startswith(query), "title does not match"