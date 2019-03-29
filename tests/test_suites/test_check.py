import traceback
import sys
from contextlib import contextmanager
from core.page.create_page import CreatePage
from tests.pages.search_page import SearchPage
from core.web.Base import Base
import pytest

class TestCheck(Base):
      
    def test_search_2(self):
        page = CreatePage.get(SearchPage, self.driver)
        page.search("test")
        assert False
       
    def test_data(self, a, b):
        print(a, b)
