"""
------------------------------------
@Time : 2019/4/12 16:15
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

# ---------------------------------------------------------------------------------
# 测试数据
# Name='', Mail='', Star=None, Phone='', Comment=''
contactData = [('linux1', '1@qq.com', '', '13691579841', 'test1'),
               ('linux2', '281754042@.com', '', '13691579842', 'test1'),
               ('linux3', '043@qq.cn', '', '13691579843', 'test1'),
               ('linux4', '', '', '13691579843', 'test1'),
               ('linux3', '281754043@qq', '', '13691579843', 'test1'),
               ('linux3', '@qq.com', '', '13691579843', 'test1')]
# ---------------------------------------------------------------------------------

@pytest.mark.newcontact
@pytest.mark.parametrize('Name, Mail, Star, Phone, Comment', contactData)
def test_NewContact(driver, login, Name, Mail, Star, Phone, Comment):
    '''测试添加联系人'''
    home_page = HomePage(driver)
    contact_page = ContactPage(driver)
    home_page.selectMenu()
    contact_page.newContact(Name, Mail, Star, Phone, Comment)
    home_page.sleep(5)
    # 校验错误的邮箱是否提示信息正确
    if re.match(r'^.{1,}@[0-9a-zA-Z]{1,13}\..*$', Mail):
        contact_page.assertValueInSource(Name)
    else:
        contact_page.assertErrorTip('请正确填写邮件地址。')

if __name__=='__main__':
    pytest.main(['-v', 'test_contactCase.py'])