# coding=utf-8
# 内控易是打包部署后，检查redis服务、打印服务是否成功，操作为登录后，查询单据，打印单据
import json
import logging
import os
import re
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import xlrd

import requests


def read_data(row1=2, row2=157):
    # 读取登录信息
    # return {"url": "http://dev4.neikongyi.com/nky", "user": "admin1", "password": "nky2018"}
    # book = xlrd.open_workbook(r"F:\workspace\内控易运维\内控易登录信息.xls")
    book = xlrd.open_workbook(r"内控易登录信息.xls")
    sheet = book.sheet_by_index(0)
    _nky_data = []
    for row in range(row1, row2):
        row -= 1
        _dict = {'org_name': str(sheet.cell(row, 1))[6:-1],
                 'service': str(sheet.cell(row, 2))[6:-1] + ".neikongyi.com",
                 'user': str(sheet.cell(row, 3))[6:-1],
                 'userid': str(sheet.cell(row, 5))[7:-2],
                 'round': str(sheet.cell(row, 6))[7:-2],
                 'password': str(sheet.cell(row, 4))[6:-1]
                 }
        _nky_data.append(_dict)
    return _nky_data


def read_rows():
    book = xlrd.open_workbook(r"内控易登录信息.xls")
    sheet = book.sheet_by_index(0)
    return int(sheet.nrows)


class Log:

    def __init__(self, log_name, log_path=os.path.dirname(os.path.abspath(__file__))):

        # 文件的命名
        self.log_path = log_path
        # self.logName = os.path.join(self.log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logName = os.path.join(self.log_path, log_name)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logName, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


def send_report(org_name, log_msg):
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    from_addr = '1280490756@qq.com'  # 自己的邮箱账号
    password = 'kxroqaghttkjffgf'  # 该QQ形成的动态密码，如更换QQ，则要开启smtp服务，复制服动态码
    to_addr = ['1334819965@qq.com', 'wangxiong@neikongyi.com']  # 接收人的邮箱账号
    smtp_server = 'smtp.qq.com'
    msg = MIMEMultipart()
    msg['From'] = _format_addr('王雄<%s>' % from_addr)  # 发件人
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)

    msg['Subject'] = Header('自动化运行内控易情况-' + org_name, 'utf-8').encode()  # 标题
    msg.attach(MIMEText(log_msg))
    # 此处为测试报告的存放路径，如要运行代码，则要修改为当前path的文件
    # att1 = MIMEText(open(r'E:\eclipse\work\neikongyi\report\TestReport.html', 'rb').read(), 'base64', 'utf-8')
    # att1["Content-Type"] = 'application/octet-stream'
    # att1["Content-Disposition"] = 'attachment; filename="TestReport' + time.strftime(
    #     "%Y-%m-%d") + '.html"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    # msg.attach(att1)
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()


