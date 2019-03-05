import  unittest
from selenium import webdriver
from testsuites.base_testcase import BaseTestCase
from pageobject.homepage03 import   HomePage
from framework.logger import Logger
import time

logger=Logger(logger="Search03").getlog()


class Search03(BaseTestCase):
    def test_homepage02(self):
        home_page=HomePage(self.driver)
        # home_page.get_url("http://127.0.0.1/forum.php")
        logger.info("获取网页。。。")
        home_page.denglu("admin", "root")
        logger.info("管理员登陆成功")
        home_page.FaTie("haotest","123")
        logger.info("发帖成功")
        title=home_page.find("haotest")
        try:
            self.assertEqual(title,"haotest",msg=title)
            logger.info("验证成功")
            print(title)
        except:
            logger.error("验证错误")
            print("错误")
        home_page.quit()
        logger.info("退出成功")

if __name__=='__main__':
    unittest.main()