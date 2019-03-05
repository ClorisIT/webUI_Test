from pageobject.base import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage(BasePage):
    home_page_input_username=(By.ID,'ls_username')
    home_page_button_password=(By.ID,'ls_password')
    home_page_button_denglu=(By.CSS_SELECTOR,'.fastlg_l button')
    home_page_button_moren=(By.CSS_SELECTOR,'td h2 a')
    home_page_input_title=(By.ID,'subject')
    home_page_input_zhengwen=(By.ID, 'fastpostmessage')
    home_page_button_submit=(By.ID,"fastpostsubmit")
    home_page_button_replay=(By.ID,"post_reply")
    home_page_input_replay_text=(By.NAME,"message")
    home_page_button_replay_submit=(By.NAME,"replysubmit")
    home_page_button_quit=(By.LINK_TEXT,"退出")

    def denglu(self,content1,content2):
        self.sendkeys(content1,*self.home_page_input_username)
        self.sendkeys(content2,*self.home_page_button_password)
        self.click(*self.home_page_button_denglu)
    def FaTie(self,content1,content2):
        time.sleep(5)
        self.click(*self.home_page_button_moren)
        time.sleep(3)
        self.sendkeys(content1,*self.home_page_input_title)
        time.sleep(3)
        self.sendkeys(content2,*self.home_page_input_zhengwen)
        time.sleep(3)
        self.click(*self.home_page_button_submit)
    def HuiTie(self,content):
        time.sleep(3)
        self.click(*self.home_page_button_replay)
        time.sleep(3)
        self.sendkeys(content,*self.home_page_input_replay_text)
        time.sleep(3)
        self.click(*self.home_page_button_replay_submit)
        time.sleep(5)
    def quit(self):
        self.home_page_button_quit


