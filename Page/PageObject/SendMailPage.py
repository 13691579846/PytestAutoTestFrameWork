"""
------------------------------------
@Time : 2019/4/15 9:16
@Auth : linux超
@File : SendMailPage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from Page.BasePage import BasePage, cf

# ---------------------------------------------------------------------------------
# 页面元素
# writeMail = ('xpath', "//div[@id='dvNavContainer']//span[text()='写 信']")
# addressee = ('xpath', "//input[@aria-label='收件人地址输入框，请输入邮件地址，多人时地址请以分号隔开']")
# subject = ('xpath', "//input[contains(@id, '_subjectInput')]")
# iframe = ('xpath', '//iframe[@class="APP-editor-iframe"]')
# text = ('xpath', '/html/body')
# sendBtn = ('xpath', "//header//span[text()='发送']")
# expect = ('xpath', "//h1[contains(@id,'_succInfo')]")
# uploadAttachment = ('xpath', '//div[@title="点击添加附件"]')
# delete = ('xpath', "//a[text()='删除']")
writeMail = cf.getLocatorsOrAccount('SendMailPageElements', 'writeMail')
addressee = cf.getLocatorsOrAccount('SendMailPageElements', 'writeMail')
subject = cf.getLocatorsOrAccount('SendMailPageElements', 'writeMail')
iframe = cf.getLocatorsOrAccount('SendMailPageElements', 'writeMail')
text = cf.getLocatorsOrAccount('SendMailPageElements', 'writeMail')
sendBtn = cf.getLocatorsOrAccount('SendMailPageElements', 'writeMail')
expect = cf.getLocatorsOrAccount('SendMailPageElements', 'expect')
uploadAttachment = cf.getLocatorsOrAccount('SendMailPageElements', 'writeMail')
delete = cf.getLocatorsOrAccount('SendMailPageElements', 'writeMail')
# ---------------------------------------------------------------------------------

class SendMailPage(BasePage):


    def sendMail(self, Address, Subject, Text, Flag = 0, PFA=''):
        '''发送邮件功能'''
        print('------------string send mail---------------------')
        self.click(*writeMail)
        self.sendKeys(*addressee, Address)
        self.sendKeys(*subject, Subject)
        self.switchToFrame(*iframe)
        self.sendKeys(*text, Text)
        self.switchToDefaultFrame()
        if Flag:
            self.click(*uploadAttachment)
            self.ctrlV(PFA)
            self.enterKey()
            self.waitElementtobelocated(*delete)
        self.click(*sendBtn)
        print('------------end send mail---------------------')

if __name__=='__main__':
    from Page.PageObject.LoginPage import LoginPage
    from selenium import webdriver
    driver = webdriver.Firefox()

    login = LoginPage(driver)
    login.login('账号', 'xiaochao11520')
    sendMail = SendMailPage(driver)
    sendMail.sendMail('281754043@qq.com', 'pytest', 'pytest实战实例', 1, 'D:\KeyWordDriverTestFrameWork\geckodriver.log')