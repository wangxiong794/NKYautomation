import json

import requests
from service.logger import Log
from service.login import get_cookie_login
from config import common_header
log = Log()


def add_user(c, i):
    url = "http://123.56.223.19/nky/service/uaccount/addUserAccount"
    common_header['cookie'] = c
    add_data = {
        'name': "user"+i,
        'accountName': "user"+i,
        'departmentId': 'null',
        'mobile': "14782536978",
        'idNo': '',
        'supervisorUserId': '',
        'description': '',
        'position': '',
    }
    success = requests.request("POST",url,headers=common_header, data=json.dumps(add_data)).json()
    message = "第 %s 条:" %(i)+str(success)
    log.info(message)


if __name__ == "__main__":
    a = get_cookie_login()
    for b in range(2,10002):
        add_user(a,str(b))