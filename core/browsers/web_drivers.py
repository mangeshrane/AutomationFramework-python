'''
Created on Feb 18, 2019

@author: mrane
'''
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from core.configuration import CONFIG
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os

class WebDrivers(object):
	
	@property
	def chrome(self, extension=None, headless=False):
		option = Options()
		option.set_headless(headless)
		for arg in CONFIG.get("webdriver.chrome.arguments", []):
			option.add_argument(arg)
		if extension:
			option.add_extension(extension)
		driver = webdriver.Chrome(executable_path=CONFIG.get("webdriver.chrome.driver"), options=option)
		return driver
	
	@property
	def firefox(self, args=[], extension=None):
		profile = FirefoxProfile()
		pref =  CONFIG.get("webdriver.firefox.preferences", None)
		if pref:
			for key, value in pref.items():
				profile.set_preference(key, value)
		if extension:
			profile.add_extension(extension)
		driver = webdriver.Firefox(profile, executable_path=CONFIG.get("webdriver.firefox.driver"))
		return driver
	
	@staticmethod
	def get():
		if os.environ.get("CORE.DRIVER", None):
			try:
				browser = os.environ["CORE.DRIVER"]
			except Exception:
				browser = "chrome"
		else:
			browser = CONFIG.get("tests.browser", "chrome")
		return WebDrivers.__getattribute__(WebDrivers(), browser)

