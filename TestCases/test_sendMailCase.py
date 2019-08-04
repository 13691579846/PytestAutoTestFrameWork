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

from data.send_mail_data import SendMailData


@pytest.mark.sendMailTest
class TestSendMail(object):
    """发送邮件"""
    mail_data = SendMailData
    send_success_data = mail_data.send_mail_success
    send_fail_address_is_none_data = mail_data.send_fail_address_is_none
    send_fail_address_is_invalid_data = mail_data.send_fail_address_is_invalid_data
    send_fail_subject_is_none_data = mail_data.send_fail_subject_is_none_data

    @pytest.mark.sendmail
    @pytest.mark.parametrize('address, subject, text, pfa, expect', send_success_data)
    def test_send_mail_success(self, login, refresh_page, address, subject, text, pfa, expect):
        home_page = login[1]
        send_mail_page = login[3]
        home_page.select_menu(menu="homePage")
        send_mail_page.send_mail(address, subject, text, pfa)
        send_mail_page.wait_success_info_element_located()
        actual = send_mail_page.get_source()
        assert expect in actual, "发送邮件成功, 断言失败"

    @pytest.mark.parametrize('address, subject, text, pfa, expect', send_fail_address_is_none_data)
    def test_send_fail_address_is_none(self, login, refresh_page, address, subject, text, pfa, expect):
        home_page = login[1]
        send_mail_page = login[3]
        home_page.select_menu(menu="homePage")
        send_mail_page.send_mail(address, subject, text, pfa)
        actual = send_mail_page.get_error_address_is_none()
        assert expect == actual, "发送邮件失败, 断言失败"

    @pytest.mark.parametrize('address, subject, text, pfa, expect', send_fail_address_is_invalid_data)
    def test_send_fail_address_invalid(self, login, refresh_page, address, subject, text, pfa, expect):
        home_page = login[1]
        send_mail_page = login[3]
        home_page.select_menu(menu="homePage")
        send_mail_page.send_mail(address, subject, text, pfa)
        actual = send_mail_page.get_error_popup_window()
        assert expect == actual, "发送邮件失败, 断言失败"

    @pytest.mark.parametrize('address, subject, text, pfa, expect', send_fail_subject_is_none_data)
    def test_send_fail_subject_is_none_data(self, login, refresh_page, address, subject, text, pfa, expect):
        home_page = login[1]
        send_mail_page = login[3]
        home_page.select_menu(menu="homePage")
        send_mail_page.send_mail(address, subject, text, pfa)
        actual = send_mail_page.get_error_popup_window()
        assert expect == actual, "发送邮件失败, 断言失败"


if __name__ == '__main__':
    pytest.main(['-v', 'test_sendMailCase.py'])
