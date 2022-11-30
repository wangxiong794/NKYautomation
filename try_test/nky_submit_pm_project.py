# 内控易自动提交校内项目
# coding=utf-8
"""内控易校内项目自动审批"""
import json
import os
import re
import time

import xlrd

from service.logger import Log
import pymysql
import requests

file_dir = os.path.dirname(os.path.abspath(__file__))
old_file = os.path.join(file_dir, "定额上报项目.xls")
service = [
    {"service": "dev3.neikongyi.com", "round": "15723", "hm": "http://", "user": "admin1", "id": "1",
     "orgnizationId": "200", "password_mw": "nky2018",
     "password": "mH5o9J0Ux2STESsJRYDz6Cet1VR3CB3cmTUs5WrR93M=,fFCtmQCcr52EW5eWIYujPiwYpgjW5uvO,bhcWI0brGfJjnV9OOQLaVGi47S45WBTnMfj4OvyXzEYf0huk0ccp0rv9mJ/aSsms2XN1thNYzG82i5cfbCLAmOyk2g8up8JyvhcP8yaNBM4="
     }
]
data = [
    {"service": "dev3.neikongyi.com", "round": "14552", "hm": "http://", "user": "zhangshuying", "id": "10200",
     "orgnizationId": "200", "password_mw": "nky2018",
     "password": "CfbaMqsGzRQnJCM3X7Ci7DYTD3yCd8tWDwqrHSHQJzo=,o46yj102Fr/GBKi9G++DBCauv4VyvKaf,KI88rPGCM1io0668Ibz06pcIlx/fElNGFi9+UnARuJslOYnxXWsqbCUER1/jkCqWFmtr6g+UKkfl77s3D8m2lcjmETUozHB48+S8aafyE/o="
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


def read_data():
    """
    # 查询需要上报的定额明细
    SELECT
        e.department_id AS guide_department_id,
        b.department_id,
        b.id AS guide_id,
        b.custom_object_tmpl_id,
        b.`name`,
        a.user_ids,
        b.pm_project_content
    FROM
        pm_guide_user_item AS a
        LEFT JOIN pm_special_guide AS b ON a.pm_special_guide_id = b.id
        LEFT JOIN pm_project_class AS d ON b.pm_project_class_id = d.id
        LEFT JOIN user_orgnization AS e ON a.user_ids = e.user_id
    WHERE
        b.is_quota = 1;
    """
    book = xlrd.open_workbook(old_file, formatting_info=True)
    table = book.sheet_by_index(0)
    nrows = table.nrows  # 包括标题
    # 获取总列数
    ncols = table.ncols
    # 计算出合并的单元格有哪些
    colspan = {}
    if table.merged_cells:
        for item in table.merged_cells:
            for row in range(item[0], item[1]):
                for col in range(item[2], item[3]):
                    # 合并单元格的首格是有值的，所以在这里进行了去重
                    if (row, col) != (item[0], item[2]):
                        colspan.update({(row, col): (item[0], item[2])})
    # 读取每行数据
    data = []
    row = []
    for i in range(1, nrows):
        row = []
        for j in range(ncols):
            # 假如碰见合并的单元格坐标，取合并的首格的值即可
            if colspan.get((i, j)):
                row.append(table.cell_value(*colspan.get((i, j))))
            else:
                row.append(table.cell_value(i, j))
        # print(row)
        data.append(row)
    data.append(row)
    _run = workSpace()
    _run.login()
    del data[-1]
    # print(data)
    for _data in data:
        # _data[0]=str(re.split("\.", str(_data[0]))[0])
        guide_department_id = str(re.split("\.", str(_data[0]))[0])
        department_id = str(re.split("\.", str(_data[1]))[0])
        guide_id = str(re.split("\.", str(_data[2]))[0])
        guide_name = _data[3]
        custom_object_tmpl_id = str(re.split("\.", str(_data[4]))[0])
        user_ids = str(re.split("\.", str(_data[5]))[0])
        budget_items = json.loads(_data[6])["pmProjectBudgetItems"]
        # print(department_id, guide_department_id, guide_id, custom_object_tmpl_id, guide_name,
        #       budget_items, user_ids)
        projcet_id = _run.save_project(department_id, guide_department_id, guide_id, custom_object_tmpl_id, guide_name,
                                       budget_items, user_ids)
        _run.save_year_budget(projcet_id)


if __name__ == '__main__':
    # a = workSpace()
    # a.login()
    # test_data=[10024,10010,10029,"勤工俭学(困难补助)",10003,10200,{"name":"勤工俭学(困难补助)","departmentId":10024,"years":"2022","projectTerm":1,"pmXnProjectTypeId":5381,"guideDepartmentId":10010,"billFlowDefineId":10007,"isLongTerm":"false","pmProjectTextItems":[],"pmProjectStrategicTasks":[],"pmProjectIndicatorItems":"null","pmProjectIndicatorTextItems":[],"pmProjectBudgetItems":[{"groupName":"默认任务组","name":"勤工俭学（困难补助）","projectYear":"2022","financialAccountCode":"30305","financialAccountBudgetaryYearDefineId":"null","amount":"null","financialAccountId":30047}],"pmProjectPayPlanItems":[],"pmProjectYearBudgetItems":[],"pmProjectGoverServerItems":[],"pmProjectAssetItems":[],"pmProjectGoverPurItems":[]}]
    # bill_id = a.save_project(10000, 10010, 10033, 10003, 'name',[],'10000')
    # a.save_year_budget(str(bill_id))
    # a.start_flow(10068)
    read_data()
