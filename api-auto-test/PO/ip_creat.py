from selenium.webdriver.common.by import By
from PO import base_page
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

#继承base后既可以调用base的方法也可自己添加新的方法
class ip_creat_Page(base_page.Action):

    #通过xpath进行定位元素

    #开放api
    kaifang_api_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/ul/div[3]/li/div')
    #ip访问控制
    ip_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[3]/li/ul/div[3]/span/li/span')
    #鼠标悬停
    shubiao_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/div[1]/div[2]/table/thead/tr/th[4]/div')
    #创建ip
    ip_creat_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/form/div/div/button')
    #ip名称
    name_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div[1]/div/div/div/form/div[1]/div/div[1]/input')
    #类型筛选
    leixing_loc = (By.CSS_SELECTOR,'body > div.el-dialog__wrapper.ps-dialog > div > div.el-dialog__body > div > div.scrollbar-wrapper.el-scrollbar__wrap > div > div > div > form > div:nth-child(2) > div > div > div.el-input.el-input--suffix > span > span > i')
    reject_loc = (By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li[2]/span')
    #描述
    miaoshu_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div[1]/div/div/div/form/div[3]/div/div/textarea')
    #ip策略名称为空提示信息
    name_null_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div[1]/div/div/div/form/div[1]/div/div[2]')
    #ip策略名称重复提示信息
    name_repeat_loc = (By.CSS_SELECTOR,'body > div.el-message.el-message--warning > p')
    #ip策略名称输入错误提示信息
    name_error_loc = (By.CSS_SELECTOR,'body > div.el-dialog__wrapper.ps-dialog > div > div.el-dialog__body > div > div.scrollbar-wrapper.el-scrollbar__wrap > div > div > div > form > div.el-form-item.is-error.is-required > div > div.el-form-item__error')
    #确定
    queding_loc = (By.CSS_SELECTOR,'body > div.el-dialog__wrapper.ps-dialog > div > div.el-dialog__footer > div > div > button.el-button.el-button--primary')


    #操作元素
    def click_kaifang_api_loc(self):
        self.find_element(*self.kaifang_api_loc).click()
    def click_ip_loc(self):
        self.find_element(*self.ip_loc).click()
    def mouse_loc(self):
        mouse = self.find_element(*self.shubiao_loc)
        ActionChains(self.driver).move_to_element(mouse).perform()

    def click_ip_creat_loc(self):
        #点击创建ip访问控制
        self.find_element(*self.ip_creat_loc).click()
        time.sleep(2)

        #清空输入框
    def clear_content_loc(self):
        self.find_element(*self.name_loc).clear()
        self.find_element(*self.miaoshu_loc).clear()

    def input_content_loc(self,value1,value2):
        self.find_element(*self.name_loc).send_keys(value1)
        self.find_element(*self.miaoshu_loc).send_keys(value2)
        time.sleep(2)

        # 点击类型筛选
    def click_leixing_loc(self):
        self.find_element(*self.leixing_loc).click()
        time.sleep(2)
        #移动鼠标到拒绝元素上
        mouse = self.find_element(*self.reject_loc)
        ActionChains(self.driver).move_to_element(mouse).perform()
        time.sleep(2)
        #点击拒绝元素
        self.find_element(*self.reject_loc).click()

    # ip策略名称为空提示信息
    def get_name_null(self):
        return self.find_element(*self.name_null_loc).text

    # ip策略名称重复提示信息
    def get_name_repeat(self):
        return self.find_element(*self.name_repeat_loc).text
    # ip策略名称错误提示信息
    def get_name_error(self):
        return self.find_element(*self.name_error_loc).text

    def click_queding_loc(self):
        self.find_element(*self.queding_loc).click()


