from selenium import webdriver
from enum import Enum


class BrowserType(Enum):

    CHROME = "chrome"
    FIREFOX = "firefox"
    PHANTOMJS = "phantomjs"
    EXPLORER = "iexplorer"


class BrowserSupport():

    def __init__(self, url):
        self.url = url
        self.driver = None

    def launch_browser(self, browser_type: BrowserType):

        if browser_type == BrowserType.CHROME:
            self.driver = webdriver.Chrome(executable_path="./resources/chrome_driver/chromedriver.exe")
        elif browser_type == BrowserType.FIREFOX:
            self.driver = webdriver.Firefox(executable_path="./resources/firefox_driver/geckodriver.exe")
        else:
            print("Error, browser ", browser_type, " not implemented yet.")

        if self.driver is not None:
            self.driver.get(self.url)
            self.driver.set_page_load_timeout(15)

    def close_browser(self):
        self.driver.close()


