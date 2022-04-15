# coding=utf-8
# 本义该文件用于定时分析错误日志，来用于下一步处理，放啊没够想好，没时间改了。
import os.path

import paramiko
from service.logger import Log
import re
from get_root_path import root_dir

los = Log()
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('101.201.120.189',22,'root','nky2018')
# stdin, stdout, stderr = ssh.exec_command('cat /var/lib/tomcat8/logs/log.log')
# msg = stdout.read().decode('utf-8')
# los.info(msg)
path1=os.path.join(os.path.join(root_dir), 'logs'), '2022_03_04.log'
print(path1)
# l1 = open(path,'r',encoding='utf-8')
# print(l1)
# l1=l1.read()
# # print(msg)
# msg2 = re.match(r'测试',l1)
# print(msg2)
# # ssh.close()
