'''
Created on Feb 5, 2019

@author: mrane
'''
from selenium.webdriver.common.by import By
from core.configuration import CONFIG
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from abc import ABC, abstractmethod
from core.page.element import Element
from builtins import str

class Page(ABC):
    
    """
    Base class that all page models can inherit from
    """
    def __init__(self, driver, implicit_wait=10):
        self.base_url = CONFIG.get("application.url")
        super().__init__(driver)
        self.driver = driver

    def _load(self, url):
        url = self.base_url + url
        self.driver.get(url)
    
    @abstractmethod
    def load(self):
        pass
    
    @abstractmethod
    def is_loaded(self):
        pass

    def run_script(self, src):
        return self.driver.execute_script(src)

    def click_and_hold(self, element):
        loc = self.find_element(element)
        ActionChains(self.driver).click_and_hold(loc).perform()

    def select_option(self, select_field, select_option, select_method='label'):
        if isinstance(select_field, Element):
            select = Select(select_field)
        elif isinstance(select_field, str):
            select = Select(self.driver.find_element(select_field))
        if 'label' == select_method:
            select.select_by_visible_text(select_option)
        elif 'value' == select_method:
            select.select_by_value(select_option)
        elif 'index' == select_method:
            select.select_by_index(select_option)

    def page_should_contain(self, string):
        assert string in self.driver.page_source, "Content doesn't match. Message is {0}".format(string)

    def page_should_not_contain(self, string):
        assert string not in self.driver.page_source, "Content doesn't match. Message is {0}".format(string)

    def get_id_from_link(self, link):
        loc = (By.LINK_TEXT, link)
        href = self.find_element(loc).get_attribute('href')
        split_list = href.split('?locale=en')
        split_list_first_element = split_list[1]
        first_element_split_list = split_list_first_element.split("/")
        return first_element_split_list[-1]

    def get_last_element(self, loc):
        element_list = self.find_elements(loc)
        return element_list[-1]

    def get_element_by_index(self, index, loc):
        element_list = self.find_elements(loc)
        return element_list[index - 1]

    def go_to_link(self, link_name):
        locator = Element(By.LINK_TEXT, link_name)
        locator.click()

    def upload_file(self, element, filepath):
        element.send_keys(filepath)

    def accept_alert(self, wait=CONFIG.get("webdriver.wait.short")):
        try:
            WebDriverWait(self.driver, wait).until(EC.alert_is_present(), 'Timed out waiting for confirmation popup to appear.')
            alert = self.driver.switch_to_alert()
            alert.accept()
            return True
        except TimeoutException:
            print('No alert accepted')
            return False

    def press_enter_key(self, loc):
        if type(loc) is WebElement:
            loc.send_keys(Keys.ENTER)
        else:
            self.find_element(loc).send_keys(Keys.ENTER)

    def clear_and_send_keys(self, element, keys):
        if isinstance(element, Element):
            pass
        else:
            raise ValueError("Needed element of type Element")
        element.click()
        element.clear()
        element.send_keys(keys)

    def is_element_present(self, loc):
        try: 
            self.find_element(loc)
        except NoSuchElementException: 
            return False
        return True

    def get_content_value(self, element):
        return element.get_attribute('value')

    def get_content_text(self, element):
        return element.text

    def go_back(self):
        self.driver.back()

    def dismiss_alert(self, wait=CONFIG.get("webdriver.wait.short")):
        try:
            WebDriverWait(self.driver, wait).until(EC.alert_is_present(), 'Timed out waiting for confirmation popup to appear.')
            alert = self.driver.switch_to_alert()
            alert.dismiss()
        except TimeoutException:
            print('No alert accepted')
