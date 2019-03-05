from pageobject.base import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage(BasePage):
    home_page_input_username=(By.ID,'ls_username')
    home_page_button_password=(By.ID,'ls_password')
    home_page_button_denglu=(By.CSS_SELECTOR,'.fastlg_l button')
    home_page_button_moren = (By.XPATH, '//*[@id="category_1"]/table/tbody/tr[1]/td[2]/h2/a')
    home_page_button_fatie=(By.XPATH,'//*[@id="newspecial"]/img')
    home_page_button_vote=(By.XPATH,'//*[@id="editorbox"]/ul/li[2]/a')
    home_page_input_vote_title=(By.XPATH,'//*[@id="subject"]')
    home_page_input_vote_text1=(By.XPATH,'//*[@id="pollm_c_1"]/p[1]/input')
    home_page_input_vote_text2 =(By.XPATH, '//*[@id="pollm_c_1"]/p[2]/input')
    home_page_input_vote_text3 =(By.XPATH, '//*[@id="pollm_c_1"]/p[3]/input')
    home_page_button_vote_submit=(By.XPATH,'//*[@id="postsubmit"]/span')
    home_page_input_vote_choose1=(By.XPATH,'//*[@id="option_1"]')
    # home_page_input_vote_choose2 = (By.XPATH, '//*[@id="option_2"]')
    # home_page_input_vote_choose3 = (By.XPATH, '//*[@id="option_3"]')
    home_page_button_choose1_text=(By.CSS_SELECTOR,'.pcht  tr:nth-child(1) td.pvt')
    home_page_button_choose2_text=(By.CSS_SELECTOR,'.pcht  tr:nth-child(3) td.pvt')
    home_page_button_choose3_text=(By.CSS_SELECTOR,'.pcht  tr:nth-child(5) td.pvt')
    home_page_button_proportion1_text=(By.CSS_SELECTOR,'.pcht tr:nth-child(2) td:nth-child(2)')
    home_page_button_proportion2_text=(By.CSS_SELECTOR,'.pcht tr:nth-child(4) td:nth-child(2)')
    home_page_button_proportion3_text=(By.CSS_SELECTOR,'.pcht tr:nth-child(6) td:nth-child(2)')
    home_page_button_vote_title_text=(By.CSS_SELECTOR,"#thread_subject")

    def denglu(self, content1, content2):
        self.sendkeys(content1, *self.home_page_input_username)
        self.sendkeys(content2, *self.home_page_button_password)
        self.click(*self.home_page_button_denglu)
    def fatie(self,content1,content2,content3,content4):
        time.sleep(3)
        self.click(*self.home_page_button_moren)
        time.sleep(3)
        self.click(*self.home_page_button_fatie)
        time.sleep(3)
        self.click(*self.home_page_button_vote)
        time.sleep(3)
        self.sendkeys(content1,*self.home_page_input_vote_title)
        time.sleep(3)
        self.sendkeys(content2,*self.home_page_input_vote_text1)
        time.sleep(3)
        self.sendkeys(content3,*self.home_page_input_vote_text2)
        time.sleep(3)
        self.sendkeys(content4,*self.home_page_input_vote_text3)
        time.sleep(3)
        self.click(*self.home_page_button_vote_submit)
        time.sleep(3)
    def vote(self):
        time.sleep(3)
        self.click(*self.home_page_input_vote_choose1)
        time.sleep(3)
        # self.click(*self.home_page_input_vote_choose2)
        # time.sleep(3)
        # self.click(*self.home_page_input_vote_choose3)
    def take_out(self):
        a=self.text(*self.home_page_button_choose1_text)
        b=self.text(*self.home_page_button_choose2_text)
        c=self.text(*self.home_page_button_choose3_text)
        d=self.text(*self.home_page_button_proportion1_text)
        e=self.text(*self.home_page_button_proportion2_text)
        f=self.text(*self.home_page_button_proportion3_text)
        g=self.text(*self.home_page_button_vote_title_text)
        print("投票名称:",a,"投票比例:",d)
        print("投票名称:",b,"投票比例:",e)
        print("投票名称:",c,"投票比例:",f)
        print("投票主题:",g)




