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
    """模拟按键"""
    # 键盘码
    vk_code = {
        'enter': 0x0D,
        'tab': 0x09,
        'ctrl': 0x11,
        'v': 0x56,
        'a': 0x41,
        'x': 0x58
    }

    @staticmethod
    def key_down(key_name):
        """按下键"""
        key_name = key_name.lower()
        try:
            win32api.keybd_event(KeyBoard.vk_code[key_name], 0, 0, 0)
        except Exception as e:
            print('未按下enter键')
            print(e)

    @staticmethod
    def key_up(key_name):
        """抬起键"""
        key_name = key_name.lower()
        win32api.keybd_event(KeyBoard.vk_code[key_name], 0, win32con.KEYEVENTF_KEYUP, 0)

    @staticmethod
    def one_key(key):
        """模拟单个按键"""
        key = key.lower()
        KeyBoard.key_down(key)
        time.sleep(2)
        KeyBoard.key_up(key)

    @staticmethod
    def two_keys(key1, key2):
        """模拟组合按键"""
        key1 = key1.lower()
        key2 = key2.lower()
        KeyBoard.key_down(key1)
        KeyBoard.key_down(key2)
        KeyBoard.key_up(key1)
        KeyBoard.key_up(key2)


if __name__ == '__main__':
    pass
