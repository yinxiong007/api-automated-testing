'''import unittest,time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.implicitly_wait(20)
        self.verificationErrors = []

    def test_search(self):
        self.driver.find_element(By.ID, "kw").send_keys("hanxiaobei")
        time.sleep(2)
        self.driver.find_element(By.ID, "su").click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors, msg="验证失败")



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Baidu("test_search"))
    runner = unittest.TextTestRunner()
    runner.run(suite)'''''

from selenium import webdriver
import time,os
import unittest
import HTMLTestRunner

class Test_case(unittest.TestCase):
    """测试类"""
    def setUp(self):
        self.url = "http://www.baidu.com"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.verificationErrors = []

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

    def test_sou1(self):
        """测试搜索演示1"""
        self.driver.get(self.url)
        self.driver.find_element_by_id("kw").send_keys("测试")
        self.driver.find_element_by_id("su").click()
        self.driver.close()
        time.sleep(5)
    def test_sou2(self):
        """测试搜索演示2"""
        self.driver.get(self.url)
        self.driver.find_element_by_id("kw").send_keys("自动化测试")
        self.driver.find_element_by_id("su").click()
        self.driver.close()
        time.sleep(5)


#生成一个运行测试用例集合
suite = unittest.TestSuite()
suite.addTest(Test_case('test_sou1'))
suite.addTest(Test_case('test_sou2'))

report_file = ".\\result\\20170423_report.html"
fp = open(report_file,"wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="搜索",description="测试搜索结果")
runner.run(suite)
fp.close()