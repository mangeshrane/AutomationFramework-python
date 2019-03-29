'''
Created on Mar 28, 2019

@author: mrane
'''
import pytest
from core.page.create_page import CreatePage
from tests.pages.search_page import SearchPage
from core.web.Base import Base
from core.data_providers.data_provider import get_data
from core.browsers.web_drivers import WebDrivers

 
class TestSearch(Base):
      
    @pytest.mark.parametrize("a, b", [(1, 2),
                                      (3, 4)])
    def test_add(self, a, b):
        print(a+b)
        
    @pytest.mark.parametrize("query, test", [('selenium',0), ('QTP',1)])
    def test_search_1(self, query, test):
        page = CreatePage.get(SearchPage, self.driver)
        page.search(query)
        assert self.driver.title.startswith(query), "title does not match"
         
     
#     @pytest.mark.parametrize(get_data("users.csv"))
#     def test_params_from_csv(self, first_name, last_name):
#         print(first_name, last_name)
# @pytest.mark.usefixtures("web_driver")
# class fixture():
#     
#     @pytest.fixture(scope="class", autouse=True)
#     def web_driver(self, request):
#         self.driver = WebDrivers().get()
#         request.cls.driver = self.driver        
#         yield 
#         # Close browser window:
#         self.driver.quit()
# 
# class TestAdd(fixture):
#     
#     @pytest.mark.parametrize("a, b", [(1, 2),
#                                       (3, 4)])
#     def test_add(self, a, b):
#         print(a+b)
#         
    def test_print(self):
        print("print")
        