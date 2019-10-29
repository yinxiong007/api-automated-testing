import unittest
from selenium import webdriver
from PO.ip_creat import ip_creat_Page
from PO.ip_edit_del import ip_del_Page


import time

class TestIp(unittest.TestCase):
    """UI自动化"""
    #driver = webdriver.Chrome()
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.url = "http://10.0.95.8:8091/apigw"

        sp = ip_creat_Page(self.driver)
        sp.open(self.url)

        # 将用户名密码写入浏览器cookie
        self.driver.add_cookie({'name':'token','value':'BearereyJhbGciOiJIUzUxMiJ9.eyJ1c2VySWRzIjoiMzA2NTg1ODE0NjgwNTIyNzUyLDE4MGRmZTFjNTkzYjRlOTg5OGM1YTZmZGYyMjU1ZjUyIiwidGVuYW50SWQiOiIzMDY2MDM2MDAyOTUyODQ3MzYiLCJ1c2VyTmFtZSI6Inlpbnhpb25nIiwiZXhwIjoxNTc1MzA4ODI1LCJ1c2VySWQiOiIxODBkZmUxYzU5M2I0ZTk4OThjNWE2ZmRmMjI1NWY1MiJ9.yKPNgFdFlh8tf205Llj3kBUk_uvsgDj5Jf676XbBfnMqnSWYz3rATfivztHzqpjvMsQU3mZD829aj92RZTe6Ng'})
        sp.open(self.url)
        time.sleep(3)
        self.driver.implicitly_wait(20)
        # 脚本运行时，错误的信息将被打印到这个列表中
        self.verificationErrors = []

    @classmethod
    def tearDownClass(self):
        #self.driver = webdriver.Chrome()
        try:
            self.driver.quit()
        except Exception as e:
            print(e)

    def test1_ip_creat(self):
        """创建ip访问控制"""
        # 实例化ip页面
        sp = ip_creat_Page(self.driver)
        sp.click_kaifang_api_loc()
        sp.click_ip_loc()
        sp.mouse_loc()
        sp.click_ip_creat_loc()
        sp.input_content_loc('iptest','test')
        sp.click_queding_loc()
        time.sleep(5)
        self.driver.refresh()

    def test2_ip_creat(self):
        """创建ip--名称为空"""
        sp = ip_creat_Page(self.driver)
        sp.click_kaifang_api_loc()
        sp.click_ip_loc()
        sp.mouse_loc()
        sp.click_ip_creat_loc()
        sp.input_content_loc('','test')
        sp.click_queding_loc()
        #断言
        self.assertEqual(sp.get_name_null(),'请输入策略名称')
        self.driver.refresh()

    def test3_ip_creat(self):
        """创建ip--名称重复"""
        sp = ip_creat_Page(self.driver)
        sp.click_kaifang_api_loc()
        sp.click_ip_loc()
        sp.mouse_loc()
        sp.click_ip_creat_loc()
        sp.input_content_loc('iptest','test')
        sp.click_queding_loc()
        time.sleep(2)
        #断言
        self.assertEqual(sp.get_name_repeat(),'标题已存在')
        self.driver.refresh()

    def test4_ip_creat(self):
        """创建ip--名称输入空格"""
        sp = ip_creat_Page(self.driver)
        sp.click_kaifang_api_loc()
        sp.click_ip_loc()
        sp.mouse_loc()
        sp.click_ip_creat_loc()
        sp.input_content_loc(' ','test')
        time.sleep(2)
        # 断言
        self.assertEqual(sp.get_name_error(),'只能以英文和汉字开头')

    def test5_ip_creat(self):
        """创建ip--类型筛选"""
        sp = ip_creat_Page(self.driver)
        self.driver.refresh()
        sp.click_kaifang_api_loc()
        sp.click_ip_loc()
        sp.mouse_loc()
        sp.click_ip_creat_loc()
        sp.input_content_loc('iptest1','test')
        sp.click_leixing_loc()
        time.sleep(2)
        sp.click_queding_loc()
        self.driver.refresh()


    def test6_ip_del(self):
        """删除ip"""
        sp = ip_del_Page(self.driver)
        sp.click_kaifang_api_loc()
        sp.click_ip_loc()
        sp.mouse_loc()
        sp.click_ip_del_loc()
        self.driver.refresh()
        time.sleep(2)
        sp.click_ip_del_loc()
        time.sleep(2)
