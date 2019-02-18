

from tests.pages.LoginPage import LoginPage
from selenium import webdriver
from core.page.create_page import CreatePage
import unittest
from core.decorators.expect import expect_exception
from core.decorators.DataProvider import data, dataFile
from core.decorators.test import Test
from core import decorators
from core.browsers.web_drivers import WebDrivers
from core.reporter.extent import HTMLTestRunner


##############################################################################
# Facilities for running tests from the command line
##############################################################################

# Note: Reuse unittest.TestProgram to launch test. In the future we may
# build our own launcher to support more specific command line
# # parameters like test title, CSS, etc.
# class TestProgram(unittest.TestProgram):
#     """
#     A variation of the unittest.TestProgram. Please refer to the base
#     class for command line parameters.
#     """
#     
# 
# driver = WebDrivers().get()
# login = CreatePage.get(LoginPage, driver)
# login.loginBtn.send_keys("selenium")
if __name__ == "__main__":
    main(module=None)

class test(unittest.TestCase):
    def runTests(self):
        if self.testRunner is None:
            self.testRunner = HTMLTestRunner(verbosity=self.verbosity)
        unittest.TestProgram.runTests(self)
        
    main = TestProgram

##############################################################################
# Executing this module from the command line
##############################################################################


     
    def setUp(self):
        print("setup")
         
    def tearDown(self):
        print("tearDown")
         
    @classmethod
    def setUpClass(cls):
        print("setupClass")
       
    @classmethod
    def tearDownClass(cls):
        print("tear Down Clas")
     
    @expect_exception(AssertionError)
    def test_case(self):
        print("test case")
        raise AssertionError("Not found")
     
    @Test
    @dataFile(r"D:\Workspace\AutomationFramework-Java\src\test\resources\testData\data.xlsx", "Add Customer")
    def test_case_1(self, *args):
        print("test case 1", args)
     
    @dataFile(r"C:\Users\mrane\Downloads\data.csv", headers=False)
    def test_case_2(self, *args):
        print("test case 2", args)
        print(decorators.test.k)
     
    @dataFile(r"C:\Users\mrane\Downloads\data.json", headers=False)
    def test_case_3(self, *args):
        print("test case 3", args)