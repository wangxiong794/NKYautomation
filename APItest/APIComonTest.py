# coding=utf-8
import requests
import json
import time
from service.logger import Log

log = Log()
service = [
    {"service": "demo4.neikongyi.com", "round": "14936", "userId": "1",
     "password": "nga+eNSuUrhHx/K9W1C/a/qtWqsV30AHQjjm0tWToik=,1ihNzkC+zh+TKlMqP4Jz2jjyq6xf35sX,otJ+EuH/6L3TW51gTEKaLULuik2L+KbvrunnwS/G0P1VMKGG9F6JvGfWHn+NinGF3cFdVhnnDDAjDDBJbeBvhBvVcmRp03iAP7eSpZh1Zz4="},
    {"service": "39.107.221.188", "round": "14604", "userId": "1",
     "password": "mYy8+QClL3k7B0tw7hxatyKuki1JJ7pyE++6JQKu+yw=,YeWqwTvWP32OHuttwv+j+NLT3vQrQ6tT,uXjqZj8MFez3rBlFL7xptS++0+MljjyVjBGd/VnNHBpstxmVgpvJoYcT9B5Jr9sOQktSrnMAgBG8IRRG0x51HYda/zeNBz4qQeqQA8lj6lw="},
    {"service": "39.106.158.149", "round": "14192", "userId": "10119",
     "password": "qQB1wEzHB2iJUqsjgl/NYiEus039kzzftRT4xIHRo18=,vdgB8wGAWYlb8TBj6OkWb3iTNNL2eCaR,Q45UcDZytuo7CZhsY7nHXTdJpe2YPti/PvVoBjqcfSos1Xq8tYCMCJD9UxDRgH1q0hyP450kwQdK3GvfE8n6ttt+NhReMMEKBhwc7E8dOEc="},
    {
        "service": "39.106.158.149", "round": "14265", "userName": "wxfz10wmyh7q", "orgnizationId": 200,
        "userId": "10152",
        "password": "KNgNaynOMNamTi7xAkeMYJ7OjUKTTEuFQEQIaTxsmCc=,9PO3xflDJY0hCKP8QKn2Rl9m7YKmok3q,"
                    "+SVMcA8lpuo7+Njl3AGZaBvNpWkBZJ4/X1El3IfMge9xIL1Hs8ZGWN+TrT1ZyXR9lBv1rxb50hzXYcIPSsnIDXFzDZpX"
                    "/q7XM6XgQOWzxQQ= "
    },
    {
        "service": "123.60.128.8", "round": "14736", "userId": "1", "userName": "admin1",
        "password": "eKHLqA5cA6JAb47w9b+8rIlGtvnC8PdA7TLhgsooJDo=,RN6ITJz91vYAhBKUsmS4Nvb08qfApJcD,Ed8g7dQTC+M976bxmMlG/VrA5zAsizbphqAwyTDf7ayKAz6GSxsEyNb7/p51mT1DeySgD/C4EPstmJQGktQXlZS1SfEzKeMoVQatzBDaPsI="

    }
]


