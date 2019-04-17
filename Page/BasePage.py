"""
------------------------------------
@Time : 2019/4/12 8:45
@Auth : linux超
@File : BasePage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException, TimeoutException, \
    NoAlertPresentException, NoSuchFrameException
from selenium import webdriver
import time

from util.clipboard import ClipBoard
from util.keyboard import KeyBoard

class BasePage(object):
    '''
    结合显示等待封装一些selenium 内置方法
    '''
    def __init__(self, driver, outTime=30):
        self.byDic = {
        'id': By.ID,
        'name': By.NAME,
        'class_name': By.CLASS_NAME,
        'xpath': By.XPATH,
        'link_text': By.LINK_TEXT
        }
        self.driver = driver
        self.outTime = outTime

    def findElement(self, by, locator):
        '''
        find alone element
        :param by: eg: id, name, xpath, css.....
        :param locator: id, name, xpath for str
        :return: element object
        '''
        try:
            print('[Info:Starting find the element "{}" by "{}"!]'.format(locator, by))
            element = wd(self.driver, self.outTime).until(lambda x : x.find_element(by, locator))
        except TimeoutException as t:
            print('error: found "{}" timeout!'.format(locator), t)
        except NoSuchWindowException as e:
            print('error: no such "{}"'.format(locator), e)
        except Exception as e:
            raise e
        else:
            # print('[Info:Had found the element "{}" by "{}"!]'.format(locator, by))
            return element

    def findElements(self, by, locator):
        '''
        find group elements
        :param by: eg: id, name, xpath, css.....
        :param locator: eg: id, name, xpath for str
        :return: elements object
        '''
        try:
            print('[Info:start find the elements "{}" by "{}"!]'.format(locator, by))
            elements = wd(self.driver, self.outTime).until(lambda x : x.find_element(by, locator))
        except TimeoutException as t:
            print(t)
        except NoSuchWindowException as e:
            print(e)
        except Exception as e:
            raise e
        else:
            # print('[Info:Had found the elements "{}" by "{}"!]'.format(locator, by))
            return elements

    def isElementExsit(self, by, locator):
        '''
        assert element if exist
        :param by: eg: id, name, xpath, css.....
        :param locator: eg: id, name, xpath for str
        :return: if element return True else return false
        '''
        if by.lower() in self.byDic:
            try:
                wd(self.driver, self.outTime).\
                    until(EC.visibility_of_element_located((self.byDic[by], locator)))
            except TimeoutException:
                print('Error: element "{}" time out!'.format(locator))
                return False
            except NoSuchWindowException:
                print('Error: element "{}" not exsit!'.format(locator))
                return False
            return True
        else:
            print('the "{}" error!'.format(by))

    def isClick(self, by, locator):
        '''判断是否可点击,返回元素对象'''
        if by.lower() in self.byDic:
            try:
                element = wd(self.driver, self.outTime).\
                    until(EC.element_to_be_clickable((self.byDic[by], locator)))
            except Exception:
                return False
            return element
        else:
            print('the "{}" error!'.format(by))

    def isAlertAndSwitchToIt(self):
        '''
        assert alert if exsit
        :return: alert obj
        '''
        try:
            re = wd(self.driver, self.outTime).until(EC.alert_is_present())
        except NoAlertPresentException:
            return False
        except Exception:
            return False
        return re

    def switchToFrame(self, by, locator):
        '''判断frame是否存在，存在就跳到frame'''
        print('info:switching to iframe "{}"'.format(locator))
        if by.lower() in self.byDic:
            try:
                wd(self.driver, self.outTime).\
                    until(EC.frame_to_be_available_and_switch_to_it((self.byDic[by], locator)))
            except TimeoutException as t:
                print('error: found "{}" timeout！'.format(locator), t)
            except NoSuchFrameException as e:
                print('error: no such "{}"'.format(locator), e)
            except Exception as e:
                raise e
        else:
            print('the "{}" error!'.format(by))

    def switchToDefaultFrame(self):
        '''返回默认的frame'''
        print('info:switch back to default iframe')
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(e)

    def getAlertText(self):
        '''获取alert的提示信息'''
        if self.isAlertAndSwitchToIt():
            alert = self.isAlertAndSwitchToIt()
            return alert.text
        else:
            return None

    def getElementText(self, by, locator, name=None):
        '''获取某一个元素的text信息'''
        try:
            element = self.findElement(by, locator)
            if not name:
                return element.get_attribute(name)
            else:
                return element.text
        except:
            print('get "{}" text failed return None'.format(locator))
            return None

    def loadUrl(self, url):
        '''加载url'''
        print('info: string upload url "{}"'.format(url))
        self.driver.get(url)

    def getSource(self):
        '''获取页面源码'''
        return self.driver.page_source

    def sendKeys(self, by, locator, value=''):
        '''写数据'''
        print('info:input "{}"'.format(value))
        try:
            element = self.findElement(by, locator)
            element.send_keys(value)
        except AttributeError as e:
            print(e)

    def clear(self, by, locator):
        '''清理数据'''
        print('info:clearing value')
        try:
            element = self.findElement(by, locator)
            element.clear()
        except AttributeError as e:
            print(e)

    def click(self, by, locator):
        '''点击某个元素'''
        print('info:click "{}"'.format(locator))
        element = self.isClick(by, locator)
        if element:
            element.click()
        else:
            print('the "{}" unclickable!')

    def sleep(self, num=0):
        '''强制等待'''
        print('info:sleep "{}" minutes'.format(num))
        time.sleep(num)

    def ctrlV(self, value):
        '''ctrl + V 粘贴'''
        print('info:pasting "{}"'.format(value))
        ClipBoard.setText(value)
        self.sleep(3)
        KeyBoard.twoKeys('ctrl', 'v')

    def enterKey(self):
        '''enter 回车键'''
        print('info:keydown enter')
        KeyBoard.oneKey('enter')

    def waitElementtobelocated(self, by, locator):
        '''显示等待某个元素出现，且可见'''
        print('info:waiting "{}" to be located'.format(locator))
        try:
            wd(self.driver, self.outTime).until(EC.visibility_of_element_located((self.byDic[by], locator)))
        except TimeoutException as t:
            print('error: found "{}" timeout！'.format(locator), t)
        except NoSuchWindowException as e:
            print('error: no such "{}"'.format(locator), e)
        except Exception as e:
            raise e

    def assertValueInSource(self, value):
        '''断言某个关键字是否存在页面源码中'''
        print('info:assert "{}" in page source'.format(value))
        source = self.getSource()
        try:
            assert value in source, '关键字"{}"不存在源码中!'.format(value)
        except AssertionError:
            raise '关键字"{}"不存在源码中!'.format(value)

    def assertStringContainsValue(self, String, value):
        '''断言某段字符串包含另一个字符串'''
        print('info:assert "{}" contains "{}"'.format(String, value))
        try:
            assert value in String, '"{}"不包含"{}"!'.format(String, value)
        except AssertionError:
            raise '"{}"不包含"{}"!'.format(String, value)

if __name__=="__main__":
    driver = webdriver.Firefox()
    frame = ('xpath', '//div[@id="loginDiv"]/ifram')
    wait = BasePage(driver)
    driver.get('https://mail.126.com/')
    wait.switchToFrame(*frame)
    username = wait.findElement('xpath', '//input[@name="email"]')
    username.send_keys('linuxxiaochao')
    if wait.isElementExsit('xpath', '//input[@name="password"]'):
        wait.findElement('xpath', '//input[@name="password"]').send_keys('xiaochao11520')
    wait.click('xpath', '//a[@id="dologin"]')
