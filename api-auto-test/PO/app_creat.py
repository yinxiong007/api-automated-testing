from selenium.webdriver.common.by import By
from PO import base_page
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

#继承base后既可以调用base的方法也可自己添加新的方法
class app_creat_Page(base_page.Action):

    #通过xpath进行定位元素

    #调用api
    diaoyong_api_loc = (By.CSS_SELECTOR,'#app > div > div.el-scrollbar.hideSidebar.sidebar-container-fixed > div.scrollbar-wrapper.el-scrollbar__wrap > div > ul > div:nth-child(4) > li > div')
    #应用管理
    app_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[4]/li/ul/div/span/li/span')
    #鼠标悬停
    shubiao_loc = (By.XPATH,'//tr//th[3]//div[@class="cell"]')
    #创建应用
    app_creat_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/main/button/span')
    #应用名称
    name_loc = (By.CSS_SELECTOR,'body > div.el-dialog__wrapper.ps-dialog > div > div.el-dialog__body > div > div.scrollbar-wrapper.el-scrollbar__wrap > div > div > form > div:nth-child(1) > div > div.el-input > input')
    #描述
    miaoshu_loc = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.ps-dialog > div > div.el-dialog__body > div > div.scrollbar-wrapper.el-scrollbar__wrap > div > div > form > div:nth-child(2) > div > div.el-textarea > textarea')
    #应用名称为空的提示信息
    name_null_loc = (By.CSS_SELECTOR,'body > div.el-dialog__wrapper.ps-dialog > div > div.el-dialog__body > div > div.scrollbar-wrapper.el-scrollbar__wrap > div > div > form > div.el-form-item.is-error.is-required > div > div.el-form-item__error')
    #应用名称重复提示信息
    name_repeat_loc = (By.CSS_SELECTOR,'body > div.el-message.el-message--warning')
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

    def click_app_creat_loc(self):
        #点击创建应用按钮
        self.find_element(*self.app_creat_loc).click()
        time.sleep(2)
    def input_content_loc(self,value1,value2):
        self.find_element(*self.name_loc).send_keys(value1)
        self.find_element(*self.miaoshu_loc).send_keys(value2)
        time.sleep(2)
        #应用名称为空的提示信息
    def get_name_null(self):
        return self.find_element(*self.name_null_loc).text
       #应用名称重复提示信息
    def get_name_repeat(self):
        #toast_element = WebDriverWait(self.driver, 4).until(lambda x: x.find_element(*self.name_repeat_loc))
        return self.find_element(*self.name_repeat_loc).text

    def click_queding_loc(self):
        self.find_element(*self.queding_loc).click()
