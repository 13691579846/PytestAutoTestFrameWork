"""
------------------------------------
@Time : 2019/4/20 12:28
@Auth : linux超
@File : HomePage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from Page.BasePage import BasePage

class HomePage(BasePage):
    # 配置文件读取元素
    homePage = BasePage.cf.getLocatorsOrAccount('HomePageElements', 'homePage')
    mailList = BasePage.cf.getLocatorsOrAccount('HomePageElements', 'mailList')
    applicationCenter = BasePage.cf.getLocatorsOrAccount('HomePageElements', 'applicationCenter')
    inBox = BasePage.cf.getLocatorsOrAccount('HomePageElements', 'inBox')
    '''首页菜单选项'''
    def selectMenu(self, Menu='mailList'):

        if Menu == 'mailList':
            self.click(*HomePage.mailList)
        elif Menu == 'homePage':
            self.click(*HomePage.homePage)
        elif Menu == 'applicationCenter':
            self.click(*HomePage.applicationCenter)
        elif Menu == 'inBox':
            self.click(*HomePage.inBox)
        else:
            raise ValueError('''
            菜单选择错误!
            homePage->首页
            mailList->通讯录
            applicationCenter->应用中心
            inBox->收件箱''')

if __name__=='__main__':
    from selenium import webdriver
    from Page.PageObject.LoginPage import LoginPage
    driver = webdriver.Firefox()
    login = LoginPage(driver)
    login.login('账号', 'xiaochao11520')

    home = HomePage(driver)
    home.selectMenu()
