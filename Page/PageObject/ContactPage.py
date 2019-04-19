"""
------------------------------------
@Time : 2019/4/12 12:29
@Auth : linux超
@File : ContactPage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from Page.BasePage import BasePage, cf

# ---------------------------------------------------------------------------------
# 页面元素
# new_contact = ('xpath', '//span[text()="新建联系人"]')
# name = ('id', 'input_N')
# mail = ('xpath', '//div[@id="iaddress_MAIL_wrap"]//input[@class="nui-ipt-input"]')
# star = ('xpath', 'span[@class="nui-chk-text"]/preceding-sibling::span/b')
# phone = ('xpath', "//div[@id='iaddress_TEL_wrap']//input[@class='nui-ipt-input']")
# comment = ('id', "input_DETAIL")
# commit = ('xpath', "//span[text()='确 定']")
new_contact = cf.getLocatorsOrAccount('ContactPageElements', 'new_contact')
name = cf.getLocatorsOrAccount('ContactPageElements', 'name')
mail = cf.getLocatorsOrAccount('ContactPageElements', 'mail')
star = cf.getLocatorsOrAccount('ContactPageElements', 'star')
phone = cf.getLocatorsOrAccount('ContactPageElements', 'phone')
comment = cf.getLocatorsOrAccount('ContactPageElements', 'comment')
commit = cf.getLocatorsOrAccount('ContactPageElements', 'commit')
errortip = cf.getLocatorsOrAccount('ContactPageElements', 'tooltip')# 错误提示
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

    def assertErrorTip(self, excepted):
        '''断言联系人添加失败时是否有提示信息'''
        text = self.getElementText(*errortip)
        print('info: assert "{}"=="{}"'.format(text, excepted))
        assert text == excepted

if __name__ == '__main__':
    from selenium import webdriver
    from Page.PageObject.LoginPage import LoginPage
    from Page.PageObject.HomePage import HomePage
    driver = webdriver.Firefox()
    home = HomePage(driver)
    login = LoginPage(driver)
    contact = ContactPage(driver)

    login.login('账号', 'xiaochao11520')
    home.selectMenu()
    contact.newContact('281754041@qq.com')


