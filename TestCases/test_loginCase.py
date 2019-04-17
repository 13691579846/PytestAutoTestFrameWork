"""
------------------------------------
@Time : 2019/4/12 14:10
@Auth : linux超
@File : test_loginCase.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
import pytest
from Page.PageObject.LoginPage import LoginPage

# ---------------------------------------------------------------------------------
# 测试数据
loginData = [('linuxxiaochao', 'xiaochao11520'),
                ('linuxxiaochao', 'xiaochao11520'),
                ('linuxxiaochao', 'xiaochao11520')]
# ---------------------------------------------------------------------------------

@pytest.fixture()
def teardown_func(driver):
    '''
    执行每个用例之后要清除一下cookie，
    否则你第一个账号登录之后，重新加载网址还是登录状态，无法测试后面的账号
    '''
    yield
    driver.delete_all_cookies()

@pytest.mark.parametrize('username, password', loginData)
def test_login(teardown_func, driver, username, password):
    '''测试登录'''
    login = LoginPage(driver, 30)
    login.login(username, password)
    login.sleep(5)
    login.assertValueInSource(username)

if __name__=="__main__":
    pytest.main(['-v', 'test_loginCase.py'])
