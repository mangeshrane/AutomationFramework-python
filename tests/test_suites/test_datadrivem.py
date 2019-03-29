'''
Created on Mar 28, 2019

@author: mrane
'''
import pytest
from core.page.create_page import CreatePage
from tests.pages.search_page import SearchPage
from core.web.Base import Base
from core.data_providers.data_provider import get_data
 
class TestSearch(Base):

    @pytest.mark.parametrize("query, test", [('selenium',0), ('QTP',1)])
    def test_search_1(self, query, test):
        print(test)
        page = CreatePage.get(SearchPage, self.driver)
        page.search(query)
        assert self.driver.title.startswith(query), "title does not match"
          
    @pytest.mark.parametrize(*get_data("users.csv", fields=["first_name", "last_name"]))
    def test_params_from_csv(self, first_name, last_name):
        print(first_name, last_name)

         
        