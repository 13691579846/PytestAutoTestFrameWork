"""
------------------------------------
@Time : 2019/4/15 12:04
@Auth : linux超
@File : clipboard.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
import win32con
import win32clipboard as wc


class ClipBoard(object):
    """设置剪切板内容和获取剪切板内容"""

    @staticmethod
    def get_text():
        """获取剪切板的内容"""
        wc.OpenClipboard()
        value = wc.GetClipboardData(win32con.CF_TEXT)
        wc.CloseClipboard()
        return value

    @staticmethod
    def set_text(value):
        """设置剪切板的内容"""
        wc.OpenClipboard()
        wc.EmptyClipboard()
        wc.SetClipboardData(win32con.CF_UNICODETEXT, value)
        wc.CloseClipboard()


if __name__ == '__main__':
    pass
