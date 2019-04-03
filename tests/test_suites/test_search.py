from tests.pages.search_page import SearchPage
  
import allure
from core.web.create_page import CreatePage
from core.web.webtest import WebTest
  
  
@allure.story("User story")
@allure.feature("feature name")
class TestSearch(WebTest):
  
    @allure.testcase("test case name")
    def test_search(self):
        page = CreatePage.get(SearchPage, self.driver)
        page.search("test")
        assert self.driver.title.startswith("test"), "title does not match"
