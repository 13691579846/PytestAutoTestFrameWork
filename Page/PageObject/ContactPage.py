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
# new_contact = ('xpath', '//span[text()="新建联系人"]')
# name = ('id', 'input_N')
# mail = ('xpath', '//div[@id="iaddress_MAIL_wrap"]//input[@class="nui-ipt-input"]')
# star = ('xpath', 'span[@class="nui-chk-text"]/preceding-sibling::span/b')
# phone = ('xpath', "//div[@id='iaddress_TEL_wrap']//input[@class='nui-ipt-input']")
# comment = ('id', "input_DETAIL")
# commit = ('xpath', "//span[text()='确 定']")
# ---------------------------------------------------------------------------------

class ContactPage(BasePage):

    # 配置文件读取元素
    new_contact = BasePage.cf.getLocatorsOrAccount('ContactPageElements', 'new_contact')
    name = BasePage.cf.getLocatorsOrAccount('ContactPageElements', 'name')
    mail = BasePage.cf.getLocatorsOrAccount('ContactPageElements', 'mail')
    star = BasePage.cf.getLocatorsOrAccount('ContactPageElements', 'star')
    phone = BasePage.cf.getLocatorsOrAccount('ContactPageElements', 'phone')
    comment = BasePage.cf.getLocatorsOrAccount('ContactPageElements', 'comment')
    commit = BasePage.cf.getLocatorsOrAccount('ContactPageElements', 'commit')
    errortip = BasePage.cf.getLocatorsOrAccount('ContactPageElements', 'tooltip')  # 错误提示

    def newContact(self, Name='', Mail='', Star=None, Phone='', Comment=''):

        '''添加联系人'''
        print('--------string add contact--------')
        self.click(*ContactPage.new_contact)
        self.sendKeys(*ContactPage.name, Name)
        self.sendKeys(*ContactPage.mail, Mail)
        if Star:
            self.click(*ContactPage.star)
        self.sendKeys(*ContactPage.phone, Phone)
        self.sendKeys(*ContactPage.comment, Comment)
        self.click(*ContactPage.commit)
        print('--------end add contact--------')

    def assertErrorTip(self, excepted):
        '''断言联系人添加失败时是否有提示信息'''
        text = self.getElementText(*ContactPage.errortip)
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


