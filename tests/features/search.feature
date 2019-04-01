Feature: Search
    Search using query to get results

Scenario: Enter query to search to get result
    Given I'm on search page
    When I enter query into searchbox and press enter
    Then query related search results should be displayed
