

from tests.pages.LoginPage import LoginPage
from selenium import webdriver

l = LoginPage(webdriver.Chrome(r"C:\Users\mrane\Downloads\chromedriver.exe"))
print(LoginPage.loginBtn)