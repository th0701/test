import unittest
import HTMLTestRunner
from common import getpath
import time
import os

def runCase():
    suite = unittest.TestSuite()
    tests = unittest.defaultTestLoader.discover(
        start_dir="apiTestCase",
        pattern="api_test*"
    )

    for x in tests:
        for i in x:
            suite.addTest(i)



    time_name = time.strftime("%Y-%m-%d")
    html_time_name = getpath.getpath("report", time_name)
    if not os.path.isdir(html_time_name):
        os.mkdir(html_time_name)
    # 时分秒
    report_html = "report_" + time.strftime("%H-%M-%S") + "_.html"
    with open(os.path.join(html_time_name, report_html) ,"wb") as f:
        ht = HTMLTestRunner.HTMLTestRunner(f, title="谈欢的自动化测试报告")
        ht.run(suite)


