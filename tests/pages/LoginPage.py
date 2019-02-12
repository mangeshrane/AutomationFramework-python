from core.page.page import Page
from core.page.element import Element
from selenium.webdriver.common.by import By
from tests.pages.dashboard import Dashboard


class LoginPage(Page):
    
    username = Element(By.XPATH, "/html/body/div/form[1]//input[@name='email']")
    password = Element(By.XPATH, "/html/body/div/form[1]//input[@name='password']")
    rememberMe = Element(By.XPATH, "/html/body/div/form[1]//label/div/ins[@class='iCheck-helper']")
    forgotPassword = Element(By.XPATH, "//a[@id='link-forgot']/strong[.='Forget Password']")
    # loginBtn = Element(By.XPATH, "/html/body/div/form[1]/button[@type='submit']")
    loginBtn = Element(By.NAME, "q")
    
    def __init__(self, driver):
        self.driver = driver
        
    def login(self, uname, passwd):
        self.username.send_keys(uname)
        self.password.send_keys(passwd)
        self.loginBtn.click()
        return Dashboard(self.driver)
    
    def load(self):
        self.driver.get("http://google.com")
        
    def is_loaded(self):
        assert self.loginBtn.is_displayed(), "Not displayed" 