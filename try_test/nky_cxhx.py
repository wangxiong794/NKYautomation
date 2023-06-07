# 内控易取消核销再核销
import requests
import json
from service.logger import Log
import re

service = [
    {"agreement": "https://", "service": "yykxc.neikongyi.com", "round": "15271", "orgnizationId": "200", "userId": "1",
     "user": "admin1",
     "password": "F2aZypE9nCpCWKgKM033szPxKLmFDx3u3QoLhQaplFo=,zXr4rXUlJyj8dOmT5RlH0LGy+PW1k9l3,yDZqqcj2x+knsnyndUtJksJTEI/qPpPZS8IwwXonZq593doueGrPRvTgWtDdxKaE8UWXrEgPkCHaisymCKASf9BvUdnsUcBBTDGU1yWRjzE="},

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

    def open_ba(self, bill_id):
        # 激活事前申请单
        _url = self.agreement + self.ip + "/nky/service/BudgetApplication/" + str(bill_id)
        _payload = {
            "statusId": 4,
            "id": bill_id,
            "orgnizationId": 200
        }
        _headers = self.headers
        _headers['sec-ch-ua'] = '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"'
        _headers['sec-ch-ua-mobile'] = '70'
        _headers['sec-ch-ua-platform'] = "macOS"
        _headers['Sec-Fetch-Dest'] = 'empty'
        _headers['Sec-Fetch-Mode'] = "cors"
        _headers['Sec-Fetch-Site'] = 'same-origin'
        _headers['X-Content-Type-Options'] = 'nosniff'
        _response = requests.request("PUT", _url, data=json.dumps(_payload), headers=_headers)
        # print(_headers)

        print(str(_response), _response)

    def gql_ri(self, bill_id):
        # 查询报销单核销信息
        _url = self.agreement + self.ip + "/nky/service/graphql"
        _payload = {
            "query": '{\n  Reimburse(criteriaStr:\"id=' + str(
                bill_id) + '\"){\n    id\n    reimburseItems{\n      id\n    }\n  }\n}'
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
        # print(_headers)
        _data = json.loads(_response.text)["data"]['Reimburse'][0]
        re_items = _data['reimburseItems']
        for re_item in re_items:
            re_item['actual'] = 0
            re_item['editFlag'] = 'update'
            re_item['quotaNumber'] = ""
        _data['actual'] = 0
        _data['isVerified'] = 'false'
        _data['orgnizationId'] = 200
        print(_data)
        return _data

    def hx(self, bill_id, pay_load):
        # 取消核销
        _url = self.agreement + self.ip + "/nky/service/Reimburse/" + str(bill_id)
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
    for i in (7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              76,
              77,
              78,
              80,
              84,
              85,
              86,
              87,
              88,
              91,
              92,
              93,
              94,
              96,
              98,
              99,
              100,
              103,
              104,
              106,
              107,
              108,
              109,
              110,
              112,
              113,
              114,
              115,
              117,
              122):
        _data = a.gql_ri(i)
        a.hx(i, _data)
#     for i in (9,
# 10,
# 12,
# 13,
# 14,
# 17,
# 18,
# 19,
# 20,
# 21,
# 24,
# 26,
# 27,
# 28,
# 30,
# 31,
# 32,
# 34,
# 35,
# 37,
# 39,
# 40,
# 41,
# 42,
# 43,
# 44,
# 47,
# 48,
# 49,
# 50,
# 52,
# 53,
# 54,
# 58,
# 59,
# 60,
# 62,
# 69,
# 72,
# 74,
# 80,
# 90):
#         a.open_ba(i)
