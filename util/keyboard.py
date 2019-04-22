"""
------------------------------------
@Time : 2019/4/15 12:05
@Auth : linux超
@File : keyboard.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""

# 模拟按键
import win32api
import win32con
import time

class KeyBoard(object):
    '''模拟按键'''
    # 键盘码
    vk_code = {
        'enter' : 0x0D,
        'tab' : 0x09,
        'ctrl' : 0x11,
        'v' : 0x56,
        'a' : 0x41,
        'x' : 0x58
    }

    @staticmethod
    def keyDown(keyName):
        '''按下键'''
        keyName = keyName.lower()
        try:
            win32api.keybd_event(KeyBoard.vk_code[keyName], 0, 0, 0)
        except Exception as e:
            print('未按下enter键')
            print(e)

    @staticmethod
    def keyUp(keyName):
        '''抬起键'''
        keyName = keyName.lower()
        win32api.keybd_event(KeyBoard.vk_code[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

    @staticmethod
    def oneKey(key):
        '''模拟单个按键'''
        key = key.lower()
        KeyBoard.keyDown(key)
        time.sleep(2)
        KeyBoard.keyUp(key)

    @staticmethod
    def twoKeys(key1, key2):
        '''模拟组合按键'''
        key1 = key1.lower()
        key2 = key2.lower()
        KeyBoard.keyDown(key1)
        KeyBoard.keyDown(key2)
        KeyBoard.keyUp(key1)
        KeyBoard.keyUp(key2)

if __name__=='__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys('python')
    KeyBoard.twoKeys('ctrl', 'a')
    KeyBoard.twoKeys('ctrl', 'x')
