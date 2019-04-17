"""
------------------------------------
@Time : 2019/4/15 16:50
@Auth : linux超
@File : conf.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from datetime import datetime
import os
# 项目根目录
projectDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 报告目录
reportDir = os.path.join(projectDir, r'report')
# 当前时间
currentTime = datetime.now().strftime('%H_%M_%S')

# 邮件配置信息
# 邮件服务器
smtpServer = 'smtp.qq.com'
# 发送者
fromUser = '账号@qq.com'
# 发送者密码
fromPassWord = 'mhxvqpewblldbjhf'
# 接收者
toUser = ['账号@qq.com']# 可以同时发送给多人，追加到列表中
# 邮件标题
subject = 'xx项目自动化测试报告'
# 邮件正文
contents = '测试报告正文'
# 报告名称
htmlName = r'{}\testReport{}.html'.format(reportDir, currentTime)
# 脚本执行命令
args = r'pytest --html='+htmlName+ ' '+projectDir+' --self-contained-html'