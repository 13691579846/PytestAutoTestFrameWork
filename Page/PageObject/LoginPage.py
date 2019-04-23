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

class LoginPage(BasePage):

    # 配置文件读取元素
    frame = BasePage.cf.getLocatorsOrAccount('LoginPageElements', 'frame')
    username = BasePage.cf.getLocatorsOrAccount('LoginPageElements', 'username')
    password = BasePage.cf.getLocatorsOrAccount('LoginPageElements', 'password')
    loginBtn = BasePage.cf.getLocatorsOrAccount('LoginPageElements', 'loginBtn')
    ferrorHead = BasePage.cf.getLocatorsOrAccount('LoginPageElements', 'ferrorHead')  # 登录失败提示

    def login(self, userName, passWord):
        '''登录'''
        print('-------staring login-------')
        self.loadUrl('https://mail.126.com')
        self.switchToFrame(*LoginPage.frame)
        self.clear(*LoginPage.username)
        self.sendKeys(*LoginPage.username, userName)
        self.clear(*LoginPage.password)
        self.sendKeys(*LoginPage.password, passWord)
        self.click(*LoginPage.loginBtn)
        self.switchToDefaultFrame()
        print('---------end login---------')

    # add at 2019/04/19
    def assertTextEqString(self, expected, name = None):
        '''断言提示信息是否与期望的值相等'''
        self.switchToFrame(*LoginPage.frame)
        text = self.getElementText(*LoginPage.ferrorHead, name)
        self.switchToDefaultFrame()
        print('info: assert "{}" == "{}"'.format(text, expected))
        assert text == expected, '{} ！= {}'.format(text, expected)

if __name__=="__main__":
    from selenium import webdriver
    driver = webdriver.Firefox()
    login = LoginPage(driver, 30)
    login.login('lin', '')
    login.assertTextEqString('请输入密码')
