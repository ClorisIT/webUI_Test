import  unittest
from selenium import webdriver
from testsuites.base_testcase import BaseTestCase
from pageobject.homepage04 import   HomePage
from framework.logger import Logger

logger=Logger(logger="Search04").getlog()


class Search04(BaseTestCase):
    def test_homepage02(self):
        home_page=HomePage(self.driver)
        home_page.get_url("http://127.0.0.1/forum.php")
        logger.info("获取网页。。。")
        home_page.denglu("admin", "root")
        logger.info("登陆成功")
        home_page.fatie("组长帅不帅","帅","帅","帅")
        logger.info("发起投票成功")
        home_page.vote()
        logger.info("投票成功")
        home_page.take_out()
        logger.info("取值成功")

if __name__=='__main__':
    unittest.main()