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
from Page.PageObject.LoginPage import LoginPage, cf

# ---------------------------------------------------------------------------------
# 测试数据
loginData = [('linux', ''),
            ('', 'chao'),
            ('l', 'chao'),
            ('', '')]
userName = cf.getLocatorsOrAccount('126LoginAccount', 'username')
passWord = cf.getLocatorsOrAccount('126LoginAccount', 'password')
# ---------------------------------------------------------------------------------

@pytest.fixture()
def teardown_func(driver):
    '''
    执行每个用例之后要清除一下cookie，
    否则你第一个账号登录之后，重新加载网址还是登录状态，无法测试后面的账号
    '''
    yield
    driver.delete_all_cookies()

@pytest.mark.login
@pytest.mark.parametrize('username, password', loginData)
def test_login(teardown_func, driver, username, password):
    '''测试登录'''
    login = LoginPage(driver, 30)
    login.login(username, password)
    login.sleep(5)

    # 增加登录失败时， 对提示信息的验证
    if username == userName and password == passWord:
        login.assertValueInSource('写 信')
    elif username == '':
        login.assertTextEqString('请输入帐号')
    elif username != '' and password == '':
        login.assertTextEqString('请输入密码')
    elif username == '' and password == '':
        login.assertTextEqString('请输入帐号')
    else:
        login.assertTextEqString('帐号或密码错误')

if __name__=="__main__":
    pytest.main(['-v', 'test_loginCase.py'])
