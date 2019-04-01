"""Search feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from core.page.create_page import CreatePage
from tests.pages.search_page import SearchPage

page = None

@scenario('../features/search.feature', 'Enter query to search to get result')
def test_enter_query_to_search_to_get_result():
    """Enter query to search to get result."""
    
@given("I'm on search page")
def im_on_search_page(browser):
    """I'm on search page."""
    page = CreatePage.get(SearchPage, browser)
    return dict(page=page)
    
@when('I enter query into searchbox and press enter')
def i_enter_query_into_searchbox_and_press_enter(im_on_search_page, browser):
    """I enter query into searchbox and press enter."""
    im_on_search_page['page'].search("test")

@then('query related search results should be displayed')
def query_related_search_results_should_be_displayed(browser):
    """query related search results should be displayed."""
    assert browser.title.startswith("es"), "title does not match"