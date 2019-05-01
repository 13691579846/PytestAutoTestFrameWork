"""
------------------------------------
@Time : 2019/4/18 10:54
@Auth : linux超
@File : parseConFile.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
import configparser
from config.conf import configDir


class ParseConFile(object):

    def __init__(self):
        self.file = configDir
        self.conf = configparser.ConfigParser()
        self.conf.read(self.file, encoding='utf-8')

    def getAllSections(self):
        """获取所有的section，返回一个列表"""
        return self.conf.sections()

    def getAllOptions(self, section):
        """获取指定section下所有的option, 返回列表"""
        return self.conf.options(section)

    def getLocatorsOrAccount(self, section, option):
        """获取指定section, 指定option对应的数据, 返回元祖和字符串"""
        try:
            locator = self.conf.get(section, option)
            if ('->' in locator):
                locator = tuple(locator.split('->'))
            return locator
        except configparser.NoOptionError as e:
            print('error:', e)
        return 'error: No option "{}" in section: "{}"'.format(option, section)

    def getOptionValue(self, section):
        """获取指定section下所有的option和对应的数据，返回字典"""
        value = dict(self.conf.items(section))
        return value


if __name__ == '__main__':
    cf = ParseConFile()
    print(cf.getAllSections())
    print(cf.getAllOptions('126LoginAccount'))
    print(cf.getLocatorsOrAccount('126LoginAccount', 'username'))
    print(cf.getOptionValue('126LoginAccount'))
