from  selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import  expected_conditions as EC
from selenium import  webdriver
import time
import os.path

class BasePage(object):
    def  __init__(self,driver):
        self.driver=driver

    def find_element(self,*loc):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
    def  click(self,*loc):
        el=self.driver.find_element(*loc)
        el.click()
    def sendkeys(self,text,*loc):
        el=self.driver.find_element(*loc)
        el.clear()
        el.send_keys(text)
    def get_url(self,url):
        self.driver.get(url)
    def text(self,*loc):
        el=self.driver.find_element(*loc)
        return el.text
    def frame(self,*loc):
        e1=self.driver.find_element(*loc)
        self.driver.switch_to.frame(e1)







