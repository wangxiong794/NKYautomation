# coding=utf-8
import smtplib
import time
import unittest
from BeautifulReport import BeautifulReport
import os

# 获取路径
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

cur_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前文件的当前路径
case_path = os.path.join(cur_path, "test_case\\nky_bpm")  # 在当前文件路径找名为testcase的文件夹
if not os.path.exists(case_path):
    print("测试用例需放到‘case’文件目录下")
    os.mkdir(case_path)
report_path = os.path.join(cur_path, "report")  # 在当前文件路径找名为report的文件夹,用来存报告
if not os.path.exists(report_path): os.mkdir(report_path)  # 如果没有该文件夹，就创建文件夹


def add_case():
    """加载所有的测试用例"""
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(r".\\test_case\\nky_bpm", "*test.py",)
    suite.addTest(discover)

    filename = 'test' + str(time.strftime('%y%m%d%H%M%S')) + '.html'
    BeautifulReport(suite).report(filename=filename, description='测试报告',)


def send_report():
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    from_addr = '1280490756@qq.com'  # 自己的邮箱账号
    password = 'ppsmcagezvueffha'  # 该QQ形成的动态密码，如更换QQ，则要开启smtp服务，复制服动态码
    to_addr = ['1334819965@qq.com', 'wangxiong@neikongyi.com']  # 接收人的邮箱账号
    smtp_server = 'smtp.qq.com'
    msg = MIMEMultipart()
    msg['From'] = _format_addr('王雄<%s>' % from_addr)  # 发件人
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)

    msg['Subject'] = Header('自动化测试用例执行情况', 'utf-8').encode()  # 标题
    msg.attach(MIMEText('用例执行情况' + time.strftime("%Y-%m-%d %H:%M:%S") + '，可见附件'))
    # 此处为测试报告的存放路径，如要运行代码，则要修改为当前path的文件
    att1 = MIMEText(open(r'E:\eclipse\work\neikongyi\report\TestReport.html', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="TestReport' + time.strftime(
        "%Y-%m-%d") + '.html"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att1)
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()


if __name__ == "__main__":
    # 用例集合
    add_case()

