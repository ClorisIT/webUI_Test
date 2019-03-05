import unittest
from selenium import webdriver
from framework.browser import Browser

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.browser=Browser()
        self.driver=self.browser.open_browser()
        # self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
    def tearDown(self):
        self.driver=self.browser.quit_browser()