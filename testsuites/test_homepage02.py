import  unittest
from selenium import webdriver
from testsuites.base_testcase import BaseTestCase
from pageobject.homepage02 import   HomePage
from framework.logger import Logger

logger=Logger(logger="Search02").getlog()


class Search02(BaseTestCase):
    def test_homepage02(self):
        home_page=HomePage(self.driver)
        home_page.get_url("http://127.0.0.1/forum.php")
        logger.info("获取网页。。。")
        home_page.denglu("admin", "root")
        logger.info("管理员登陆成功")
        home_page.Delete()
        logger.info("删除成功")
        home_page.SectorManagement("root")
        logger.info("新板块添加成功")
        home_page.quit()
        logger.info("管理员退出成功")
        home_page.AverageUser("admin01","123456")
        logger.info("普通用户登陆成功")
        home_page.FaTie("haotest", "12345678910")
        logger.info("普通用户发帖成功")
        home_page.HuiTie("lihaojie")
        logger.info("普通用户回帖成功")

if __name__=='__main__':
    unittest.main()