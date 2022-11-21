# 内控易自动提交校内项目
# coding=utf-8
"""内控易校内项目自动审批"""
import json
import time
from service.logger import Log
import pymysql
import requests

service = [
    {"service": "demo4.neikongyi.com", "round": "14936",
     "password": "nga+eNSuUrhHx/K9W1C/a/qtWqsV30AHQjjm0tWToik=,1ihNzkC+zh+TKlMqP4Jz2jjyq6xf35sX,otJ+EuH/6L3TW51gTEKaLULuik2L+KbvrunnwS/G0P1VMKGG9F6JvGfWHn+NinGF3cFdVhnnDDAjDDBJbeBvhBvVcmRp03iAP7eSpZh1Zz4="},
    {"service": "39.107.221.188", "round": "14604",
     "password": "mYy8+QClL3k7B0tw7hxatyKuki1JJ7pyE++6JQKu+yw=,YeWqwTvWP32OHuttwv+j+NLT3vQrQ6tT,uXjqZj8MFez3rBlFL7xptS++0+MljjyVjBGd/VnNHBpstxmVgpvJoYcT9B5Jr9sOQktSrnMAgBG8IRRG0x51HYda/zeNBz4qQeqQA8lj6lw="}
]
log = Log()


# demo4_ip = 'demo4.neikongyi.com'
# demo4_user = 'admin1'
# demo4_password = ''
# demo4_round = ''
# demo4_headers={
#     'Accept': 'application/json',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Connection': 'keep-alive'
# }


# ip = demo4_ip
# user = demo4_user
# password = demo4_password
# round=demo4_round


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
            'description': "自动同意",
            'id': log_id,
            'additionalValues': {}
        }
        _header = self.headers
        response = requests.request("PUT", _url, data=json.dumps(_payload), headers=_header)
        if '200' in str(response):
            return response.text
        else:
            return "审批失败，审批节点为" + str(log_id)

    def pmZjlz(self, _log_id):
        # 先不管这个节点
        _url = "http://" + self.ip + "/nky/service/ApprovalLog/" + str(_log_id)
        _payload = {
            'approvalDate': "2021-11-15T02:06:02.998Z",
            'approvalStatusId': 502,
            'description': "自动同意",
            'id': _log_id,
            'additionalValues': {},
            'approTempProperties': '{\"items\":[{\"title\":\"论证金额(元)\",\"value\":\"1,146,200.00\"}]}'
        }
        _header = self.headers
        response = requests.request("PUT", _url, data=json.dumps(_payload), headers=_header)
        if '200' in str(response):
            return response.text
        else:
            return "审批失败，审批节点为" + str(_log_id)


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
        sql_1 = "SELECT id,`name`,status_id,activity_id,xm_total_amount FROM pm_special_project WHERE status_id=2 AND " \
                "orgnization_id=200 AND activity_id !='mergeProject' AND project_term=1; "
        db_1.execute(sql_1)
        return list(db_1)


def sql_approve_log(bill_id, activity):
    # 查询下一审批人
    try:
        with DB() as db_2:
            sql_2 = "SELECT id,activity_id FROM approval_log WHERE orgnization_id=200 AND " \
                    "bill_type='pmSpecialProject' AND activity_id !='" + str(
                activity) + "'  AND approval_status_id=501 AND " \
                            "bill_id=" + str(bill_id) + "; "
            db_2.execute(sql_2)
            return list(db_2)
    except:
        with DB() as db_2:
            sql_2 = "SELECT id,activity_id FROM approval_log WHERE orgnization_id=200 AND " \
                    "bill_type='pmSpecialProject' AND activity_id !=" + str(
                activity) + "  AND approval_status_id=501 AND " \
                            "bill_id=" + str(bill_id) + "; "
            db_2.execute(sql_2)
            return list(db_2)


def sql_budget_item(bill_id):
    # 数据库插本年测算数据
    with DB() as db_3:
        sql_0 = "SELECT pm_special_project_id,years,group_name,group_name_des,`name` ,standard_control_id, financial_account_id,amount,description FROM pm_project_budget_item WHERE years =2022 AND pm_special_project_id=" + str(
            bill_id) + ";"
        db_3.execute(sql_0)
        list_0 = list(db_3)
        if len(list_0) == 0:
            sql_3 = "SELECT pm_special_project_id,years,group_name,`name` ,standard_control_id, financial_account_id,amount,description FROM pm_project_budget_item WHERE pm_special_project_id=" + str(
                bill_id) + ";"
            db_3.execute(sql_3)
            listdata = list(db_3)
            for i in listdata:
                i['years'] = 2022
                data_str = str(i['pm_special_project_id']) + "," + str(i['years']) + ",'" + str(
                    i['group_name']) + "','" + str(
                    i['name']) + "'," + str(i['standard_control_id']) + "," + str(
                    i['financial_account_id']) + "," + str(
                    i['amount']) + ",'" + str(i['description']) + "'"
                sql_4 = "INSERT INTO `pm_project_budget_item` (`pm_special_project_id`, `years`, `group_name`, " \
                        " `name`, `standard_control_id`, `financial_account_id`, `amount`, `description`) " \
                        "VALUES (%s); " % data_str
                db_3.execute(sql_4)
        else:
            log.info("项目%s已有本年测算，无需二次生成" % (str(bill_id)))


