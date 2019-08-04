"""
------------------------------------
@Time : 2019/4/20 12:29
@Auth : linux超
@File : ContactPage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class ContactPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 新键联系人按钮
    new_contact_btn = do_conf.get_locators_or_account('ContactPageElements', 'new_contact')
    # 姓名输入框
    name = do_conf.get_locators_or_account('ContactPageElements', 'name')
    # 电子邮箱输入框
    mail = do_conf.get_locators_or_account('ContactPageElements', 'mail')
    # 标记为星级
    star = do_conf.get_locators_or_account('ContactPageElements', 'star')
    # 电话号码输入框
    phone = do_conf.get_locators_or_account('ContactPageElements', 'phone')
    # 备注输入框
    comment = do_conf.get_locators_or_account('ContactPageElements', 'comment')
    # 确定按钮
    commit = do_conf.get_locators_or_account('ContactPageElements', 'commit')
    # 添加失败的提示信息
    error_tip = do_conf.get_locators_or_account('ContactPageElements', 'tooltip')

    def add_contact(self, name, mail, star, phone, comment):
        """添加联系人"""
        self.click_new_contact_btn()
        self.input_name(name)
        self.input_mail(mail)
        if star == '1':
            self.select_str()
        self.input_phone(phone)
        self.input_comment(comment)
        self.click_commit_btn()

    def click_new_contact_btn(self):
        return self.click(*ContactPage.new_contact_btn)

    def input_name(self, name):
        return self.send_keys(*ContactPage.name, name)

    def input_mail(self, mail):
        return self.send_keys(*ContactPage.mail, mail)

    def select_str(self):
        return self.click(*ContactPage.star)

    def input_phone(self, phone):
        return self.send_keys(*ContactPage.phone, phone)

    def input_comment(self, comment):
        return self.send_keys(*ContactPage.comment, comment)

    def click_commit_btn(self):
        return self.click(*ContactPage.commit)

    def get_error_text(self):
        return self.get_element_text(*ContactPage.error_tip)


if __name__ == '__main__':
    pass
