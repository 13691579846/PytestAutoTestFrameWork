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
from Page.PageObject.LoginPage import LoginPage

@pytest.fixture(scope='function')
def login(driver):
    '''除登录用例，每一个用例的前置条件'''
    print('------------staring login------------')
    loginFunc = LoginPage(driver, 30)
    loginFunc.login('账号', 'xiaochao11520') # 这里一定要传递正确的用户和密码
    yield
    print('------------end login------------')
    driver.delete_all_cookies()