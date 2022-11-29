# coding=utf-8
# 内控易是打包部署后，检查redis服务、打印服务是否成功，操作为登录后，查询单据，打印单据
import json
import logging
import os

import time
import requests

from service.logger import Log

log = Log()
service = [
    {"service": "dev4.neikongyi.com", "round": "14209", "hm": "http://", "user": "admin1", "id": "1",
     "orgnizationId": "200", "password_mw": "nky2018",
     "password": "KbXAinQyUIwJvGMm7OyB5KynVVmuYsHUux28EAEaYyQ=,23epiu+6cOAkmySj+wJrCof8V2FdOKGd,mCWVBTnlh1/UNorp80swybuGsu4XHyAIxrwTBIq9Uz8gqBBrhn8bUJ3esFoJ09c1Xns0NZx7kbpELhmy3+LnJCcKIHOZns2YsJTKFHtWvkU="
     }
]


class workSpace():
    def __init__(self):

        useService = service[0]
        self.http = useService["hm"]
        self.ip = useService['service']
        self.cookie = self.need_Verify_Code()
        self.user = useService["user"]
        self.password = useService['password']
        self.password_mw = useService['password_mw']
        self.round = useService["round"]
        self.userId = useService["id"]
        self.org = useService["orgnizationId"]
        self.headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            # 'content-length': "240",
            'content-type': "application/json; charset=utf-8",
            'Cookie': self.cookie,
            "Host": self.ip,
            'origin': self.http + self.ip,
            "Referer": self.http + self.ip + "/nky",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.122 Safari/537.36",
            "x-Current-User-Id": self.userId,
        }

    def need_Verify_Code(self):  # 获取cookie
        url = self.http + self.ip + "/nky/service/session/needVerifyCode"
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
        url = self.http + self.ip + "/nky/service/session/login"
        _payload = {
            'orgnizationId': self.org,
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

    def wx_login(self):
        url = self.http + self.ip + "/nky/service/session/wxbind"
        _payload = {
            'presetorgid': self.org,
            "userName": self.user,
            "password": self.password_mw,
            # "round": self.round,

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

    def gql_return_bill(self):
        _payload = "{\"query\":\"{\\n  list: BudgetApplication(criteriaStr: \\\"((statusId=4 and (statusId = 4 and amount > 0 and exists(select available from BillStock where billId = m.id and stockTypeId = 900 and billType = 'BudgetApplication' and frozen + outStock > 0 and frozen + outStock < m.amount ))) and (fiscalYearId = 10000))\\\") {\\n    id\\n  }\\n}\\n\",\"variables\":null,\"operationName\":null}"
        _url = self.http + self.ip + "/nky/service/graphql"
        _headers = self.headers
        # print(_url)
        _response = requests.request("POST", _url, data=_payload, headers=_headers)
        # print(_response.text)
        _data = json.loads(_response.text)["data"]['list']
        ids = []
        for _id in _data:
            #     # print(a)
            ids.append(_id['id'])
        # print(_data)
        print(ids)
        return ids

    def gql_return_amount(self, bill_id):
        _payload = "{\"query\":\"{\\n\\tBillItemStock(criteriaStr:\\\"billId=%s\\\"){\\n    billItemId\\n    billItemType\\n    frozen\\n    outStock\\n    available\\n  }\\n  BudgetApplicationItem(criteriaStr:\\\"parentId=%s\\\"){\\n    id\\n    budgetItemId\\n  }\\n}\\n\",\"variables\":null,\"operationName\":null}" % (
            str(bill_id), str(bill_id))
        _url = self.http + self.ip + "/nky/service/graphql"
        _headers = self.headers
        # print(_url)
        _response = requests.request("POST", _url, data=_payload, headers=_headers)
        _data = json.loads(_response.text)["data"]['BillItemStock']
        _budget_data = json.loads(_response.text)["data"]['BudgetApplicationItem']
        _budget_dict = {}
        for _budget in _budget_data:
            _budget_dict.update({_budget["id"]: _budget["budgetItemId"]})
        # print(_budget_dict)
        budgetApplicationItems = []
        _amount = 0
        _originalAmount_0 = 0
        for _items in _data:
            # print(_budget_dict[_items["billItemId"]])
            _originalAmount_0 = _originalAmount_0 + round(float(_items["frozen"]) + float(_items["outStock"]) +
                                                        float(_items["available"]),2)
            _amount = _amount + round(float(_items["frozen"]), 2) + round(float(_items["outStock"]), 2)
            _dict = {"billItemId": _budget_dict[_items["billItemId"]],
                     "amount": _amount,
                     "originalAmount": _originalAmount,
                     "id": _items["billItemId"]}
            # print(_dict)

            budgetApplicationItems.append(_dict)
        print(_response.text)
        # print(budgetApplicationItems)
        # print(_amount, _originalAmount)
        _data_dict = {
            "amount": _amount,
            "budgetApplicationItems": budgetApplicationItems,
            "id": bill_id,
            "isReleased": "true",
            "orgnizationId": self.org,
            "originalAmount": _originalAmount_0,
            "statusId": 4
        }
        # print(_data_dict)
        return _data_dict

    def return_amount(self, bill_id, _payload_1):
        _url = self.http + self.ip + "/nky/service/BudgetApplication/" + str(bill_id)
        _response = requests.request("PUT", _url, data=json.dumps(_payload_1), headers=self.headers)
        log.info(str(bill_id) + str(_payload_1))
        if '200' in str(_response):
            log.info("%s已退回" % bill_id)
        else:
            log.info("%s退还失败，错误码%s" % (bill_id, str(_response)))

    def __del__(self):
        requests.session().close()


if __name__ == "__main__":
    # run('1')
    a = workSpace()
    # a.login()
    a.wx_login()
    # _data = a.gql_return_amount(10342)
    # a.return_amount(10342,_data)
    bills = a.gql_return_bill()
    # print(bills)
    for bill in bills:
        _data = a.gql_return_amount(bill)
        # print(_data)
        a.return_amount(bill, _data)
        # time.sleep(1)
    a.__del__()
