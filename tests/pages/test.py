

from tests.pages.LoginPage import LoginPage
from selenium import webdriver
from core.page.create_page import CreatePage
import unittest
from core.decorators.expect import expect_exception
from core.decorators.DataProvider import data, dataFile
from core.decorators.test import Test

# driver = webdriver.Chrome(r"C:\Users\mrane\Downloads\chromedriver.exe")
# login = CreatePage.get(LoginPage, driver)
# login.loginBtn.send_keys("selenium")


class test(unittest.TestCase):
    
    
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
    
    
    @dataFile(r"D:\Workspace\AutomationFramework-Java\src\test\resources\testData\data.xlsx", "Add Customer")
    @Test
    def test_case_1(self, *args):
        print("test case 1", args)
    
    @dataFile(r"C:\Users\mrane\Downloads\data.csv", headers=False)
    def test_case_2(self, *args):
        print("test case 2", args)
    
    @dataFile(r"C:\Users\mrane\Downloads\data.json", headers=False)
    def test_case_3(self, *args):
        print("test case 3", args)