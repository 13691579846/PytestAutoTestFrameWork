"""
------------------------------------
@Time : 2019/4/19 15:49
@Auth : linux超
@File : test.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""

import re
# [0-9a-zA-Z_]*.@\s*.com
# ^[0-9a-zA-Z_]{1,}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$
text = input('>>')
if re.match(r'^.{1,}@[0-9a-zA-Z]{1,13}\..*$', text):
    print('正确')
else:
    print('错误')
