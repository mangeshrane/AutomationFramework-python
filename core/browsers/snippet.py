""" This module contains the singleton driver instance implementation"""

import logging
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as ffOptions
from selenium.webdriver.edge.options import Options as edgeOptions
from FrameworkUtilities.config_utility import ConfigUtility
from FrameworkUtilities.logger_utility import custom_logger


class DriverFactory:
    """
    This class contains the reusable methods for getting the driver instances
    """
    log = custom_logger(logging.INFO)
    config = ConfigUtility()

    def __init__(self, browser, platform, environment, url=""):
        self.platform = platform
        self.browser = browser
        self.environment = environment
        self.url = url
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.prop = self.config.load_properties_file()

    def get_driver_instance(self):

        if self.browser == "chrome":

            chrome_capabilities = webdriver.DesiredCapabilities.CHROME
            chrome_capabilities['platform'] = self.platform
            chrome_capabilities['browserName'] = 'chrome'
            chrome_capabilities['javascriptEnabled'] = True

            options = chromeOptions()
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-notifications")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-web-security")
            options.add_argument("--no-proxy-server")
            options.add_argument("--enable-automation")
            options.add_argument("--disable-save-password-bubble")
            options.add_experimental_option('prefs', {'credentials_enable_service': False,
                                                      'profile': {'password_manager_enabled': False}})

            driver = webdriver.Remote(
                command_executor=self.prop.get('GRID', 'GRID_SERVER'),
                desired_capabilities=chrome_capabilities, options=options)

        elif self.browser == "firefox":

            firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
            firefox_capabilities['platform'] = self.platform
            firefox_capabilities['browserName'] = 'firefox'
            firefox_capabilities['javascriptEnabled'] = True
            firefox_capabilities['marionette'] = True

            options = ffOptions()
            options.log.level = 'trace'

            driver = webdriver.Remote(command_executor=self.prop.get('GRID', 'GRID_SERVER'),
                                      desired_capabilities=firefox_capabilities, options=options)

        elif self.browser == "safari":

            safari_capabilities = webdriver.DesiredCapabilities.SAFARI
            safari_capabilities['platform'] = self.platform
            safari_capabilities['browserName'] = 'safari'
            safari_capabilities['javascriptEnabled'] = True

            driver = webdriver.Remote(
                command_executor=self.prop.get('GRID', 'GRID_SERVER'),
                desired_capabilities=safari_capabilities)

        elif self.browser == "edge":

            edge_capabilities = webdriver.DesiredCapabilities.EDGE
            edge_capabilities['platform'] = self.platform
            edge_capabilities['browserName'] = 'MicrosoftEdge'
            edge_capabilities['javascriptEnabled'] = True

            driver = webdriver.Remote(
                command_executor=self.prop.get('GRID', 'GRID_SERVER'),
                desired_capabilities=edge_capabilities)

        elif self.browser == "sauce":
            username = self.prop.get('CLOUD', 'sl_username')
            automate_key = self.prop.get('CLOUD', 'sl_key')
            url = "https://" + username + ":" + automate_key + "@ondemand.saucelabs.com:443/wd/hub"

            caps = {}
            caps['browserName'] = "Safari"
            caps['appiumVersion'] = "1.8.1"
            caps['deviceName'] = "iPhone X Simulator"
            caps['deviceOrientation'] = "portrait"
            caps['platformVersion'] = "11.3"
            caps['platformName'] = "iOS"
            caps['name'] = "iPhone X Execution"

            driver = webdriver.Remote(
                command_executor=url,
                desired_capabilities=caps)

        elif self.browser == "browserstack_desktop":
            username = self.prop.get('CLOUD', 'bs_username')
            automate_key = self.prop.get('CLOUD', 'bs_key')
            url = "http://" + username + ":" + automate_key + "@hub.browserstack.com:80/wd/hub"

            caps = {}
            caps['browser'] = 'Firefox'
            caps['browser_version'] = '61.0'
            caps['os'] = 'OS X'
            caps['os_version'] = 'High Sierra'
            caps['resolution'] = '1024x768'
            caps['name'] = "Mac Safari Execution"
            caps['browserstack.debug'] = True
            caps['browserstack.networkLogs'] = True

            driver = webdriver.Remote(
                command_executor=url,
                desired_capabilities=caps)

        elif self.browser == "browserstack_mobile":
            username = self.prop.get('CLOUD', 'bs_username')
            automate_key = self.prop.get('CLOUD', 'bs_key')
            url = "http://" + username + ":" + automate_key + "@hub-cloud.browserstack.com/wd/hub"

            caps={}

            caps['device'] = 'Google Pixel'
            caps['os_version'] = '7.1'
            caps['name'] = "Google Pixcel Execution"

            driver = webdriver.Remote(
                command_executor=url,
                desired_capabilities=caps)

        elif self.browser == "local_edge":

            driver_location = os.path.join(self.cur_path, r"../ExternalDrivers/MicrosoftWebDriver.exe")
            os.environ["webdriver.edge.driver"] = driver_location

            edge_capabilities = webdriver.DesiredCapabilities.EDGE
            driver = webdriver.Edge(capabilities=edge_capabilities, executable_path=driver_location)

        elif self.browser == "local_firefox":
            driver_location = os.path.join(self.cur_path, r"../ExternalDrivers/geckodriver.exe")
            os.environ["webdriver.gecko.driver"] = driver_location

            browser_profile = webdriver.FirefoxProfile()
            browser_profile.set_preference("dom.webnotifications.enabled", False)

            options = ffOptions()
            options.log.level = 'trace'
            firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
            firefox_capabilities['marionette'] = True
            driver = webdriver.Firefox(capabilities=firefox_capabilities, executable_path=driver_location,
                                       options=options, log_path='/tmp/geckodriver.log',
                                       firefox_profile=browser_profile)

        elif self.browser == "local_chrome":
            driver_location = os.path.join(self.cur_path, r"../ExternalDrivers/chromedriver.exe")
            os.environ["webdriver.chrome.driver"] = driver_location

            options = chromeOptions()
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-notifications")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-web-security")
            options.add_argument("--no-proxy-server")
            options.add_argument("--enable-automation")
            options.add_argument("--disable-save-password-bubble")
            options.add_experimental_option('prefs', {'credentials_enable_service': False,
                                                      'profile': {'password_manager_enabled': False}})

            driver = webdriver.Chrome(driver_location, options=options)

        else:
            driver_location = os.path.join(self.cur_path, r"../ExternalDrivers/chromedriver.exe")
            os.environ["webdriver.chrome.driver"] = driver_location

            options = chromeOptions()
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-notifications")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-web-security")
            options.add_argument("--no-proxy-server")
            options.add_argument("--enable-automation")
            options.add_argument("--disable-save-password-bubble")
            options.add_experimental_option('prefs', {'credentials_enable_service': False,
                                                      'profile': {'password_manager_enabled': False}})

            driver = webdriver.Chrome(driver_location, options=options)

        if "chrome" in self.browser:
            driver.fullscreen_window()

        if self.environment == "staging":
            test_data = self.prop.get('RAFT', 'staging_test_data')
            self.config.change_properties_file('RAFT', 'base_test_data', test_data)
            self.url = self.prop.get('RAFT', 'staging_url')
            self.config.change_properties_file('RAFT', 'base_url', self.url)

        elif self.environment == "prod":
            test_data = self.prop.get('RAFT', 'prod_test_data')
            self.config.change_properties_file('RAFT', 'base_test_data', test_data)
            self.url = self.prop.get('RAFT', 'prod_url')
            self.config.change_properties_file('RAFT', 'base_url', self.url)

        else:
            test_data = self.prop.get('RAFT', 'staging_test_data')
            self.config.change_properties_file('RAFT', 'base_test_data', test_data)
            self.url = self.prop.get('RAFT', 'staging_url')
            self.config.change_properties_file('RAFT', 'base_url', self.url)

        driver.get(self.url)

        return driver
