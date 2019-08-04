"""
------------------------------------
@Time : 2019/8/4 13:05
@Auth : linux超
@File : login_data.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""


class LoginData(object):
    """用户登录测试数据"""

    login_success_data = [
        (
            "linuxxiaochao",
            "xiaochao11520",
            "linuxxiaochao@126.com"
        )
    ]

    login_fail_data = [
        (
            "linuxxiaochao",
            "",
            "请输入密码"
        ),
        (
            "",
            "xiaochao11520",
            "请输入帐号"
        ),
        (
            "linux",
            "xiaochao",
            "帐号或密码错误"
        )
    ]


if __name__ == '__main__':
    pass
