from selenium.webdriver.support.wait import WebDriverWait

'''
这个类主要是完成所有页面的一些公共方法的封装
'''
class Action(object):
    #初始化
    def __init__(self,se_driver):
        self.driver = se_driver

    #定义open方法
    def open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    #重写元素定位的方法
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,20).until(lambda driver:driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print(u"%s 页面中未能找到 %s"%(self, loc))

    #定义script方法，用于执行js脚本
    def script(self,src):
        self.driver.execute_script(src)

    #重写send_keys方法
    def send_keys(self, loc, value, clear_first=True, clik_first=True):
        try:
            if clik_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print(u"%s未找到%s"%(self,loc))

    # 免验证码登录
    def  send_cookie(self):
        cookie = {'name': 'token',
                               'value': 'BearereyJhbGciOiJIUzUxMiJ9.eyJ1c2VySWRzIjoiMTgwZGZlMWM1OTNiNGU5ODk4YzVhNmZkZjIyNTVmNTIiLCJ0ZW5hbnRJZCI6IjMwNjYwMzYwMDI5NTI4NDczNiIsInVzZXJOYW1lIjoieWlueGlvbmciLCJleHAiOjE1Nzg5NDA4MTksInVzZXJJZCI6IjE4MGRmZTFjNTkzYjRlOTg5OGM1YTZmZGYyMjU1ZjUyIn0.Dq5U_Qb-gpoAzDqsNW2v37kkAcomxDM8xIxWM5qImrzYJ9p3ErCtW_uMgYBiK4HbBsJoTgeAHu8wucIMiUkzFg'}
        self.driver.add_cookie(cookie)


#封装的截图装饰器
class Screen(object):
    u'''这个是截图功能的装饰器'''
    def __init__(self, driver):
        self.driver = driver
    def __call__(self, f):
        def inner(*args):
            try:
                return f(*args)
            except:
                import time
                nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
                pic_path = "C:\\Users\\pact.PACT-20170616CE\\PycharmProjects\\UI自动化测试\\api-auto-test\\report\\screenshot" + "\\" + nowTime + ".png"
                self.driver.get_screenshot_as_file(pic_path)
                raise
        return inner