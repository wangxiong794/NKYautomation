# coding=utf-8
import requests
import json
import time
from service.logger import Log
log=Log()
service = [
    {"service": "demo4.neikongyi.com", "round": "14936",
     "password": "nga+eNSuUrhHx/K9W1C/a/qtWqsV30AHQjjm0tWToik=,1ihNzkC+zh+TKlMqP4Jz2jjyq6xf35sX,otJ+EuH/6L3TW51gTEKaLULuik2L+KbvrunnwS/G0P1VMKGG9F6JvGfWHn+NinGF3cFdVhnnDDAjDDBJbeBvhBvVcmRp03iAP7eSpZh1Zz4="},
    {"service": "39.107.221.188", "round": "14604",
     "password": "mYy8+QClL3k7B0tw7hxatyKuki1JJ7pyE++6JQKu+yw=,YeWqwTvWP32OHuttwv+j+NLT3vQrQ6tT,uXjqZj8MFez3rBlFL7xptS++0+MljjyVjBGd/VnNHBpstxmVgpvJoYcT9B5Jr9sOQktSrnMAgBG8IRRG0x51HYda/zeNBz4qQeqQA8lj6lw="}
]

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


if __name__=='__main__':
    a=workSpace()
    a.login()
