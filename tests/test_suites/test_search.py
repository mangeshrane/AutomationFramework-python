from core.web.Base import Base
from core.page.create_page import CreatePage
from tests.pages.search_page import SearchPage


class TestSearch(Base):
    
    def test_search(self):
        page = CreatePage.get(SearchPage, self.driver)
        page.search("test")
        
        