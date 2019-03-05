import  unittest
from selenium import webdriver
from testsuites.base_testcase import BaseTestCase
from pageobject.homepage01 import  HomePage
from framework.logger import Logger

logger=Logger(logger="Search01").getlog()


class Search01(BaseTestCase):
    def test_homepage01(self):
        home_page=HomePage(self.driver)
        home_page.get_url("http://127.0.0.1/forum.php")
        logger.info("获取网页。。。")
        # 板块一
        home_page.denglu("admin","root")
        logger.info("登陆成功")
        home_page.FaTie("haotest","123")
        logger.info("帖子标题","帖子正文")
        logger.info("发表成功")
        home_page.HuiTie("lihaojie")
        logger.info("回复成功")
        #板块二
        # home_page.denglu("admin", "root")
        # # home_page.SectorManagement("root")
        # home_page.SectorManagement()
        # home_page.quit()
        # home_page.AverageUser("admin01","123456")
        # home_page.FaTie("haotest", "123")
        # home_page.HuiTie("lihaojie")
        # 板块三
        # home_page.denglu("admin", "root")
        # home_page.FaTie("haotest","123")
        # home_page.find("haotest")

        # 板块四
        # home_page.denglu("admin", "root")
        # home_page.fatie("董杰帅不帅","帅","帅","帅")
        # home_page.vote()
        # home_page.take_out()

if __name__=='__main__':
    unittest.main()

