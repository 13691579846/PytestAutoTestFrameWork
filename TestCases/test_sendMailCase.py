"""
------------------------------------
@Time : 2019/4/15 10:04
@Auth : linux超
@File : test_sendMailCase.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
import pytest
from Page.PageObject.SendMailPage import SendMailPage

# ---------------------------------------------------------------------------------
# 测试数据 0和1 标记是否发送附件
# Address, Subject, Text
mailData = [
('281754043@qq.com', 'pytest测试主题1', 'pytest 测试邮件, 请勿回复!', 0, ''),
('281754043@qq.com', 'pytest测试主题2', 'pytest 测试邮件, 请勿回复!', 1, 'D:\KeyWordDriverTestFrameWork\geckodriver.log'),
('281754043@qq.com', 'pytest测试主题3', 'pytest 测试邮件, 请勿回复!', 1, 'D:\KeyWordDriverTestFrameWork\geckodriver.log'),
]
# ---------------------------------------------------------------------------------

@pytest.mark.sendmail
@pytest.mark.parametrize('Address, Subject, Text, Flag, PFA', mailData)
def test_sendMail(driver, login, Address, Subject, Text, Flag, PFA):
    '''测试发送邮件，包括带附件的邮件'''
    send_mail = SendMailPage(driver)
    send_mail.sendMail(Address, Subject, Text, Flag, PFA)
    send_mail.sleep(5)
    assert send_mail.isElementExsit(*SendMailPage.expect)

if __name__=='__main__':
    pytest.main(['-v', 'test_sendMailCase.py'])