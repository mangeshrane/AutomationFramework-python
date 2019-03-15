from core.page.page import Page
from core.page.element import Element
from selenium.webdriver.common.by import By
from tests.pages.dashboard import Dashboard
from core.page.create_page import CreatePage
from core.configuration import CONFIG


class LoginPage(Page):
    
    username = Element(By.XPATH, "/html/body/div/form[1]//input[@name='email']", CONFIG.get("webdriver.wait.short"))
    password = Element(By.XPATH, "/html/body/div/form[1]//input[@name='password']", CONFIG.get("webdriver.wait.short"))
    rememberMe = Element(By.XPATH, "/html/body/div/form[1]//label/div/ins[@class='iCheck-helper']")
    forgotPassword = Element(By.XPATH, "//a[@id='link-forgot']/strong[.='Forget Password']")
    loginBtn = Element(By.XPATH, "/html/body/div/form[1]/button[@type='submit']", CONFIG.get("webdriver.wait.short"))
    
    def __init__(self, driver):
        self.driver = driver
        
    def login(self, uname, passwd):
        self.username.send_keys(uname)
        self.password.send_keys(passwd)
        self.loginBtn.click()
        return CreatePage.get(Dashboard, self.driver)
    
    def load(self):
        print("load called")
        self.driver.get("https://www.phptravels.net/admin")
        
    def is_loaded(self):
        assert self.loginBtn.is_displayed(), "Not displayed" 