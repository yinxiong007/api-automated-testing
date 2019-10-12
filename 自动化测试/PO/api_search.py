from selenium.webdriver.common.by import By
from 自动化测试.PO import base_page
from selenium.webdriver import ActionChains
import time

#继承base后既可以调用base的方法也可自己添加新的方法
class SearchPage(base_page.Action):

    #通过xpath进行定位元素

    #开放api
    kaifang_api_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[3]/li/div')
    #api管理
    api_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[3]/li/ul/div[2]/span/li/span')
    #api名称输入框
    api_name_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/form/div[1]/div/div/input')
    #查询按钮
    search_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/form/div[4]/div/button')
    #搜索成功后的内容
    content_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/div[1]/div[3]/table/tbody/tr/td[1]/div/button/span')

    #操作元素
    def click_kaifang_api_loc(self):
        self.find_element(*self.kaifang_api_loc).click()
    def click_api_loc(self):
        self.find_element(*self.api_loc).click()
    def mouse_loc(self):
        mouse = self.find_element(*self.api_name_loc)
        ActionChains(self.driver).move_to_element(mouse).perform()
    def input_api_name_loc(self,value):
        #第一种利用原生的send_keys方法
        self.find_element(*self.api_name_loc).send_keys(value)
        #第二种利用二次封装的send_keys方法
        #self.send_keys(self.search_loc,value)
        time.sleep(2)
    def click_search_loc(self):
        self.find_element(*self.search_loc).click()



