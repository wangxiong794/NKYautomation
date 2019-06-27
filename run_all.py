''''''
from testcase import budget_test,constructionproject_test,contract_test,meeting_test,purchase_test,revenue_test,pay_test,\
    asset_test
# import os
def run_all():
    print('佛祖保佑，全部通过')
    import unittest
    from BeautifulReport import BeautifulReport
    suite=unittest.TestSuite()
    suite1=unittest.defaultTestLoader.loadTestsFromModule(pay_test)
    suite2=unittest.defaultTestLoader.loadTestsFromModule(constructionproject_test)
    suite3=unittest.defaultTestLoader.loadTestsFromModule(contract_test)
    suite4=unittest.defaultTestLoader.loadTestsFromModule(meeting_test)
    suite5=unittest.defaultTestLoader.loadTestsFromModule(purchase_test)
    suite6=unittest.defaultTestLoader.loadTestsFromModule(revenue_test)
    suite7=unittest.defaultTestLoader.loadTestsFromModule(budget_test)
    suite8=unittest.defaultTestLoader.loadTestsFromModule(asset_test)
    suite.addTests([suite1,suite2,suite3,suite4,suite5,suite6,suite7,suite8])
    BeautifulReport(suite).report(filename='TestReport', description='内控易测试报告',report_dir=".")    #log_path='.'把report放到当前目录下   
def send_report():
    from email.header import Header
    from email.mime.text import MIMEText
    from email.utils import parseaddr, formataddr
    import smtplib
    from email.mime.multipart import MIMEMultipart
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))
    from_addr = '1280490756@qq.com'#自己的邮箱账号
    password = 'ctzgyuxebocpbaed'#该QQ形成的动态密码，如更换QQ，则要开启smtp服务，复制服动态码
    to_addr = ['1334819965@qq.com','wangxiong@neikongyi.com']#接收人的邮箱账号
    smtp_server = 'smtp.qq.com'
    msg =MIMEMultipart()
    msg['From'] = _format_addr('王雄<%s>' % from_addr)#发件人
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('自动化测试用例执行情况', 'utf-8').encode()#标题
    msg.attach(MIMEText('用例执行情况，可见附件' ))
    #此处为测试报告的存放路径，如要运行代码，则要修改为当前path的文件
    att1 = MIMEText(open(r'D:\eclipse\work\neikongyi\TestReport1.html', 'rb').read(),'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="TestReport.html"' #这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att1)
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
if __name__ == '__main__':
    run_all()
    send_report()
    