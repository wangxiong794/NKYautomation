# coding=utf-8

import json
import requests

from config import ip, user_id, user, password, run_id
from service import login


def sendRequest(method, nky_url, nky_headers, nky_payload):
    if method == "GET":
        return requests.request('GET', nky_url, headers=nky_headers)

    elif method == "POST":
        return requests.request('POST', url=nky_url, headers=nky_headers, data=nky_payload)

    elif method == "PUT":
        print('PUT方法')


if __name__ == "__main__":
    cook = login.need_Verify_Code()
    url = "http://" + ip + "/nky/service/session/login"
    payload = {
        "userName": user,
        "password": password,
        "round": run_id,
    }
    headers = {"Accept": "application/json",
               "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.9",
               "Connection": "keep-alive",
               'content-length': "240",
               'content-type': "application/json; charset=utf-8",
               'Cookie': cook,
               "Host": ip,
               'origin': "http://" + ip,
               "Referer": "http://" + ip + "/nky",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/80.0.3987.122 Safari/537.36",
               "x-Current-User-Id": str(user_id), }
    print(type(payload))
    payload = json.dumps((payload))
    print(type(payload))
    res = sendRequest("POST", url, headers, payload)
    print(res)