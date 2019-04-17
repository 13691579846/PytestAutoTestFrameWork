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
import win32clipboard as WC

class ClipBoard(object):
    '''设置剪切板内容和获取剪切板内容'''
    @staticmethod
    def getText():
        '''获取剪切板的内容'''
        WC.OpenClipboard()
        value = WC.GetClipboardData(win32con.CF_TEXT)
        WC.CloseClipboard()
        return value

    @staticmethod
    def setText(value):
        '''设置剪切板的内容'''
        WC.OpenClipboard()
        WC.EmptyClipboard()
        WC.SetClipboardData(win32con.CF_UNICODETEXT, value)
        WC.CloseClipboard()

if __name__=='__main__':
    from selenium import webdriver
    value = 'python'
    driver = webdriver.Firefox()
    driver.get('http://www.baidu.com')
    query = driver.find_element_by_id('kw')
    ClipBoard.setText(value)
    clValue = ClipBoard.getText()
    query.send_keys(clValue.decode('utf-8'))