'''
Created on Mar 14, 2019
 
@author: mrane
'''
from tests.pages.LoginPage import LoginPage
from core.configuration import CONFIG
import time
 
import pytest
from tests.pages.dashboard import Dashboard
from core.web.create_page import CreatePage
from core.web.webtest import WebTest
from core.logger import LOG
 
class TestLoginPage(WebTest):
    '''
    classdocs
    '''
 
    @pytest.mark.run(before="test_login")
    def test_login(self):
        print("running login")
        page = CreatePage.get(LoginPage, self.driver)
        page = page.login(CONFIG.get("application.username"), CONFIG.get("application.password"))
        LOG.info("PAGE TITLE " + self.driver.title)
 
    def test_accounts(self):
        page = CreatePage.get(Dashboard, self.driver)
        page.click_on_accounts()
        time.sleep(5)