def sql_indicator_item(bill_id):
    # 数据库插本年绩效目标
    with DB() as db_4:
        sql_0 = "SELECT pm_special_project_id,years,indicator_id,operation_type_id,target,budget_rate FROM " \
                "pm_project_indicator_item WHERE years = 2022 AND pm_special_project_id=" + str(
            bill_id) + ";"
        db_4.execute(sql_0)
        list_0 = list(db_4)
        if len(list_0) == 0:
            sql_3 = "SELECT pm_special_project_id,years,indicator_id,operation_type_id,target,budget_rate FROM " \
                    "pm_project_indicator_item WHERE pm_special_project_id=" + str(
                bill_id) + ";"
            db_4.execute(sql_3)
            listdata = list(db_4)
            for i in listdata:
                i['years'] = 2022
                data_str_1 = str(i['pm_special_project_id']) + "," + str(i['years']) + "," + str(
                    i['indicator_id']) + "," + str(i['operation_type_id']) + ",'" + str(i['target']) + "'," + str(
                    i['budget_rate'])
                sql_4 = "INSERT INTO `pm_project_indicator_item` (`pm_special_project_id`, `years`, `indicator_id`, " \
                        "`operation_type_id`, `target`, `budget_rate`) VALUES (%s);" % data_str_1
                db_4.execute(sql_4)
        else:
            log.info("项目%s已有本年指标，无需二次生成" % (str(bill_id)))


def sql_year_budget_item(bill_id):
    # 根据测算明细插入部门经济科目
    with DB() as db_5:
        sql_0 = "SELECT * FROM pm_project_year_budget_item WHERE years=2022 AND pm_special_project_id=" + str(
            bill_id) + ";"
        db_5.execute(sql_0)
        list_0 = list(db_5)
        if len(list_0) == 0:
            sql_3 = "SELECT pm_special_project_id,years,financial_account_id,SUM(amount) as amount FROM " \
                    "pm_project_budget_item WHERE years=2022 AND pm_special_project_id=%s GROUP BY " \
                    "financial_account_id;" % (str(bill_id))
            db_5.execute(sql_3)
            listdata = list(db_5)
            for i in listdata:
                i['years'] = 2022
                data_str = str(i['pm_special_project_id']) + "," + str(i['years']) + ",111,10001," + str(
                    i['financial_account_id']) + "," + str(i['amount'])
                sql_4 = "INSERT INTO `pm_project_year_budget_item` (`pm_special_project_id`, `years`, " \
                        "`pm_capital_property_id`, `functional_account_id`, `financial_account_id`, " \
                        "`ben_one_up_amount`) VALUES (%s);" % data_str
                db_5.execute(sql_4)
        else:
            log.info("项目%s已有本年年度预算，无需二次生成" % (str(bill_id)))


def sql_px(bill_id):
    # 排序入库
    with DB() as db_7:
        sql = " UPDATE pm_special_project SET is_sort=1 AND special_project_phases_id=5251 WHERE id=%s;" % str(bill_id)
        db_7.execute(sql)


def main(activity1='mergeProject'):
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
        elif _number == 500:
            requests.session().close()
            break
        else:
            for i in project_list:
                project_id = i['id']
                project_activity = i['activity_id']
                while project_activity != activity1:
                    approve_log_id = sql_approve_log(project_id, activity1)
                    if len(approve_log_id) != 0:
                        approve_log_id = approve_log_id[0]
                        if activity1 in approve_log_id['activity_id']:
                            break
                        else:
                            if 'pmYsbz' in approve_log_id['activity_id']:
                                sql_budget_item(project_id)
                                sql_indicator_item(project_id)
                                sql_year_budget_item(project_id)
                            elif 'workgroupSorting' in approve_log_id['activity_id']:
                                sql_px(project_id)
                            a.standard_approve_log(approve_log_id['id'])
                    else:
                        requests.session().close()
                        break
                _number += 1
                log.info("项目" + str(project_id) + "已审批至%s，请检查" % activity1)
                requests.session().close()
            requests.session().close()


def test():
    a = workSpace()
    a.login()

if __name__ == '__main__':
    # sql_budget_item(10126)
    # sql_indicator_item(10126)
    # sql_year_budget_item(10126)
    # test()
    for ab in range(0,50):
        log.info("第%s轮"%str(ab))
        time.sleep(10)
        try:
            main()
        except:
            continue
