"""
------------------------------------
@Time : 2019/4/20 10:04
@Auth : linux超
@File : test_sendMailCase.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
import pytest
from Page.PageObject.SendMailPage import SendMailPage

@pytest.mark.sendMailTest
class TestSendMail(object):

    sendMailSheet = SendMailPage.getSheet('mail')
    data = SendMailPage.excel.getAllValuesOfSheet(sendMailSheet)

    @pytest.mark.sendmail
    @pytest.mark.parametrize('Address, Subject, Text, PFA', data)
    def test_sendMail(self, driver, login, Address, Subject, Text,PFA):
        """测试发送邮件，包括带附件的邮件"""
        send_mail = SendMailPage(driver)
        send_mail.sendMail(Address, Subject, Text, PFA)
        send_mail.sleep(5)
        assert send_mail.isElementExsit(*SendMailPage.expect)

if __name__=='__main__':
    pytest.main(['-v', 'test_sendMailCase.py'])