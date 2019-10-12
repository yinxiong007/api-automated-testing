from selenium.webdriver.common.by import By
from 自动化测试.PO import base_page
from selenium.webdriver import ActionChains
import time

#继承base后既可以调用base的方法也可自己添加新的方法
class groupPage(base_page.Action):

    #通过xpath进行定位元素

    #开放api
    kaifang_api_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[3]/li/div')
    #api分组
    group_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[3]/li/ul/div[1]/span/li/span')
    #鼠标悬停
    shubiao_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/div[1]/div[2]/table/thead/tr/th[2]/div')
    #创建分组
    api_creat_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/form/div/div/button')
    #分组名称
    name_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div[1]/div/div/form/div[1]/div/div[1]/input')
    #描述
    miaoshu_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div[1]/div/div/form/div[2]/div/div[1]/textarea')
    #确定
    queding_loc = (By.XPATH,'/html/body/div[2]/div/div[3]/div/div/button[2]')

    #操作元素
    def click_kaifang_api_loc(self):
        self.find_element(*self.kaifang_api_loc).click()
    def click_group_loc(self):
        self.find_element(*self.group_loc).click()
    def mouse_loc(self):
        mouse = self.find_element(*self.shubiao_loc)
        ActionChains(self.driver).move_to_element(mouse).perform()
    def click_api_creat_loc(self):
        #第一种利用原生的send_keys方法
        self.find_element(*self.api_creat_loc).click()
        #第二种利用二次封装的send_keys方法
        #self.send_keys(self.search_loc,value)
        time.sleep(2)
    def input_content_loc(self,value1,value2):
        self.find_element(*self.name_loc).send_keys(value1)
        self.find_element(*self.miaoshu_loc).send_keys(value2)
        time.sleep(2)
    def click_queding_loc(self):
        self.find_element(*self.queding_loc).click()