import json
import time

import requests
from service.logger import Log

service = [
    {"service": "test8.neikongyi.com", "round": "17897", "hm": "http://", "user": "cs", "id": "10594",
     "orgnizationId": "200", "password_mw": "nky2018",
     "password": "b0KEw4fh0ePpmfil434O/G9Jt0jMN7a7ZVS3iZUHMxY=,8wXbPiluLxdFrBn4JlOfSoC0eVM/7zax,12uIGxxFhnkbDHPA6Md+geFc65ELjlwvXO4ErgOJg8vdG5TXvl9xzsRteI6iAFrauimMq6lxqlzeKBb1mDw0x0atoiOnG+qZ0MpZCLSNulc="
     }
]
log = Log()


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
            'origin': "http://" + self.ip,
            "Referer": "http://" + self.ip + "/nky",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.122 Safari/537.36",
            "x-Current-User-Id": self.userId,
            "x-Current-Org-Id": self.org
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

    def save_project(self, depart_id, guide_depart_id, guide_id, cus_id, guide_name, budget_items, userids):
        url = self.http + self.ip + "/nky/service/PmSpecialProject"
        pay_load = {
            "pmProjectClassId": 10008,
            "name": guide_name,
            "departmentId": depart_id,
            "years": 2022,
            "projectTerm": 1,
            "pmXnProjectTypeId": 5381,
            "guideDepartmentId": guide_depart_id,
            "billFlowDefineId": 10011,
            "isLongTerm": 'false',
            "fiscalYearId": 10000,
            "pmSpecialGuideId": guide_id,
            "customObjectTmplId": cus_id,
            # "pmProjectBudgetItems": [
            #     {
            #         "groupName": "默认任务组",
            #         "name": "部门交通费",
            #         "financialAccountId": 30039,
            #         "projectYear": "2022",
            #         "financialAccountCode": "30239",
            #         "financialAccountBudgetaryYearDefineId": 'null',
            #         "amount": '0.00',
            #         "ztYearRel": 1,
            #         "pfAmount": 'null'
            #     }
            # ],
            "pmProjectBudgetItems": budget_items,
            "pmProjectPropertyId": 6700,
            "statusId": 1,
            "orgnizationId": 200,
            'xmTotalAmount': 0,
            # "pfAmount": 0,
            "specialProjectPhasesId": '5253',
            "createUserId": userids,
            "applyUserId": userids,
            "manager_user_id": userids
        }

        _response = requests.request("POST", url, data=json.dumps(pay_load), headers=self.headers)
        log.info("生成成功，项目ID为%s" % str(_response.text))
        return _response.text
        # print(_response.text)

    def save_year_budget(self, project_id):
        _url = self.http + self.ip + "/nky/service/PmSpecialYearProject"
        pay_load = {

            "fiscalYearId": 10000,
            "years": 2022,
            "specialProjectPhasesId": 5253,
            "additionalValues": {
                "firstYear": 'true'
            },
            "pmSpecialProjectId": project_id,
            # "statusId": 1,
        }
        _response = requests.request("POST", _url, data=json.dumps(pay_load), headers=self.headers)
        print(_response.text)

    def start_flow(self, bill_id):
        url = self.http + self.ip + "/nky/service/billcommon/startFlow"
        pay_load = {
            "billId": bill_id,
            "billType": "PmSpecialProject",
            "billFlowDefineId": 10011
        }
        _response = requests.request("POST", url, data=json.dumps(pay_load), headers=self.headers)
        print(_response.text)

    def save_Reimbursee(self):
        _url = self.http + self.ip + "/nky/service/Reimburse"
        # _payload = "{\"paySettingId\":301,\"amount\":1,\"payeeFullName\":\"成都市技师学院\",\"payeeBankAccount\":\"4402054609100031151\",\"payeeBank\":\"工商银行成都红光支行\",\"departmentId\":10004,\"billFlowDefineId\":10031,\"createdUserId\":10594,\"description\":\"校验重复提交的情况\",\"reimbursePayItems\":[{\"paySettingId\":301,\"amount\":1,\"payeeFullName\":\"成都市技师学院\",\"payeeBankAccount\":\"4402054609100031151\",\"payeeBank\":\"工商银行成都红光支行\"}],\"fiscalYearId\":10015,\"additionalValues\":{},\"id\":null,\"laborsAmountTypeId\":null,\"applyDate\":\"2022-12-18T14:57:57.234Z\",\"contractItemId\":null,\"srcBillId\":null,\"budgetApplicationId\":null,\"laborFeeDetails\":[],\"travelFeeDetails\":[],\"trainingFees\":[],\"meetingFees\":[],\"abroadFeeDetails\":[],\"officialTransportFeeDetails\":[],\"officialFeeItems\":[],\"reimburseItems\":[{\"budgetItemId\":10878,\"amount\":1,\"actual\":0}],\"orgnizationId\":200}"
        _payload = {
          "paySettingId": 301,
          "amount": 1,
          "payeeFullName": "成都市技师学院",
          "payeeBankAccount": "4402054609100031151",
          "payeeBank": "工商银行成都红光支行",
          "departmentId": 10004,
          "billFlowDefineId": 10031,
          "createdUserId": 10594,
          "description": "校验重复提交的情况",
          "reimbursePayItems": [
            {
              "paySettingId": 301,
              "amount": 1,
              "payeeFullName": "成都市技师学院",
              "payeeBankAccount": "4402054609100031151",
              "payeeBank": "工商银行成都红光支行"
            }
          ],
          "fiscalYearId": 10015,
          "id": "",
          "applyDate": "2022-12-18T14:57:57.234Z",
          "reimburseItems": [
            {
              "budgetItemId": 10878,
              "amount": 1,
              "actual": 0
            }
          ],
          "orgnizationId": 200
        }
        _response = requests.request("POST", _url, data=json.dumps(_payload), headers=self.headers)
        log.info("保存成功%s" % str(_response.text))
        return _response.text

if __name__ == "__main__":
    a = workSpace()
    a.login()
    while True:
        a.save_Reimbursee()
        # time.sleep(1)