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

class TestLogin(object):

    # 测试数据
    loginSheet = LoginPage.getSheet('login')
    data = LoginPage.excel.getAllValuesOfSheet(loginSheet)

    # 正确的帐号和密码
    userName = LoginPage.cf.getLocatorsOrAccount('126LoginAccount', 'username')
    passWord = LoginPage.cf.getLocatorsOrAccount('126LoginAccount', 'password')

    @pytest.fixture()
    def teardown_func(self, driver):
        '''
        执行每个用例之后要清除一下cookie，
        否则你第一个账号登录之后，重新加载网址还是登录状态，无法测试后面的账号
        '''
        yield
        driver.delete_all_cookies()

    @pytest.mark.parametrize('username, password, expect', data)
    def test_login(self, teardown_func, driver, username, password, expect):
        '''测试登录'''
        login = LoginPage(driver, 30)
        login.login(username, password)
        login.sleep(5)
        # 增加登录失败时， 对提示信息的验证
        if username == TestLogin.userName and password == TestLogin.passWord:
            login.assertValueInSource(expect)
        elif username == '':
            login.assertTextEqString(expect)
        elif username != '' and password == '':
            login.assertTextEqString(expect)
        elif username == '' and password == '':
            login.assertTextEqString(expect)
        else:
            login.assertTextEqString(expect)


if __name__=="__main__":
    pytest.main(['-v', 'test_loginCase.py'])
