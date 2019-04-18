"""
------------------------------------
@Time : 2019/4/12 16:15
@Auth : linux超
@File : test_contactCase.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
import pytest
from Page.PageObject.HomePage import HomePage
from Page.PageObject.ContactPage import ContactPage

# ---------------------------------------------------------------------------------
# 测试数据
# Name='', Mail='', Star=None, Phone='', Comment=''
contactData = [('linuxChao1', '281754041@qq.com', '', '13691579841', 'test1'),
               ('linuxChao2', '281754042@qq.com', '', '13691579842', 'test1'),
               ('linuxChao3', '281754043@qq.com', '', '13691579843', 'test1')]
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
    contact_page.assertValueInSource(Name)

if __name__=='__main__':
    pytest.main(['-v', 'test_contactCase.py'])