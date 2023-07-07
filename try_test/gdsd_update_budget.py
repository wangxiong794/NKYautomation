# 广东水电院更新预算指标
import time

import requests
import json
from service.logger import Log

service = [
    {"agreement": "https://", "service": "nky.gdsdxy.edu.cn", "round": "14630", "orgnizationId": "200", "userId": "1",
     "user": "admin11",
     "password": "cLWmP6yjKVay1II9Aq9FILo51VbzrWtlTcGuyATxzz0=,dTnrvSzdkc8sr24Eg3lespOF8oDE6hQh,yfh2WpQI6cabH/a2SlrkXJlekHLZW9+cIOhMVAmCyUF9C88a6pdv7+dpvgcG4i4J1l9qO4QWPI/ahUwp/gRFCSodYrd2Xp+Z1blUI2OWpxY="}
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
        # 查询校内项目待审信息，bll_id为预算项ID
        _url = self.agreement + self.ip + "/nky/service/graphql"
        _payload = {
            "query": '{BudgetItem(criteriaStr:\"id=' + str(
                bill_id) + '\"){\n  authScopeId\n  baProjectId\n  baProjectName\n  bankAccountId\n  bcTypeId\n  businessTypeId\n  code\n  description\n  financialAccountId\n  fiscalYearId\n  functionalAccountId\n  governmentAccountId\n  hsProjectCode\n  id\n  name\n  projectId\n  quotaNumber\n  schoolYearId\n}}'
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
        _data = json.loads(_response.text)["data"]['BudgetItem']
        if len(_data) == 0:
            print('无对应记录')
            return None
        else:
            _data = _data[0]
            _data['toNullFields'] = ["businessTypeId", "financialAccountId", "governmentAccountId",
                                     "functionalAccountId"]
            _data['yearId'] = 10005
            print(_data)
            return bill_id, _data

    def update_budget_item(self,bill_id,_data):
        _url = self.agreement + self.ip + "/nky/service/BudgetItem/"+str(bill_id)
        _headers = self.headers
        _headers['sec-ch-ua'] = '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"'
        _headers['sec-ch-ua-mobile'] = '70'
        _headers['sec-ch-ua-platform'] = "macOS"
        _headers['Sec-Fetch-Dest'] = 'empty'
        _headers['Sec-Fetch-Mode'] = "cors"
        _headers['Sec-Fetch-Site'] = 'same-origin'
        _headers['X-Content-Type-Options'] = 'nosniff'
        _response = requests.request("PUT", _url, data=json.dumps(_data), headers=_headers)
        print(str(_response), _response.text)


if __name__ == "__main__":
    a = workSpace()
    a.login()
    for i in (
            2103,
            2104
    ):
        _data=a.gql_log(i)
        a.update_budget_item(_data[0],_data[1])
        time.sleep(1)