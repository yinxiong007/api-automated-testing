from selenium.webdriver.common.by import By
from PO import base_page
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#继承base后既可以调用base的方法也可自己添加新的方法
class group_editPage(base_page.Action):

    #通过xpath进行定位元素

    #开放api
    kaifang_api_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[3]/li/div')
    #api分组
    group_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[3]/li/ul/div[1]/span/li/span')
    #鼠标悬停
    shubiao_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/div[1]/div[2]/table/thead/tr/th[2]/div')
    #编辑分组
    group_edit_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[4]/div/button[1]')
    #分组名称
    name_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[1]/div/div/form/div[1]/div/div/input')
    #描述
    miaoshu_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[1]/div/div/form/div[2]/div/div/textarea')
    #确定
    queding_loc = (By.XPATH,'/html/body/div[3]/div/div[3]/div/div/button[2]/span')

    #操作元素
    def click_kaifang_api_loc(self):
        self.find_element(*self.kaifang_api_loc).click()
    def click_group_loc(self):
        self.find_element(*self.group_loc).click()
    def mouse_loc(self):
        mouse = self.find_element(*self.shubiao_loc)
        ActionChains(self.driver).move_to_element(mouse).perform()
    def click_api_edit_loc(self):
        #点击分组编辑按钮
        self.find_element(*self.group_edit_loc).click()
        time.sleep(2)
    def clear_content_loc(self):
        # #显示等待应用名称出现，每0.5秒扫描一次，直到20秒超时后，停止
        # WebDriverWait(self.driver, 20, 0.5).until(
        #     EC.presence_of_element_located(*self.name_loc))
        self.find_element(*self.name_loc).clear()
        self.find_element(*self.miaoshu_loc).clear()
    def input_content_loc(self,value1,value2):
        self.find_element(*self.name_loc).send_keys(value1)
        self.find_element(*self.miaoshu_loc).send_keys(value2)
        time.sleep(2)
    def click_queding_loc(self):
        self.find_element(*self.queding_loc).click()