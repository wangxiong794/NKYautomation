import json
import logging
import os
import time

import requests

root_dir = os.path.dirname(os.path.abspath(__file__))
service = [{
    "service": "jxt.neikongyi.com", "round": "14295", "userName": "cwk", "userId": "10068",
    "password": "mtzcFcMFUY5VHIvXjNiNPtwBXXEYpUr1XJZ3pzIbLkA=,zDGiNW5jJKhNaQ3ZSw2ZmSVTaKqxW/FT,0cV9KMZ5mrD5FllcNIbuiNmRPuJPsgTR5E8SA3RnwMuQEJXlZxDw/vMkYVh2eiju/MfFBweYqg0orGbe+6i9wCDDlp2IUk3Bct9iCxoNYak="
}, {
    "service": "58.118.2.90", "round": "14371", "userName": "cwk", "userId": "10068",
    "password": "liFtCwsitGDMCI+3w1HAhY9BXqfzGj1H4UfIi9T8rmY=,1h94/xCbHm71s75eLCM5uOCwALy14gA9,n8C9w5uViqshmDm5thU0HYOj0PIBGcUxpXYpVi+/GtfeWU8vxK4Z2ebz4jt2WyOq8pdiiBJIcgyImaBupcX605xw3WcQg8vpd5VuoRh2aVA="
}
]


class workSpace():
    def __init__(self):

        useService = service[1]
        self.ip = useService['service']
        self.cookie = self.need_Verify_Code()
        self.user = useService['userName']
        self.password = useService['password']
        self.round = useService["round"]
        self.userId = useService["userId"]
        self.headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            'content-length': "240",
            'content-type': "application/json",
            'Cookie': self.cookie,
            "Host": self.ip,
            'origin': "http://" + self.ip,
            "Referer": "http://" + self.ip + "/nky",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.122 Safari/537.36",
            "x-Current-User-Id": self.userId
        }

    def need_Verify_Code(self):  # 获取cookie
        url = "http://" + self.ip + "/bureau/service/session/needVerifyCode"
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Host": self.ip,
            "Referer": "http://" + self.ip + "/bureau",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        }
        _params = {'orgnizationId': 200}
        response = requests.request("GET", url, params=_params, headers=headers)
        header = eval(str(response.headers))  # 将请求后的字符类型先简单转成str，再换成dict
        set_cookie = header['Set-Cookie']
        cookie = set_cookie[0:43]
        print("cookie：" + str(cookie))
        return cookie

    def login(self):
        url = "http://" + self.ip + "/bureau/service/session/login"
        _payload = {
            "userName": self.user,
            "password": self.password,
            "round": self.round,

        }
        _headers = self.headers
        # del _headers['x-Current-User-Id']
        _response = requests.request("POST", url, data=json.dumps(_payload), headers=_headers)
        if '200' in str(_response):
            print("登录成功")
            return self.headers
        else:
            print("登录失败,错误码" + str(_response))
            return "登录失败，错误码" + str(_response)

    def gql_cwk_501(self):
        _payload = "{\"query\":\"{\\n  ApprovalLog(criteriaStr: \\\"createdTime>'2022-10-24 08:47:05' and approvalUserId=10068 and approvalStatusId=501 and activityId='officeApproval'\\\") {\\n    id\\n    createdTime\\n  }\\n}\\n\",\"variables\":null,\"operationName\":null}"
        # 返回报销单的打印模板ID，用于打印
        _url = "http://" + self.ip + "/bureau/service/graphql"
        _headers = self.headers
        # print(_url)
        _response = requests.request("POST", _url, data=_payload, headers=_headers)
        # print(_response.text.encode('utf8'))
        _data = json.loads(_response.text)["data"]['ApprovalLog']
        ids = []
        for a in _data:
            # print(a)
            ids.append(a['id'])

        # print(_data)
        # print(ids)
        return ids

    def auto_agree(self, app_id):
        _url = "http://" + self.ip + "/bureau/service/ApprovalLog/%s" % app_id
        _payload = {
            'approTempProperties': "{\"items\":[]}",
            'approvalDate': "2022-11-20T05:45:34.252Z",
            'approvalStatusId': '502',
            'description': "同意",
            'id': app_id
        }
        _response = requests.request("PUT", _url, data=json.dumps(_payload), headers=self.headers)
        print(str(_response), app_id)

    def __del__(self):
        requests.session().close()


if __name__ == "__main__":
    while True:

        a = workSpace()
        a.login()
        ids = a.gql_cwk_501()
        for i in ids:
            a.auto_agree(i)
            time.sleep(0.5)
        a.__del__()
        print(time.strftime('%m-%d-%H:%M:%S'))
        time.sleep(600)

