import unittest
import HTMLTestRunner
import time

#相对路径
testcase_path = ".\\testcase"
#存放文件的目录
report_dir = ".\\report"
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_path = report_dir + '\\'+now+'_report.html'

def creat_suite():
    uit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path,pattern="test_*.py")
    for test_suite in discover:
        # print(test_suite)
        for test_case in test_suite:
            uit.addTest(test_case)
    return uit

suite = creat_suite()
fp = open(report_path,"wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="测试结果",description="测试搜索结果")
runner.run(suite)
fp.close()