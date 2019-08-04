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
import pytest

from config.conf import ROOT_DIR, HTML_NAME

# from util.sendMailForReprot import SendMailWithReport


def main():
    if ROOT_DIR not in sys.path:
        sys.path.append(ROOT_DIR)
    # 执行用例
    args = ['--reruns', '1', '--html=' + './report/' + HTML_NAME]
    pytest.main(args)
    # 发送邮件 这里我屏蔽了 自己添加自己的邮箱信息
    # SendMailWithReport.send_mail(
    #     smtpServer, fromUser, fromPassWord,
    #     toUser, subject, contents,
    #     htmlName)


if __name__ == '__main__':
    main()
# 我的部分博客地址
# https://www.cnblogs.com/linuxchao/p/linuxchao-pytest-report.html
# https://www.cnblogs.com/linuxchao/p/linuxchao-pytest-configfile.html
# https://www.cnblogs.com/linuxchao/p/linuxchao-pytest-conftest.html
