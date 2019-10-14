from selenium.webdriver.common.by import By
from PO import base_page
from selenium.webdriver import ActionChains
import time

#继承base后既可以调用base的方法也可自己添加新的方法
class api_editPage(base_page.Action):

    #通过xpath进行定位元素

    #开放api
    kaifang_api_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[3]/li/div')
    #api管理
    api_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/ul/div[3]/li/ul/div[2]/span/li/span')
    # 鼠标悬停
    shubiao_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/form/div[2]/label')
    #api名称输入框
    api_name_input_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/form/div[1]/div/div/input')
    #api名称
    api_name_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/div[1]/div[3]/table/tbody/tr[2]/td[1]/div/button/span')
    #api授权
    api_authorize_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/section/section/main/div[1]/div[4]/div[2]/table/tbody/tr[2]/td[5]/div/button[2]/span')
    #api授权界面应用id查询输入框
    appid_input_search_loc = (By.CSS_SELECTOR,'body > div.el-dialog__wrapper.ps-dialog > div > div.el-dialog__body > div > div.scrollbar-wrapper.el-scrollbar__wrap > div > div > div > div.el-row > div.el-col.el-col-16 > form > div:nth-child(2) > div > div > input')
    #api授权界面应用id查询按钮
    appid_search_loc = (By.CSS_SELECTOR,'body > div.el-dialog__wrapper.ps-dialog > div > div.el-dialog__body > div > div.scrollbar-wrapper.el-scrollbar__wrap > div > div > div > div.el-row > div.el-col.el-col-16 > form > div:nth-child(3) > div > button')
    #添加app
    app_add_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div[1]/div/div/div/div[3]/div[1]/div[1]/div[4]/div[2]/table/tbody/tr/td[4]/div/button/span')
    #确定
    queding_loc = (By.XPATH,'/html/body/div[2]/div/div[3]/div/div/button[2]/span')
    #授权信息
    api_shouquan_loc =(By.XPATH,'//*[@id="tab-1"]')
    #解绑
    jiebang_loc = (By.XPATH,'//*[@id="pane-1"]/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[5]/div/button')
    #api详情界面查询输入框
    xiangqing_search_loc = (By.XPATH,'//*[@id="pane-1"]/div/div[1]/div[2]/form/div/div/div/input')
    #api详情查询按钮
    search_loc = (By.XPATH,'//*[@id="pane-1"]/div/div[1]/div[2]/form/button')
    #解绑成功后的提示信息
    jiebang_tips_loc = (By.CSS_SELECTOR,'body > div.el-message.el-message--success')


    #操作元素
    def click_kaifang_api_loc(self):
        self.find_element(*self.kaifang_api_loc).click()
    def click_api_loc(self):
        self.find_element(*self.api_loc).click()
    def mouse_loc(self):
        mouse = self.find_element(*self.shubiao_loc)
        ActionChains(self.driver).move_to_element(mouse).perform()
    def click_api_name_loc(self):
        self.find_element(*self.api_name_loc).click()
        time.sleep(2)
    def click_api_shouquan_loc(self):
        self.find_element(*self.api_shouquan_loc).click()
    def click_jiebang_loc(self):
        self.find_element(*self.jiebang_loc).click()
    def input_name_loc(self,value):
        self.find_element(*self.xiangqing_search_loc).send_keys(value)
    def click_search_loc(self):
        self.find_element(*self.search_loc).click()
    #解绑成功的提示
    def get_jiebang_tips_loc(self):
        return self.find_element(*self.jiebang_tips_loc).text

    def click_api_authorize_loc(self):
        self.find_element(*self.api_authorize_loc).click()
    def input_appid_loc(self,value):
        self.find_element(*self.appid_input_search_loc).send_keys(value)
    def click_appid_search_loc(self):
        self.find_element(*self.appid_search_loc).click()
    def click_app_add_loc(self):
        self.find_element(*self.app_add_loc).click()
    def click_queding_loc(self):
        self.find_element(*self.queding_loc).click()