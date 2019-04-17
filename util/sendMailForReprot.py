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

class sendMailWithReport(object):
    @staticmethod
    def sendMail(smtpServer, fromUser, fromPassWord, toUser, subject, contents, fileName):
        # 初始化服务器等信息
        yag = yagmail.SMTP(fromUser, fromPassWord, smtpServer)
        # 发送邮件
        yag.send(toUser, subject, contents, fileName)
if __name__=='__main__':
    sendMailWithReport.sendMail('smtp.qq.com', '281754043@qq.com', 'mhxvqpewblldbjhf', '281754043@qq.com',
                                'python自动化测试', '邮件正文',
                              '17_12_07.html')
