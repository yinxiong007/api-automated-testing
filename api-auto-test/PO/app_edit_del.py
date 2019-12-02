from selenium.webdriver.common.by import By
from PO import base_page
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

#继承base后既可以调用base的方法也可自己添加新的方法
class app_edit_Page(base_page.Action):

    #通过xpath进行定位元素

    #调用api
    diaoyong_api_loc = (By.CSS_SELECTOR,'#app > div > div.el-scrollbar.hideSidebar.sidebar-container-fixed > div.scrollbar-wrapper.el-scrollbar__wrap > div > ul > div:nth-child(4) > li > div')
    #应用管理
    app_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[4]/li/ul/div/span/li/span')
    #鼠标悬停
    shubiao_loc = (By.XPATH,'//tr//th[3]//div[@class="cell"]')
    #编辑按钮
    app_edit_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/main/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[4]/div/button[1]/span')
    #应用名称
    name_loc = (By.CSS_SELECTOR,'body > div.el-dialog__wrapper.ps-dialog > div > div.el-dialog__body > div > div.scrollbar-wrapper.el-scrollbar__wrap > div > div > form > div:nth-child(1) > div > div > input')
    #描述
    miaoshu_loc = (By.CSS_SELECTOR,'body > div.el-dialog__wrapper.ps-dialog > div > div.el-dialog__body > div > div.scrollbar-wrapper.el-scrollbar__wrap > div > div > form > div:nth-child(2) > div > div > textarea')
    #确定
    queding_loc = (By.CSS_SELECTOR,'body > div.el-dialog__wrapper.ps-dialog > div > div.el-dialog__footer > div > div > button.el-button.el-button--primary')


    #操作元素
    def click_diaoyong_api_loc(self):
        self.find_element(*self.diaoyong_api_loc).click()
    def click_app_loc(self):
        self.find_element(*self.app_loc).click()
    def mouse_loc(self):
        mouse = self.find_element(*self.shubiao_loc)
        ActionChains(self.driver).move_to_element(mouse).perform()

    def click_app_edit_loc(self):
        #点击编辑应用按钮
        self.find_element(*self.app_edit_loc).click()
        time.sleep(2)

        #清空输入框
    def clear_content_loc(self):
        self.find_element(*self.name_loc).clear()
        self.find_element(*self.miaoshu_loc).clear()

    def input_content_loc(self,value1,value2):
        self.find_element(*self.name_loc).send_keys(value1)
        self.find_element(*self.miaoshu_loc).send_keys(value2)
        time.sleep(2)

    def click_queding_loc(self):
        self.find_element(*self.queding_loc).click()

class app_del_Page(base_page.Action):

    #通过xpath进行定位元素

    #调用api
    diaoyong_api_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[4]/li/div')
    #应用管理
    app_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[4]/li/ul/div/span/li/span')
    #鼠标悬停
    shubiao_loc = (By.XPATH,'//tr//th[3]//div[@class="cell"]')
    #删除按钮
    app_del_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/main/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[4]/div/button[2]')
    #确定
    queding_loc = (By.CSS_SELECTOR,'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary')
    #取消
    quxiao_loc = (By.CSS_SELECTOR,'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button:nth-child(1)')

    #进入应用详情元素
    name_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/main/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/button')
    #显示密钥
    xianshi_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/div[1]/div[2]/div[2]/div[2]/div/button[1]')
    #隐藏密钥
    yincang_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/div[1]/div[2]/div[2]/div[2]/div/button[1]')

    #操作元素
    def click_diaoyong_api_loc(self):
        self.find_element(*self.diaoyong_api_loc).click()
    def click_app_loc(self):
        self.find_element(*self.app_loc).click()
    def mouse_loc(self):
        mouse = self.find_element(*self.shubiao_loc)
        ActionChains(self.driver).move_to_element(mouse).perform()

    def click_app_del_loc(self):
        #点击删除应用
        self.find_element(*self.app_del_loc).click()
        time.sleep(2)

    def click_queding_loc(self):
        self.find_element(*self.queding_loc).click()

    def click_quxiao_loc(self):
        self.find_element(*self.quxiao_loc).click()

    def click_name_loc(self):
        self.find_element(*self.name_loc).click()

    def click_xianshi_loc(self):
        self.find_element(*self.xianshi_loc).click()

    def click_yincang_loc(self):
        self.find_element(*self.yincang_loc).click()