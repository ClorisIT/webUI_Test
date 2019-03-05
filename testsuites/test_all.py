import unittest
import HTMLTestRunner
import os
from testsuites.test_homepage01 import Search01
from testsuites.test_homepage02 import Search02
from testsuites.test_homepage03 import Search03
from testsuites.test_homepage04 import Search04


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Search01))
suite.addTest(unittest.makeSuite(Search02))
suite.addTest(unittest.makeSuite(Search03))
suite.addTest(unittest.makeSuite(Search04))

if __name__ == "__main__":
    html_report = r"D:\python\baidu\report\report.html"
    bg = open(html_report, "wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=bg, verbosity=2, title="单元测试报告", description="用例执行情况")
    runner.run(suite)