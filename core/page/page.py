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

class Page(object):
    
    """
    Base class that all page models can inherit from
    """
    def __init__(self, driver, implicit_wait=10):
        self.base_url = CONFIG.get("application.url")
        self.driver = driver

    def _load(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def load(self):
        self._load(self.url)

    def is_loaded(self):
        return self.driver.current_url == (self.base_url + self.url)

    def run_script(self, src):
        return self.driver.execute_script(src)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element(loc).click()
            if clear_first:
                self.find_element(loc).clear()
            self.find_element(loc).send_keys(value)
        except AttributeError:
            print('{0} page does not have {0} locator'.format(self, loc))

    def fill_field(self, loc, value):
        self.find_element(loc).send_keys(value)

    def click_element(self, loc):
        self.find_element(loc).click()

    def click_and_hold(self, element):
        loc = self.find_element(element)
        ActionChains(self.driver).click_and_hold(loc).perform()
        ActionChains(self.driver).release(loc).perform()

    def select_option(self, select_field, select_option, select_method = 'label'):
        if type(select_field) is WebElement:
            select = Select(select_field)
        else:
            select = Select(self.find_element(select_field))
        if 'label' == select_method:
            select.select_by_visible_text(select_option)
        if 'value' == select_method:
            select.select_by_value(select_option)
        if 'index' == select_method:
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
        locator = (By.LINK_TEXT, link_name)
        self.click_element(locator)

    def submit_form(self,loc):
        self.find_element(loc).submit()

    def uplaod_file(self, file_path, loc):
        self.find_element(loc).send_keys(file_path)

    def wait_till_visible(self, by, loc, wait_time = 10):
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by, loc))

    def accept_alert(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present(), 'Timed out waiting for confirmation popup to appear.')
            alert = self.driver.switch_to_alert()
            alert.accept()
        except TimeoutException:
            print('No alert accepted')

    def press_enter_key(self, loc):
        if type(loc) is WebElement:
            loc.send_keys(Keys.ENTER)
        else:
            self.find_element(loc).send_keys(Keys.ENTER)

    def clear_and_send_value(self, value, loc):
        if type(loc) is not WebElement:
            element = self.find_element(loc)
        else:
            element = loc
        element.click()
        element.clear()
        element.send_keys(value)

    def close_message_popup(self):
        if self.is_element_present(self.system_message_dialog):
            self.click_element(self.system_message_dialog)
            self.click_element(self.system_message_dialog_close_link)

    def is_element_present(self, loc):
        try: self.find_element(loc)
        except NoSuchElementException: return False
        return True

    def link_not_exists(self, link):
        assert False == self.is_element_present(link)

    def link_exists(self, link):
        assert False == self.is_element_present(link)

    def get_content_value(self, loc):
        if type(loc) is not WebElement:
            element = self.find_element(loc)
        else:
            element = loc
        return element.get_attribute('value')

    def get_content_text(self, loc):
        if type(loc) is not WebElement:
            element = self.find_element(loc)
        else:
            element = loc
        return element.text

    def check_dropdown_options(self, option_list, loc):
        select = Select(self.find_element(loc))
        options_text = []
        for opt in select.options:
            options_text.append(opt.text.encode())
        for option in option_list:
            assert option in options_text, "Actaul/Obtained list :- {0}/{1}".format(option, options_text)

    def get_content_text_list(self, loc):
        elements = self.find_elements(loc)
        text_list = []
        for element in elements:
            text_list.append(element.text)
        return text_list

    def go_back(self):
        self.driver.back()

    def dismiss_alert(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(), 'Timed out waiting for confirmation popup to appear.')
            alert = self.driver.switch_to_alert()
            alert.dismiss()
        except TimeoutException:
            print('No alert accepted')

    def clear(self , loc):
        element = self.find_element(loc)
        element.clear()

    def page_refresh(self):
        self.driver.refresh()
