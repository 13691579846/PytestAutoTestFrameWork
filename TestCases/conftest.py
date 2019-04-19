"""
------------------------------------
@Time : 2019/4/12 15:10
@Auth : linux超
@File : conftest.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
import pytest
from Page.PageObject.LoginPage import LoginPage#, cf
# 从配置文件中获取正确的用户名和密码
userName = LoginPage.cf.getLocatorsOrAccount('126LoginAccount', 'username')
passWord = LoginPage.cf.getLocatorsOrAccount('126LoginAccount', 'password')

@pytest.fixture(scope='function')
def login(driver):
    '''除登录用例，每一个用例的前置条件'''
    print('------------staring login------------')
    loginFunc = LoginPage(driver, 30)
    loginFunc.login(userName, passWord)
    yield
    print('------------end login------------')
    driver.delete_all_cookies()