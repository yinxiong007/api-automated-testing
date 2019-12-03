#coding = utf-8
import unittest
from selenium import webdriver
from PO.api_search import SearchPage
from PO.api_edit import api_editPage
import time

class Test_Api(unittest.TestCase):
    """UI自动化"""
    #driver = webdriver.Chrome()
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.url = "http://10.0.95.8:8091/apigw"

        sp = SearchPage(self.driver)
        sp.open(self.url)

        # 将用户名密码写入浏览器cookie
        self.driver.add_cookie({'name':'token','value':'BearereyJhbGciOiJIUzUxMiJ9.eyJ1c2VySWRzIjoiMTgwZGZlMWM1OTNiNGU5ODk4YzVhNmZkZjIyNTVmNTIiLCJ0ZW5hbnRJZCI6IjMwNjYwMzYwMDI5NTI4NDczNiIsInVzZXJOYW1lIjoieWlueGlvbmciLCJleHAiOjE1Nzg5NDA4MTksInVzZXJJZCI6IjE4MGRmZTFjNTkzYjRlOTg5OGM1YTZmZGYyMjU1ZjUyIn0.Dq5U_Qb-gpoAzDqsNW2v37kkAcomxDM8xIxWM5qImrzYJ9p3ErCtW_uMgYBiK4HbBsJoTgeAHu8wucIMiUkzFg'})
        sp.open(self.url)
        time.sleep(3)
        self.driver.implicitly_wait(20)
        self.verificationErrors = []
    @classmethod
    def tearDownClass(self):
        try:
            self.driver.quit()
        except Exception as e:
            print(e)


    def test1_search(self):
        """搜索api关键字"""
        # 实例化搜索页面
        sp = SearchPage(self.driver)
        sp.click_kaifang_api_loc()
        sp.click_api_loc()
        sp.mouse_loc()
        sp.input_api_name_loc('dididi')
        time.sleep(2)
        sp.click_search_loc()
        time.sleep(2)
        self.driver.refresh()

    def test2_authorize(self):
        """api授权"""
        sp = api_editPage(self.driver)
        sp.click_kaifang_api_loc()
        sp.click_api_loc()
        sp.mouse_loc()
        time.sleep(3)
        sp.click_api_authorize_loc()
        sp.input_appid_loc('273')
        sp.click_appid_search_loc()
        time.sleep(5)
        sp.click_app_add_loc()
        time.sleep(5)
        sp.click_queding_loc()
        self.assertEqual('授权成功',sp.get_bangding_tips_loc())

    def test3_xiangqing_search(self):
        """api详情界面搜索"""
        sp = api_editPage(self.driver)
        self.driver.refresh()
        sp.click_kaifang_api_loc()
        sp.click_api_loc()
        sp.mouse_loc()
        time.sleep(3)
        sp.click_api_name_loc()
        sp.click_api_shouquan_loc()
        sp.input_name_loc('dada')
        sp.click_search_loc()

    def test4_jiebang(self):
        """api解绑"""
        sp = api_editPage(self.driver)
        sp.click_kaifang_api_loc()
        sp.click_api_loc()
        sp.mouse_loc()
        time.sleep(3)
        sp.click_api_name_loc()
        sp.click_api_shouquan_loc()
        sp.click_jiebang_loc()
        sp.click_jiebang_queding_loc()
        #断言
        self.assertEqual(sp.get_jiebang_tips_loc(),'解绑成功')


