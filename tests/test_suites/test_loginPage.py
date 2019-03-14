'''
Created on Mar 14, 2019

@author: mrane
'''
from core.page.create_page import CreatePage
from tests.pages.LoginPage import LoginPage
from core.web.Base import Base
from core.configuration import CONFIG
import time

class TestLoginPage(Base):
    '''
    classdocs
    '''
    
    def test_login(self):
        page = CreatePage.get(LoginPage, self.driver)
        page.login(CONFIG.get("application.username"), CONFIG.get("application.password"))
        time.sleep(5)