class API_test():
    # servuce 举例
    """
     [
    {"service": "demo4.neikongyi.com", "round": "14936","user":"admin1","userid":"1"
     "password": "nga+eNSuUrhHx/K9W1C/a/qtWqsV30AHQjjm0tWToik=,1ihNzkC+zh+TKlMqP4Jz2jjyq6xf35sX,otJ+EuH/6L3TW51gTEKaLULuik2L+KbvrunnwS/G0P1VMKGG9F6JvGfWHn+NinGF3cFdVhnnDDAjDDBJbeBvhBvVcmRp03iAP7eSpZh1Zz4="},
]
    """
    log = Log('%s.log' % time.strftime('%Y_%m_%d'))
    log_error = Log('log_error_%s.log' % time.strftime('%Y_%m_%d'))

    def __init__(self, useService, h='http'):
        self.csfs = h + "://"
        self.ip = useService['service']
        self.cookie = self.need_Verify_Code()
        self.user = useService['user']
        self.password = useService['password']
        self.round = useService["round"]
        self.userId = useService["userid"]
        self.org_name = useService['org_name']
        self.headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,ko;q=0.8,ja;q=0.7,eo;q=0.6,da;q=0.5,en;q=0.4",
            "Connection": "keep-alive",
            # 'content-length': "240",
            'content-type': "application/json; charset=utf-8",
            'Cookie': self.cookie,
            "Host": self.ip,
            'origin': self.csfs + self.ip,
            "Referer": self.csfs + self.ip + "/nky",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/98.0.4758.102 Safari/537.36",
            "x-Current-User-Id": self.userId,
            "x-Current-Org-Id": '200',
            "referrerPolicy": "strict-origin-when-cross-origin"
        }

    def __del__(self):
        requests.session().close()

    def need_Verify_Code(self):  # 获取cookie
        url = self.csfs + self.ip + "/nky/service/session/needVerifyCode"
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Host": self.ip,
            "Referer": self.csfs + self.ip + "/nky",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        }
        _params = {'orgnizationId': 200}
        response = requests.request("GET", url, params=_params, headers=headers)
        header = eval(str(response.headers))  # 将请求后的字符类型先简单转成str，再换成dict
        # print(header)
        set_cookie = header['Set-Cookie']
        # print(set_cookie)
        if "acw_tc" in set_cookie:
            acw_tc = "acw_tc=" + re.findall(r"acw_tc=(.+?);", set_cookie)[0]
            JSESSIONID = "JSESSIONID=" + re.findall(r"JSESSIONID=(.+?);", set_cookie)[0]
            cookie = JSESSIONID + ";" + acw_tc
            # print(cookie)
        else:
            cookie = set_cookie[0:43]
        # self.log.info("cookie：" + str(cookie))
        return cookie

    def login(self):
        url = self.csfs + self.ip + "/nky/service/session/login"
        _payload = {
            'orgnizationId': '200',
            "userName": self.user,
            "password": self.password,
            "round": self.round,

        }
        _headers = self.headers
        # print(_headers)
        del _headers['x-Current-User-Id']
        _response = requests.request("POST", url, data=json.dumps(_payload), headers=_headers).text
        # print(_response)
        # _response_text=str(_response.text)
        if 'data' in str(_response):
            self.log.info('登录成功')
            return '登录成功'
            # return self.headers
        elif 'errors' in str(_response):
            msg = "登录失败,错误信息" + str(_response)
            if "-2" in str(_response):
                msg += "密码错误"
            elif "-1" in str(_response):
                msg += "用户不存在"
            else:
                pass
            self.log.info(msg)
            self.log_error.info(msg)
            return msg
        else:
            msg = "登录失败,错误信息" + str(_response)
            self.log.info(msg)
            self.log_error.info(msg)
            return msg

    def graphql_ri(self):
        # 返回已通过的报销单ID，用于打印
        _url = self.csfs + self.ip + "/nky/service/graphql"
        _payload = "{\"query\":\"{\\n  list: Reimburse(criteriaStr: \\\"(statusId =4 )\\\", sorts: [{name: " \
                   "\\\"createdTime\\\", isAsc: false}], firstResult: 0, maxResult: 10) {\\n    id\\n  }\\n}\\n\"," \
                   "\"variables\":null,\"operationName\":null} "

        _headers = self.headers
        # print(_headers)
        # self.log.info(_url)
        # self.log.info(_headers)
        _response = requests.request("POST", _url, data=_payload, headers=_headers)
        # print(_response)
        if "200" in str(_response):
            self.log.info("查询成功:已通过的报销单信息-" + str(_response))
            _response = json.loads(_response.text)
            # print(_response)
            # 返回可以打印的报销单
            if _response["data"]["list"]:
                return _response["data"]["list"][0]['id']
            else:
                msg = self.org_name + "报销单查询成功，但数据为空" + str(_response)
                self.log_error.info(msg)
                return msg
        else:
            msg = self.org_name + "查询失败：" + str(_response) + "\n" + "url:" + _url + "\n" + "headers:" + str(
                _headers) + "\n" + "payload:" + str(_payload)
            self.log.info("查询失败：" + str(_response))
            self.log_error.info(msg)

    def graphql_tem(self):
        # 返回报销单的打印模板ID，用于打印
        _url = self.csfs + self.ip + "/nky/service/graphql"
        _payload = "{\"query\":\"{\\n  list:BillTemplate(criteriaStr: \\\"billTypeId=32\\\") {\\n    id\\n    ext\\n  " \
                   "}\\n}\\n\",\"variables\":null,\"operationName\":null} "

        _headers = self.headers
        # self.log.info(_url)
        # self.log.info(_headers)
        _response = requests.request("POST", _url, data=_payload, headers=_headers)
        # print(_response)
        if "200" in str(_response):
            self.log.info("查询成功:报销单的打印信息为-" + str(_response))
            _response = json.loads(_response.text)
            # 返回可以打印的打印模板

            if _response["data"]["list"]:
                tem_id = _response["data"]["list"][0]['id']
                return tem_id
            else:
                self.log_error.info(self.org_name + "查询成功，但数据为空" + str(_response))
                return self.org_name, "查询成功，但数据为空" + _response
            # tem_ext = _response["data"]["list"][0]['ext']
        else:
            msg = self.org_name + "查询失败：" + str(_response) + "\n" + "url:" + _url + "\n" + "headers:" + str(
                _headers) + "\n" + "payload:" + str(_payload)
            self.log.info(msg)
            self.log_error.info(msg)

    def print_ri(self, ri, tem_id, ext='odt'):
        # 打印报销单
        _url = self.csfs + self.ip + "/nky/service/file/print?billType=Reimburse&billId=" + str(
            ri) + "&templateId=" + str(tem_id) + "&ext=" + str(ext) + "&isMobile=false&years="
        self.log.info("开始打印：" + _url)
        # self.log.info(_url)
        _response = requests.request("GET", _url, headers=self.headers)
        # print(_response)
        if "200" in str(_response):
            self.log.info("打印接口成功，返回信息为：" + str(_response.text))
            return "打印接口成功，返回信息为：" + str(_response.text)
        else:
            msg = "打印接口失败，错误信息为：" + str(_response.text) + "\n" + "url:" + _url + "\n" + "headers:" + str(
                self.headers) + "\n"
            self.log.info(msg)
            self.log_error.info(msg)
            return msg

    def process_list(self):
        _url = self.csfs + self.ip + "/nky/service/workflow/process-list"
        self.log.info(_url)
        _response = requests.request("GET", _url, headers=self.headers)
        # print(_response)
        if "200" in str(_response):
            msg = "流程接口service/ workflow/process-list接口成功，返回信息为：" + str(_response)
            self.log.info(msg)
            return msg
        else:
            msg = "process-list接口失败，错误信息为：" + str(_response)
            self.log.info("process-list接口失败，错误信息为：" + str(_response))
            self.log_error.info(msg)
            return msg


