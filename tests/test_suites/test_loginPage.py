'''
Created on Mar 14, 2019

@author: mrane
'''
from core.page.create_page import CreatePage
from tests.pages.LoginPage import LoginPage
from core.web.Base import Base
from core.configuration import CONFIG
import time

import pytest
from pytest_dependency import depends
from tests.pages.dashboard import Dashboard

class TestLoginPage(Base):
    '''
    classdocs
    '''

    @pytest.mark.run(before="test_login")
    def test_login_1(self):
        print("running login")
        page = CreatePage.get(LoginPage, self.driver)
        page = page.login(CONFIG.get("application.username"), CONFIG.get("application.password"))

    def test_login(self):
        page = CreatePage.get(Dashboard, self.driver)
        page.click_on_accounts()
        time.sleep(5)

