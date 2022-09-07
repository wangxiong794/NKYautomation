# 帮助劳职院提交所有的单据走流程
import json

import pymysql
import requests

from service.logger import Log

service = [
    {"agreement": "http://", "service": "demo4.neikongyi.com", "round": "14340", "orgnizationId": "200", "userId": "1",
     "user": "admin1",
     "password": "eSg4h/A3kSy8GCMnVi/uExzVCqo7Uqx3bh89V4MzwQs=,kHhEUoSxQWEgfNh8IQcf+YLNTQOl0ZQ8,kkgCSecJGeK9+LUzCA3Z05lvS5y8DaV3Tky/4celz7Sip2FZbqDFnlo0Z6iqCkz7cOUEBsL/nARCSDEVlM61Be8f4Xn8s/y0ZJGWfJZkemU="},
    {"agreement": "http://", "service": "39.107.221.188", "round": "15127", "orgnizationId": "200", "userId": "1",
     "user": "admin1",
     "password": "y3YqtO2Nn+ol44LeYJ8+MfB8mIVVfUO8hu/RuMu3kSQ=,wlnYAo8mFGtG9QVVhPpNx54YWwvVLYWJ,kJK33NZYAcVxtPX/orGjZMtTCnDLsi63VSCVIPYsPnJhgtVOlrGE/mfeItE2P8c45DLKJmGFocI1LXUeMrEA5ZdWp2REjV2AaiQd7JIVkDw="}

]
log = Log()
useService = service[0]
print(useService['agreement'])


class workSpace():
    def __init__(self):
        self.ip = useService['service']
        self.agreement = useService['agreement']
        self.cookie = self.need_Verify_Code()
        self.user = useService['user']
        self.password = useService['password']
        self.round = useService["round"]
        self.userId = useService['userId']
        self.orgId = useService['orgnizationId']
        self.headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            # 'content-length': "240",
            'content-type': "application/json; charset=utf-8",
            'Cookie': self.cookie,
            "Host": self.ip,
            'origin': self.agreement + self.ip,
            "Referer": self.agreement + self.ip + "/nky",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.122 Safari/537.36",
            "x-Current-User-Id": self.userId,
            "x-Current-Org-Id": self.orgId
        }

    def __exit__(self, exc_type, exc_val, exc_tb):
        requests.session().close()

    def need_Verify_Code(self):  # 获取cookie
        url = self.agreement + self.ip + "/nky/service/session/needVerifyCode"
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Host": self.ip,
            "Referer": self.agreement + self.ip + "/nky",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        }
        _params = {'organizationId': 200}
        response = requests.request("GET", url, params=_params, headers=headers)
        header = eval(str(response.headers))  # 将请求后的字符类型先简单转成str，再换成dict
        set_cookie = header['Set-Cookie']
        cookie = set_cookie[0:43]
        log.info("cookie：" + str(cookie))
        return cookie

    def login(self):
        url = self.agreement + self.ip + "/nky/service/session/login"
        _payload = {
            'orgnizationId': '200',
            "userName": self.user,
            "password": self.password,
            "round": self.round,

        }
        _headers = self.headers
        del _headers['x-Current-User-Id']
        _response = requests.request("POST", url, data=json.dumps(_payload), headers=_headers)
        if '200' in str(_response):
            log.info('登录成功')
            return self.headers
        else:
            log.info("登录失败,错误码" + str(_response))
            return "登录失败，错误码" + str(_response)

    def start_flow(self, billId, flowId):
        _url = self.agreement + self.ip + "/nky/service/billcommon/startFlow"
        _payload = {
            "billFlowDefineId": flowId,
            "billId": billId,
            "billType": "PmSpecialProject"
        }
        _headers = self.headers
        _response = requests.request("POST", _url, data=json.dumps(_payload), headers=_headers)
        # print(str(_response), _response)
        if 'flowId' in str(_response.text):
            log.info(str(billId) + "提交成功")
        else:
            log.info(str(billId) + "提交失败")


class DB(object):
    def __init__(self, host=useService['service'], port=3306, db='nky', user='nky2018', passwd='Neikongyi201*',
                 charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()


def sql_submit_bill():
    # 查询待提交的SQL
    with DB() as db_1:
        sql_1 = "SELECT id,bill_flow_define_id FROM pm_special_project WHERE status_id=1 AND fiscal_year_id=10002;"
        db_1.execute(sql_1)
        return list(db_1)


def test():
    a = workSpace()
    a.login()
    a.start_flow(10421, 19)


def main():
    a = workSpace()
    a.login()
    data = sql_submit_bill()
    if len(data) > 0:
        for i in range(0, 200):
            data = sql_submit_bill()
            if len(data) > 0:
                bill = data[0]
                a.start_flow(bill['id'], bill['bill_flow_define_id'])
            else:
                log.info("无待提交项目")
                break
    else:
        log.info("无待提交项目")

if __name__ == "__main__":
    # main()
    # test()
    main()