def choose_address(flag='0'):
    if flag == '1':
        address = input("请输入执行地区，按enter结束，0全部，1北京，2四川,3单条执行：")
    else:
        address = '0'
    if address == '0':
        nky_data = read_data(2, read_rows())
    elif address == '1':
        nky_data = read_data(2, 138)
    elif address == '2':
        nky_data = read_data(145, 157)
    elif address == '3':
        a = input("单条执行，请输入Excel行数:")
        if int(a):
            nky_data = read_data(int(a), int(a) + 1)
        else:
            return choose_address()
    else:
        return choose_address()
    return nky_data


def run(key=None):
    # 主程序
    if key is None:
        nky_data = choose_address()
    else:
        nky_data = choose_address(key)
    for nky in nky_data:
        # print(nky)
        ap = API_test(nky, h='https')
        ap.log.info("=====开始执行：" + str(nky['org_name']))
        result = ap.login()
        if '成功' in result:
            ap.log.info("开始查询流程接口：service/workflow/process-list")
            try:
                result1 = ap.process_list()
            except TimeoutError:
                result1 = ap.process_list()
            if "成功" in result1:
                # ap.log.info("开始查询报销单")
                ri = ap.graphql_ri()
                if "为空" not in str(ri):
                    # ap.log.info("开始查询打印模板")
                    tem = ap.graphql_tem()
                    # ap.log.info("开始打印")
                    result2 = ap.print_ri(ri, tem)
                    if "成功" in result2:
                        pass
                    else:
                        send_report(nky['org_name'], result2)
                else:
                    ap.log.info(nky['org_name'] + "无报销单数据，跳过打印程序")
            else:
                send_report(nky['org_name'], result1)
        else:
            send_report(nky['org_name'], result)


def test():
    # 测试程序
    s = {"service": "dev4.neikongyi.com", "round": "14395", "user": "admin1", "userid": "1", "org_name": "dev4单位",
         "password": "+8u7Q/+6mCF3di3K+wAgtahy9VbVBTRY+SR8qdJ/tAw=,x6zkI8f2r1uWJ37mARoRPwtu7GlAzpIh,cGcmESPxL4oEaOJsqI02pP4dqwpkkjlUfEl4rPCCByT/lJUHutYzp9bnXvyzirqB5GcmEntZIDWBxqjhM5sRl6VFTJ4BJMA6oHxKTjt62eY="}
    s1 = {"service": "sunny.neikongyi.com", "round": "17161", "user": "admin1", "userid": "1", "org_name": "sunny单位",
          "password": "dkz4zOq4vc3SQT29wZiRhcMEzpRXco3i2QTaZMLeMF8=,y33ErjKVbuhXdNbXe6FU0e1YFmkJeidX,vjtmlK8yqdku4RtZrKWKzK3a2Qscku4Srhax9fWNhYyL7BibvaC1Pr9jfvoftkdP5Jt6l1ZYQxo/o0VLuwgNOQaVtogQauMQuEia8DOd8WM="
          }
    ap = API_test(s)
    ap.log.info("=====开始执行：" + str(s['org_name']))
    ap.login()
    ap.log.info("开始查询流程接口：service/workflow/process-list")
    ap.process_list()
    ap.log.info("开始查询报销单")
    ri = ap.graphql_ri()
    ap.log.info("开始查询打印模板")
    tem = ap.graphql_tem()
    ap.log.info("开始打印")
    ap.print_ri(ri, tem)


if __name__ == "__main__":
    # run('1')
    run()