from selenium.webdriver.common.by import By
from 自动化测试.PO import base_page
from selenium.webdriver import ActionChains
import time

#继承base后既可以调用base的方法也可自己添加新的方法
class app_search_Page(base_page.Action):

    #通过xpath进行定位元素

    #调用api
    diaoyong_api_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[4]/li/div')
    #应用管理
    app_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[4]/li/ul/div/span/li/span')
    #鼠标悬停
    shubiao_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/div[1]/div[2]/table/thead/tr/th[2]/div')
    #应用名称输入框
    name_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/form/div[1]/div/div/input')
    #查询按钮
    search_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/form/div[2]/div/button')
    # 搜索成功后的内容
    content_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/section/section/main/div[1]/div[3]/table/tbody/tr/td[1]/div/button/span')
    #没有搜到对应的内容
    null_content_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/div[1]/div[3]/div/span')


    #操作元素
    def click_diaoyong_api_loc(self):
        self.find_element(*self.diaoyong_api_loc).click()
    def click_app_loc(self):
        self.find_element(*self.app_loc).click()
    def mouse_loc(self):
        mouse = self.find_element(*self.shubiao_loc)
        ActionChains(self.driver).move_to_element(mouse).perform()

    def input_name_loc(self,value):
        #x先清空输入框
        self.find_element(*self.name_loc).clear()
        #输入应用名称
        self.find_element(*self.name_loc).send_keys(value)
        time.sleep(2)

    def click_search_loc(self):
        self.find_element(*self.search_loc).click()

    def get_content_loc(self):
        return self.find_element(*self.content_loc).text

    def get_null_content_loc(self):
        return self.find_element(*self.null_content_loc).text

