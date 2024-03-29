from tests.pages.search_page import SearchPage
     
import allure
from core.web.create_page import CreatePage
from core.web.webtest import WebTest
import pytest
import time
     
     
@allure.story("User story")
@allure.feature("feature name")
class TestSearch(WebTest):
       
    # USING GROUPS eg. 'smoke'
    @pytest.mark.smoke
    def test_search(self):
        page = CreatePage.get(SearchPage, self.driver)
        print(page.search_field.text)
        page.search("test")
        time.sleep(2)
        assert self.driver.title.startswith("test"), "title does not match"
