import unittest
from selenium import webdriver
from PO.app_creat import app_creat_Page
from PO.app_edit_del import app_edit_Page,app_del_Page
from PO.app_search import app_search_Page
import time


class TestApp(unittest.TestCase):
    #driver = webdriver.Chrome()
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url = "http://10.0.95.8:8091/apigw"

        sp = app_creat_Page(cls.driver)
        sp.open(cls.url)

        #把cookie加入浏览器
        sp.send_cookie()
        sp.open(cls.url)
        time.sleep(3)
        cls.driver.implicitly_wait(20)
         #脚本运行时，错误的信息将被打印到这个列表中
        cls.verificationErrors = []

    @classmethod
    def tearDownClass(cls):
        #cls.driver = webdriver.Chrome()
        try:
            cls.driver.quit()
        # 对前面verificationErrors方法获得的列表进行比较；如查verificationErrors的列表不为空，输出列表中的报错信息。
        except Exception as e:
            print(e)

    def test1_app_creat(self):
        """创建应用"""
        # 实例化app页面
        sp = app_creat_Page(self.driver)
        sp.click_diaoyong_api_loc()
        sp.click_app_loc()
        sp.mouse_loc()
        sp.click_app_creat_loc()
        sp.input_content_loc('app_test1','test')
        sp.click_queding_loc()
        time.sleep(2)

    def test2_app_creat(self):
        """创建应用--应用名称为空"""
        sp = app_creat_Page(self.driver)
        time.sleep(2)
        sp.click_app_creat_loc()
        sp.input_content_loc('','test')
        sp.click_queding_loc()
        #断言
        self.assertEqual(sp.get_name_null(),'不能为空')

    def test3_app_creat(self):
        """创建应用--应用名称重复"""
        sp = app_creat_Page(self.driver)
        sp.open(self.url)
        sp.click_diaoyong_api_loc()
        sp.click_app_loc()
        time.sleep(2)
        sp.mouse_loc()
        sp.click_app_creat_loc()
        sp.input_content_loc('app_test1','test')
        sp.click_queding_loc()
        time.sleep(2)
        # 断言
        self.assertEqual(sp.get_name_repeat(), '指定的应用名称已存在，请重新修改')

    def test4_app_edit(self):
        """编辑应用"""
        sp = app_edit_Page(self.driver)
        sp.open(self.url)
        sp.click_diaoyong_api_loc()
        sp.click_app_loc()
        sp.mouse_loc()
        time.sleep(2)
        sp.click_app_edit_loc()
        sp.clear_content_loc()
        sp.input_content_loc('xiugai1','test1')
        sp.click_queding_loc()
        time.sleep(2)

    def test5_app_xiangqing(self):
        """应用详情---密钥显示和隐藏"""
        xiangqing = app_del_Page(self.driver)
        xiangqing.click_diaoyong_api_loc()
        xiangqing.click_app_loc()
        xiangqing.mouse_loc()
        xiangqing.click_name_loc()
        xiangqing.click_xianshi_loc()
        time.sleep(2)
        xiangqing.click_yincang_loc()

    def test6_app_del(self):
        """删除应用界面取消"""
        delete = app_del_Page(self.driver)
        delete.click_diaoyong_api_loc()
        delete.click_app_loc()
        delete.mouse_loc()
        delete.click_app_del_loc()
        delete.click_quxiao_loc()
        time.sleep(2)

    def test7_app_del(self):
        """删除应用"""
        delete = app_del_Page(self.driver)
        delete.click_diaoyong_api_loc()
        delete.click_app_loc()
        delete.mouse_loc()
        delete.click_app_del_loc()
        delete.click_queding_loc()
        time.sleep(2)

    def test8_app_search(self):
        """搜索应用"""
        search = app_search_Page(self.driver)
        search.click_diaoyong_api_loc()
        search.click_app_loc()
        search.mouse_loc()
        search.input_name_loc('daxiong')
        search.click_search_loc()
        time.sleep(2)
        # 断言
        self.assertEqual(search.get_content_loc(), 'daxiong')

    def test9_app_search(self):
        """模糊搜索"""
        search = app_search_Page(self.driver)
        search.click_diaoyong_api_loc()
        search.click_app_loc()
        search.mouse_loc()
        search.input_name_loc('daxi')
        search.click_search_loc()
        time.sleep(2)
        # 断言
        self.assertEqual(search.get_null_content_loc(), '暂无数据')