class workSpace():
    def __init__(self):
        useService = service[3]
        self.user = useService['userName']
        self.ip = useService['service']
        self.cookie = self.need_Verify_Code()
        self.password = useService['password']
        self.round = useService["round"]
        self.userId = useService["userId"]
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
            print(str(log_id) + str(response.text))
            return response.text
        else:
            return "审批失败，审批节点为" + str(log_id)

    def add_reimburse(self):
        _url = "http://" + self.ip + "/nky/service/Reimburse"
        _payload = {
            {
                "paySettingId": 303,
                "amount": 1,
                "payeeFullName": "北京建谊高能建筑设计研究院有限公司",
                "payeeBankAccount": 'null',
                "payeeBank": 'null',
                "departmentId": 10001,
                "createdUserId": 10152,
                "billFlowDefineId": 10197,
                "description": "给唐婷使用",
                "reimbursePayItems": [
                    {
                        "paySettingId": 303,
                        "amount": 1,
                        "payeeFullName": "北京建谊高能建筑设计研究院有限公司"
                    }
                ],
                "fiscalYearId": 10120,
                "additionalValues": {},
                "id": 'null',
                "laborsAmountTypeId": 'null',
                "applyDate": "2022-01-11T09:31:15.517Z",
                "contractItemId": 'null',
                "srcBillId": 'null',
                "budgetApplicationId": 'null',
                "laborFeeDetails": [],
                "travelFeeDetails": [],
                "trainingFees": [],
                "meetingFees": [],
                "abroadFeeDetails": [],
                "officialTransportFeeDetails": [],
                "officialFeeItems": [],
                "reimburseItems": [
                    {
                        "budgetItemId": 11103,
                        "amount": 1,
                        "actual": 0
                    }
                ],
                "orgnizationId": 200
            }
        }

    def common_commentToUsers(self):
        _url = "http://" + self.ip + "/nky/service/common/commentToUsers"
        # noticeTypeId固定为1000
        _payload = {
            'noticeTypeId': 1000,
            'billType': 'Contract',
            'billId': 10551,
            'description': '测试',
            'createdUserId': 10101,
            'toUsers': [10101, 10102]
        }
        _header = self.headers
        response = requests.request("POST", _url, data=json.dumps(_payload), headers=_header)
        print(response)
        print(response.text)
        if '200' in str(response):
            return response.text
        else:
            return "操作失败"

    def agree(self, _id):
        _url = "http://" + self.ip + "/nky/service/ApprovalLog/" + str(_id)
        _payload = {
            "id": _id,
            "approvalStatusId": 502,
            "approvalDate": "2022-01-04T06:03:35.168Z",
            "description": "同意，同意，同意",
            "additionalValues": {}
        }
        # print(_url,_payload,self.headers)
        res = requests.request("PUT", _url, data=json.dumps(_payload), headers=self.headers)
        print(res.text, res)

    def batchUpdateReimburse(self):
        """批量核销"""
        _url = "http://" + self.ip + "/nky/service/reimburse/batchUpdateReimburse"
        _payload = {
            "reimburseIds": [
                1,
                2
            ],
            "closeApply": 'true'

        }
        res = requests.request("POST", _url, data=json.dumps(_payload), headers=self.headers)
        print(res)
        print(res.text)


if __name__ == '__main__':
    a = workSpace()
    a.login()

    for i in [
        66919,
        66921,
        66923,
        66925,
        66927,
        66929,
        66931,
        66933,
        66935,
        66937,
        66939,
        66941,
        66943,
        66945,
        66947,
        66949,
        66951,
        66953,
        66955,
        66957,
        66959,
        66961,
        66963,
        66965,
        66967,
        66969,
        66971,
        66973,
        66975,
        66977,
        66979,
        66981,
        66983,
        66985,
        66987,
        66989,
        66991,
        66993,
        66995,
        66997,
        66999,
        67001,
        67003,
        67005,
        67007,
        67009,
        67011,
        67013,
        67015,
        67017,
        67019,
        67021,
        67023,
        67025,
        67027,
        67029,
        67031,
        67033,
        67035,
        67037,
        67039,
        67041,
        67043,
        67045,
        67047,
        67049,
        67051,
        67053,
        67055,
        67057,
        67059,
        67061,
        67063,
        67065,
        67067,
        67069,
        67071,
        67073,
        67075,
        67077,
        67079,
        67081,
        67083,
        67085,
        67087,
        67089,
        67091,
        67093,
        67095,
        67097,
        67099,
        67101,
        67103,
        67105,
        67107,
        67109,
        67111,
        67113,
        67115,
        67117,
        67119,
        67121,
        67123,
        67125,
        67127,
        67129,
        67131,
        67133,
        67135,
        67137,
        67139,
        67141,
        67143,
        67145,
        67147,
        67149,
        67151,
        67153,
        67155,
        67157,
        67159,
        67161,
        67163,
        67165,
        67167,
        67169,
        67171,
        67173,
        67175,
        67177,
        67179,
        67181,
        67183,
        67185,
        67187,
        67189,
        67191,
        67193,
        67195,
        67197,
        67199,
        67201,
        67203,
        67205,
        67207,
        67209,
        67211,
        67213,
        67215,
        67217
    ]:
        time.sleep(1)
        a.standard_approve_log(i)

    # a.batchUpdateReimburse()

    # print(a.common_commentToUsers())
    requests.session().close()
