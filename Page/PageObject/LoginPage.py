"""
------------------------------------
@Time : 2019/4/12 12:28
@Auth : linux超
@File : LoginPage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from Page.BasePage import BasePage, cf

# ---------------------------------------------------------------------------------
# 页面元素
# frame = ('xpath', '//div[@id="loginDiv"]/iframe')
# username = ('xpath', '//input[@name="email"]')
# password = ('xpath', '//input[@name="password"]')
# loginBtn = ('xpath', '//a[@id="dologin"]')
# 配置文件读取元素
frame = cf.getLocatorsOrAccount('LoginPageElements', 'frame')
username = cf.getLocatorsOrAccount('LoginPageElements', 'username')
password = cf.getLocatorsOrAccount('LoginPageElements', 'password')
loginBtn = cf.getLocatorsOrAccount('LoginPageElements', 'loginBtn')
ferrorHead = cf.getLocatorsOrAccount('LoginPageElements', 'ferrorHead') # 登录失败提示
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

    # add at 2019/04/19
    def assertTextEqString(self, expected, name = None):
        '''断言提示信息是否与期望的值相等'''
        self.switchToFrame(*frame)
        text = self.getElementText(*ferrorHead, name)
        self.switchToDefaultFrame()
        print('info: assert "{}" == "{}"'.format(text, expected))
        assert text == expected, '{} ！= {}'.format(text, expected)

if __name__=="__main__":
    from selenium import webdriver
    driver = webdriver.Firefox()
    login = LoginPage(driver, 30)
    login.login('lin', '')
    login.assertTextEqString('请输入密码')
