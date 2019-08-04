"""
------------------------------------
@Time : 2019/4/20 12:28
@Auth : linux超
@File : LoginPage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class LoginPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 选择密码登录的按钮
    password_login_btn = do_conf.get_locators_or_account('LoginPageElements', 'password_login_btn')
    # 登录框外的iframe
    frame = do_conf.get_locators_or_account('LoginPageElements', 'frame')
    # 用户名输入框
    username = do_conf.get_locators_or_account('LoginPageElements', 'username')
    # 密码输入框
    password = do_conf.get_locators_or_account('LoginPageElements', 'password')
    # 登录按钮
    loginBtn = do_conf.get_locators_or_account('LoginPageElements', 'loginBtn')
    # 登录失败的提示信息
    error_head = do_conf.get_locators_or_account('LoginPageElements', 'errorHead')
    # 登录成功后的用户显示元素
    account = do_conf.get_locators_or_account('HomePageElements', 'account')

    def login(self, username, password):
        """登录流程"""
        self.open_url()
        self.click_password_login_btn()
        self.switch_login_frame()
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()

    def open_url(self):
        return self.load_url('https://mail.126.com')

    def click_password_login_btn(self):
        return self.click(*LoginPage.password_login_btn)

    def switch_login_frame(self):
        return self.switch_to_frame(*LoginPage.frame)

    def clear_username(self):
        return self.clear(*LoginPage.username)

    def input_username(self, username):
        self.clear_username()
        return self.send_keys(*LoginPage.username, username)

    def clear_password(self):
        return self.clear(*LoginPage.password)

    def input_password(self, password):
        self.clear_password()
        return self.send_keys(*LoginPage.password, password)

    def click_login_btn(self):
        return self.click(*LoginPage.loginBtn)

    def switch_default_frame(self):
        return self.switch_to_default_frame()

    def get_error_text(self):
        return self.get_element_text(*LoginPage.error_head)

    def get_login_success_account(self):
        return self.get_element_text(*LoginPage.account)


if __name__ == "__main__":
    pass
