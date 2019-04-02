from core.page.page import Page
from core.page.element import Element
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SearchPage(Page):

    def __init__(self, driver):
        self.driver = driver

    search_field = Element(By.NAME, "q", 0)

    def load(self):
        self.driver.get("http://google.com")

    def is_loaded(self):
        Page.is_loaded(self)

    def search(self, query):
        self.search_field.send_keys(query + Keys.ENTER)

