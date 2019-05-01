"""
------------------------------------
@Time : 2019/4/15 16:14
@Auth : linux超
@File : RunTestCase.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
import sys
sys.path.append('.')
from config.conf import *
from util.sendMailForReprot import SendMailWithReport


def main():
    # 判断项目的根目录是否在sys.path中，没有就添加
    if projectDir not in sys.path:
        sys.path.append(projectDir)
    # 执行用例
    os.system(args)
    # 发送邮件
    # SendMailWithReport.send_mail(
    #     smtpServer, fromUser, fromPassWord,
    #     toUser, subject, contents,
    #     htmlName)


if __name__ == '__main__':
    main()
# https://www.cnblogs.com/linuxchao/p/linuxchao-pytest-report.html
# https://www.cnblogs.com/linuxchao/p/linuxchao-pytest-configfile.html
# https://www.cnblogs.com/linuxchao/p/linuxchao-pytest-conftest.html