import traceback
import sys
from contextlib import contextmanager
from core.page.create_page import CreatePage
from tests.pages.search_page import SearchPage
from core.web.Base import Base
import pytest
from core.decorators.DataProvider import data

class TestCheck(Base):
     
    @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
    def test_search_2(self):
        page = CreatePage.get(SearchPage, self.driver)
        page.search("test")
        assert False
      
    @data([[1, 2], [4, 4], [5, 5]])
    def test_data(self, a, b):
        print(a, b)
