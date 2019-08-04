"""
------------------------------------
@Time : 2019/4/20 12:28
@Auth : linux超
@File : HomePage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class HomePage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 首页
    homePage = do_conf.get_locators_or_account('HomePageElements', 'homePage')
    # 通讯录
    mailList = do_conf.get_locators_or_account('HomePageElements', 'mailList')
    # 应用中心
    applicationCenter = do_conf.get_locators_or_account('HomePageElements', 'applicationCenter')
    # 收件箱
    inBox = do_conf.get_locators_or_account('HomePageElements', 'inBox')

    def select_menu(self, menu='mailList'):
        if menu == "mailList":
            self.click_address_list_menu()
        elif menu == 'homePage':
            self.click_home_page_menu()
        elif menu == 'applicationCenter':
            self.click_application_center_menu()
        elif menu == 'inBox':
            self.click_in_box_menu()
        else:
            raise ValueError(
                '''菜单选择错误!
                homePage->首页
                mailList->通讯录
                applicationCenter->应用中心
                inBox->收件箱'''
            )

    def click_home_page_menu(self):
        return self.click(*HomePage.homePage)

    def click_address_list_menu(self):
        return self.click(*HomePage.mailList)

    def click_application_center_menu(self):
        return self.click(*HomePage.applicationCenter)

    def click_in_box_menu(self):
        return self.click(*HomePage.inBox)


if __name__ == '__main__':
    pass
