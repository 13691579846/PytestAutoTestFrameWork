"""
------------------------------------
@Time : 2019/4/16 15:38
@Auth : linux超
@File : sendMailForReprot.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""

import yagmail


class SendMailWithReport(object):
    """发送邮件"""

    @staticmethod
    def send_mail(smtp_server, from_user, from_pass_word, to_user, subject, contents, file_name):
        # 初始化服务器等信息
        yag = yagmail.SMTP(from_user, from_pass_word, smtp_server)
        # 发送邮件
        yag.send(to_user, subject, contents, file_name)


if __name__ == '__main__':
    SendMailWithReport.send_mail('smtp.qq.com',
                                 '账号@qq.com',
                                 'mhxvqpewblldbjhf',
                                 '账号@qq.com',
                                 'python自动化测试',
                                 '邮件正文',
                                 '17_12_07.html')
