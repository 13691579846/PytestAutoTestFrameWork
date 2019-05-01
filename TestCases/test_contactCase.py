"""
------------------------------------
@Time : 2019/4/20 16:15
@Auth : linux超
@File : test_contactCase.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
import re
import pytest
from Page.PageObject.HomePage import HomePage
from Page.PageObject.ContactPage import ContactPage


@pytest.mark.conatctTest
class TestAddContact(object):

    # 测试数据
    contactSheet = ContactPage.getSheet('contact')
    data = ContactPage.excel.getAllValuesOfSheet(contactSheet)

    @pytest.mark.newcontact
    @pytest.mark.parametrize('Name, Mail, Star, Phone, Comment, expect', data)
    def test_NewContact(self, driver, login, Name, Mail, Star, Phone, Comment, expect):
        """测试添加联系人"""
        home_page = HomePage(driver)
        contact_page = ContactPage(driver)
        home_page.selectMenu()
        contact_page.newContact(Name, Mail, Star, Phone, Comment)
        home_page.sleep(5)
        # 校验错误的邮箱是否提示信息正确
        if re.match(r'^.{1,}@[0-9a-zA-Z]{1,13}\..*$', Mail):
            contact_page.assertValueInSource(expect)
        else:
            contact_page.assertErrorTip(expect)

if __name__ == '__main__':
    pytest.main(['-v', 'test_contactCase.py'])