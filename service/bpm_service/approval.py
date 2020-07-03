import datetime

import requests

from config import ip
from service.connectmysql import DB

def sql_approveid(billtype, billid):
    with DB() as db:
        select_sql = "select id from approval_log where bill_type='" + billtype + "' and bill_id='" + billid + "';"
        db.execute(select_sql)
        approveidlist = list(db)
        approveidlistlen = len(approveidlist)
        assert 2 == approveidlistlen, approveidlistlen
        approveiddict = approveidlist[1]
        approveid = approveiddict['id']
        approveid = str(approveid)
    return approveid


def sql_approval_id():  # 查找最新的审批日志的bill_type，查找审批日志的单据类型与单据id。不同的单据类型单据id是存在相同情况
    with DB() as db:
        db.execute("SELECT bill_type,bill_id FROM approval_log where id = (SELECT MAX(id) FROM approval_log)")
        idlist = list(db)
        iddict = idlist[0]
        billtype = str(iddict['bill_type'])
        abillid = str(iddict['bill_id'])
    return billtype, abillid


