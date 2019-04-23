"""
------------------------------------
@Time : 2019/4/15 9:16
@Auth : linux超
@File : SendMailPage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from Page.BasePage import BasePage

class SendMailPage(BasePage):

    # 配置文件读取元素
    writeMail = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'writeMail')
    addressee = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'addressee')
    subject = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'subject')
    iframe = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'iframe')
    text = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'text')
    sendBtn = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'sendBtn')
    expect = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'expect')
    uploadAttachment = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'uploadAttachment')
    delete = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'delete')

    def sendMail(self, Address, Subject, Text, PFA=''):
        '''发送邮件功能'''
        print('------------string send mail---------------------')
        self.click(*SendMailPage.writeMail)
        self.sendKeys(*SendMailPage.addressee, Address)
        self.sendKeys(*SendMailPage.subject, Subject)
        self.switchToFrame(*SendMailPage.iframe)
        self.sendKeys(*SendMailPage.text, Text)
        self.switchToDefaultFrame()
        if PFA:
            self.click(*SendMailPage.uploadAttachment)
            self.ctrlV(PFA)
            self.enterKey()
            self.waitElementtobelocated(*SendMailPage.delete)
        self.click(*SendMailPage.sendBtn)
        print('------------end send mail---------------------')

if __name__=='__main__':
    from Page.PageObject.LoginPage import LoginPage
    from selenium import webdriver
    driver = webdriver.Firefox()

    login = LoginPage(driver)
    login.login('账号', 'xiaochao11520')
    sendMail = SendMailPage(driver)
    sendMail.sendMail('281754043@qq.com', 'pytest', 'pytest实战实例', 1, 'D:\KeyWordDriverTestFrameWork\geckodriver.log')