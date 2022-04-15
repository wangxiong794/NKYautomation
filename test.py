# coding=utf-8
# import pyttsx3
# pyttsx3.speak("你好")
#
# import pandas as pd
#
# data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
#
# df = pd.DataFrame(data)
#
# print (df)
import json

import requests
def wx_api():
    url='https://qyapi.weixin.qq.com/cgi-bin/linkedcorp/user/get?access_token=ACCESS_TOKEN'
    body={
        "userid": "wx39cca523bb010ea0/13882657533"
    }
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        # 'content-length': "240",
        'content-type': "application/json; charset=utf-8",
        # 'Cookie': self.cookie,
        # "Host": self.ip,
        # 'origin': "http://" + self.ip,
        # "Referer": "http://" + self.ip + "/nky",
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
        #               "Chrome/80.0.3987.122 Safari/537.36",
        # "x-Current-User-Id": self.userId,
    }
    response = requests.request("PUT", url, data=json.dumps(body), headers=headers)
    print(response.text)

wx_api()