"""
------------------------------------
@Time : 2019/4/12 12:28
@Auth : linux超
@File : LoginPage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from Page.BasePage import BasePage

# ---------------------------------------------------------------------------------
# 页面元素
frame = ('xpath', '//div[@id="loginDiv"]/iframe')
username = ('xpath', '//input[@name="email"]')
password = ('xpath', '//input[@name="password"]')
loginBtn = ('xpath', '//a[@id="dologin"]')
# ---------------------------------------------------------------------------------

class LoginPage(BasePage):

    def login(self, userName, passWord):
        '''登录'''
        print('-------staring login-------')
        self.loadUrl('https://mail.126.com')
        self.switchToFrame(*frame)
        self.clear(*username)
        self.sendKeys(*username, userName)
        self.clear(*password)
        self.sendKeys(*password, passWord)
        self.click(*loginBtn)
        self.switchToDefaultFrame()
        print('---------end login---------')

if __name__=="__main__":
    from selenium import webdriver
    driver = webdriver.Firefox()
    login = LoginPage(driver, 30)
    login.login('账号', 'xiaochao11520')