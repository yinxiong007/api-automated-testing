import unittest
from selenium import webdriver
from PO.group_creat import groupPage
from PO.group_edit import group_editPage
from PO.group_delete import group_delPage
from PO.base_page import Screen


import time

class TestGroup(unittest.TestCase):
    """UI自动化"""
    #driver = webdriver.Chrome()
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.url = "http://10.0.95.8:8091/apigw"

        sp = groupPage(self.driver)
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

    def test1_group_creat(self):
        """创建分组"""
        # 实例化api分组页面
        sp = groupPage(self.driver)
        sp.click_kaifang_api_loc()
        sp.click_group_loc()
        sp.mouse_loc()
        sp.click_api_creat_loc()
        sp.input_content_loc('zidonghua','test')
        sp.click_queding_loc()
        time.sleep(5)


    def test2_group_edit(self):
        """编辑分组"""
        # 实例化api分组页面
        sp = group_editPage(self.driver)
        sp.click_kaifang_api_loc()
        sp.click_group_loc()
        sp.mouse_loc()
        sp.click_api_edit_loc()
        time.sleep(3)
        sp.clear_content_loc()
        time.sleep(3)
        sp.input_content_loc('zidonghua1','test1')
        sp.click_queding_loc()
        time.sleep(2)

    def test3_group_del1(self):
        """删除分组界面取消"""
        # 实例化api分组页面
        sp = group_delPage(self.driver)
        sp.click_kaifang_api_loc()
        sp.click_group_loc()
        sp.mouse_loc()
        sp.click_api_del_loc()
        sp.click_quxiao_loc()
        time.sleep(2)


    def test4_group_del2(self):
        """删除分组"""
        # 实例化api分组页面
        sp = group_delPage(self.driver)
        sp.click_kaifang_api_loc()
        sp.click_group_loc()
        sp.mouse_loc()
        sp.click_api_del_loc()
        sp.click_queding_loc()
        time.sleep(2)

    #@Screen(driver)
    def test5_group_del3(self):
        """删除分组--存在绑定关系"""
        sp = group_delPage(self.driver)
        sp.click_kaifang_api_loc()
        sp.click_group_loc()
        sp.mouse_loc()
        sp.click_api_del_loc()
        time.sleep(3)
        self.assertEqual(sp.get_group_del_api(),'API管理')
        sp.click_group_del_close()
