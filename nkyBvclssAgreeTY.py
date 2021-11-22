# coding=utf-8
# 内控易劳保学院，流程上不需要田院审批
from service.logger import Log
import pymysql
import requests
import json
import time

service = [
    {"service": "demo4.neikongyi.com", "round": "14936",
     "password": "nga+eNSuUrhHx/K9W1C/a/qtWqsV30AHQjjm0tWToik=,1ihNzkC+zh+TKlMqP4Jz2jjyq6xf35sX,otJ+EuH/6L3TW51gTEKaLULuik2L+KbvrunnwS/G0P1VMKGG9F6JvGfWHn+NinGF3cFdVhnnDDAjDDBJbeBvhBvVcmRp03iAP7eSpZh1Zz4="},
    {"service": "39.107.221.188", "round": "14604",
     "password": "mYy8+QClL3k7B0tw7hxatyKuki1JJ7pyE++6JQKu+yw=,YeWqwTvWP32OHuttwv+j+NLT3vQrQ6tT,uXjqZj8MFez3rBlFL7xptS++0+MljjyVjBGd/VnNHBpstxmVgpvJoYcT9B5Jr9sOQktSrnMAgBG8IRRG0x51HYda/zeNBz4qQeqQA8lj6lw="}
]
log = Log()


class workSpace():
    def __init__(self):
        self.user = "admin1"
        useService = service[1]
        self.ip = useService['service']
        self.cookie = self.need_Verify_Code()
        self.password = useService['password']
        self.round = useService["round"]
        self.userId = '1'
        self.headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            # 'content-length': "240",
            'content-type': "application/json; charset=utf-8",
            'Cookie': self.cookie,
            "Host": self.ip,
            'origin': "http://" + self.ip,
            "Referer": "http://" + self.ip + "/nky",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.122 Safari/537.36",
            "x-Current-User-Id": self.userId,
        }

    def need_Verify_Code(self):  # 获取cookie
        url = "http://" + self.ip + "/nky/service/session/needVerifyCode"
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Host": self.ip,
            "Referer": "http://" + self.ip + "/nky",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        }
        _params = {'orgnizationId': 200}
        response = requests.request("GET", url, params=_params, headers=headers)
        header = eval(str(response.headers))  # 将请求后的字符类型先简单转成str，再换成dict
        set_cookie = header['Set-Cookie']
        cookie = set_cookie[0:43]
        log.info("cookie：" + str(cookie))
        return cookie

    def login(self):
        url = "http://" + self.ip + "/nky/service/session/login"
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

    def standard_approve_log(self, log_id):
        _url = "http://" + self.ip + "/nky/service/ApprovalLog/" + str(log_id)
        _payload = {
            'approvalDate': "2021-11-15T02:06:02.998Z",
            'approvalStatusId': 502,
            'description': "系统代为审批",
            'id': log_id,
            'additionalValues': {}
        }
        _header = self.headers
        response = requests.request("PUT", _url, data=json.dumps(_payload), headers=_header)
        if '200' in str(response):
            return response.text
        else:
            return "审批失败，审批节点为" + str(log_id)


class DB(object):
    def __init__(self, host=service[1]['service'], port=3306, db='nky', user='nky2018', passwd='Neikongyi201*',
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


def sql_project():
    # 查询待审项目
    with DB() as db_1:
        sql_1 = "SELECT * FROM approval_log WHERE approval_status_id=501 AND approval_user_id=10001 AND " \
                "orgnization_id=200 AND bill_type='pmSpecialProject'; "
        db_1.execute(sql_1)
        return list(db_1)


def main():
    while True:
        _number = 0
        a = workSpace()
        time.sleep(1)
        l = a.login()
        project_list = sql_project()
        if '错误码' in l:
            log.info("正在重试")
            requests.session().close()
            continue
        elif len(project_list) == 0:
            requests.session().close()
            break
        elif _number == 100:
            requests.session().close()
            break
        else:
            if len(project_list) != 0:
                for i in project_list:
                    project_id = i['bill_id']
                    log_id = i['id']
                    print(project_id, log_id)
                    a.standard_approve_log(log_id)
                    log.info("项目%s已代为田院审批，审批日志为%s" % (project_id, log_id))
            else:
                log.info("暂无需要田院审批的项目")
                requests.session().close()
                break
        requests.session().close()


if __name__ == '__main__':
    main()
