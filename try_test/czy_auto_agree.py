# 成职院自动审批
import requests
import json
from service.logger import Log
import re

service = [
    {"agreement": "http://", "service": "10.4.10.10", "round": "14780", "orgnizationId": "200", "userId": "1",
     "user": "admin1",
     "password": "IfhFnoyc7jF2qGFCU4JD7vVpx/2SXGPP+YQ+4Ox/6xU=,bMGJVjKt8Cl2RV68OCs1PeoOr698OqAU,7TumTUlYr0cCQRCJ2s0J3L1wBLfGdm5For/uLihDycAnjfaEiQeehzzAekycmdNZ5p2PV1zET9vwfOsHsOtz4uL0QRWPZ5MFEgh+5dg9uhE="}
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
        print(header)
        set_cookie = header['Set-Cookie']
        # a2=re.search(r'JSESSIONID=(.);Path',set_cookie,re.M|re.I)
        cookie1 = set_cookie[0:69]
        cookie2 = set_cookie[100:143]
        cookie = cookie1 + ";" + cookie2
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

    def gql_log(self, bill_id):
        # 查询校内项目待审信息
        _url = self.agreement + self.ip + "/nky/service/graphql"
        _payload = {
            "query": '{\n  ApprovalLog(criteriaStr:\"billId=' + str(
                bill_id) + ' and approvalStatusId=501\"){\n    id\n    activityId\n  }\n}'
        }
        _headers = self.headers
        _headers['sec-ch-ua'] = '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"'
        _headers['sec-ch-ua-mobile'] = '70'
        _headers['sec-ch-ua-platform'] = "macOS"
        _headers['Sec-Fetch-Dest'] = 'empty'
        _headers['Sec-Fetch-Mode'] = "cors"
        _headers['Sec-Fetch-Site'] = 'same-origin'
        _headers['X-Content-Type-Options'] = 'nosniff'
        _response = requests.request("POST", _url, data=json.dumps(_payload), headers=_headers)
        print(_response.text)
        _data = json.loads(_response.text)["data"]['ApprovalLog'][0]
        if str(_data['activityId']) in (
                'workgroupSorting', 'pmPfys1','pmPfys2', 'totalWorkgroupSorting','oneDownUpdate'):
            print('无待审记录')
            return None
        else:
            _data['additionalValues'] = {}
            _data['approvalDate'] = '2023-06-07T08:02:11.153Z'
            _data['approvalStatusId'] = '502'
            _data['description'] = '同意。'
            del _data['activityId']
            a_id = str(_data['id'])
            print(_data)
            return a_id, _data

    def auto_agree(self, a_id, pay_load):
        # 管理员代为同意
        _url = self.agreement + self.ip + "/nky/service/ApprovalLog/" + a_id
        _headers = self.headers
        _headers['sec-ch-ua'] = '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"'
        _headers['sec-ch-ua-mobile'] = '70'
        _headers['sec-ch-ua-platform'] = "macOS"
        _headers['Sec-Fetch-Dest'] = 'empty'
        _headers['Sec-Fetch-Mode'] = "cors"
        _headers['Sec-Fetch-Site'] = 'same-origin'
        _headers['X-Content-Type-Options'] = 'nosniff'
        _response = requests.request("PUT", _url, data=json.dumps(pay_load), headers=_headers)
        print(str(_response), _response.text)


if __name__ == "__main__":
    a = workSpace()
    a.login()
    for i in (

            82,
            81,
            80,
            59,
            57,
            56,
            55,
            48,
            45,
            42,
            41,
            40
              ):
        while 1:
            _data = a.gql_log(i)
            if _data is None:
                break
            a.auto_agree(_data[0], _data[1])
