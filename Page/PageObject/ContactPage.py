"""
------------------------------------
@Time : 2019/4/12 12:29
@Auth : linux超
@File : ContactPage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from Page.BasePage import BasePage
# ---------------------------------------------------------------------------------
# 页面元素
new_contact = ('xpath', '//span[text()="新建联系人"]')
name = ('id', 'input_N')
mail = ('xpath', '//div[@id="iaddress_MAIL_wrap"]//input[@class="nui-ipt-input"]')
star = ('xpath', 'span[@class="nui-chk-text"]/preceding-sibling::span/b')
phone = ('xpath', "//div[@id='iaddress_TEL_wrap']//input[@class='nui-ipt-input']")
comment = ('id', "input_DETAIL")
commit = ('xpath', "//span[text()='确 定']")
# ---------------------------------------------------------------------------------

class ContactPage(BasePage):

    def newContact(self, Name='', Mail='', Star=None, Phone='', Comment=''):
        '''添加联系人'''
        print('--------string add contact--------')
        self.click(*new_contact)
        self.sendKeys(*name, Name)
        self.sendKeys(*mail, Mail)
        if Star:
            self.click(*star)
        self.sendKeys(*phone, Phone)
        self.sendKeys(*comment, Comment)
        self.click(*commit)
        print('--------end add contact--------')
if __name__ == '__main__':
    from selenium import webdriver
    from Page.PageObject.LoginPage import LoginPage
    from Page.PageObject.HomePage import HomePage
    driver = webdriver.Firefox()
    home = HomePage(driver)
    login = LoginPage(driver)
    contact = ContactPage(driver)

    login.login('linuxxiaochao', 'xiaochao11520')
    home.selectMenu()
    contact.newContact('281754041@qq.com')


