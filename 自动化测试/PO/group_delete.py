from selenium.webdriver.common.by import By
from 自动化测试.PO import base_page
from selenium.webdriver import ActionChains
import time

#继承base后既可以调用base的方法也可自己添加新的方法
class group_delPage(base_page.Action):

    #通过xpath进行定位元素

    #开放api
    kaifang_api_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[3]/li/div')
    #api分组
    group_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[3]/li/ul/div[1]/span/li/span')
    #鼠标悬停
    shubiao_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/div[1]/div[2]/table/thead/tr/th[2]/div')
    #删除分组
    group_del_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[4]/div/button[2]')
    #确定
    queding_loc = (By.CSS_SELECTOR,'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary')
    #取消
    quxiao_loc = (By.CSS_SELECTOR,'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button:nth-child(1)')

    #操作元素
    def click_kaifang_api_loc(self):
        self.find_element(*self.kaifang_api_loc).click()
    def click_group_loc(self):
        self.find_element(*self.group_loc).click()
    def mouse_loc(self):
        mouse = self.find_element(*self.shubiao_loc)
        ActionChains(self.driver).move_to_element(mouse).perform()
    def click_api_del_loc(self):
        #点击分组删除按钮
        self.find_element(*self.group_del_loc).click()
        time.sleep(2)

    def click_queding_loc(self):
        self.find_element(*self.queding_loc).click()

    def click_quxiao_loc(self):
        self.find_element(*self.quxiao_loc).click()