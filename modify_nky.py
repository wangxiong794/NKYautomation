# coding=utf-8
"""
当需要修改某个字段的值，前端无法修改，数据库连不上时，用接口去修改数据
"""
import json

import requests

url = "http://39.106.158.149/nky"
user = "admin1"
passwd = "nky2018"

service = [
    {"service": "39.106.158.149", "round": "14244",
     "password": "dXxF1fZQjft7+91IztQzpLT1RtqzJU98+VcwwJIpBHk=,4C1KWxB31/bWvqfj7dx4XpW/Oh4X2u+V,"
                 "zVl2TzSIY0GekGWb0olxFNjc9K7Oxqu4PD7OCRJ6qLb13yg+f/BydqB5szIdPGG7w/G5O7t1KY2Hc2CTim8JxrOnYuGv"
                 "+9ZOsCGvbnwlRuY="},
    {"service": "58.118.2.63", "round": "14201",
     "password": "7FtAhUOPzKj/4R4zkn4z4kvUP0km71yFZ9LTYmxkW0c=,UeStnq9Cc1HXkzupml2z6q4feui1QdTP,"
                 "djxuw9Duqz9Ll/eOv2dJVeuD8RlI+s5+WBOyYdxMp26QiBBhFY"
                 "+cymp6Zh655d1nNrZj9BaoJR3HxMZWbHlWfjhk4ud7YTlQ4fGfDq4yKSE="},
    {
        "service":"39.106.158.149","round":"14265","userName":"wxfz10wmyh7q","orgnizationId":200,
        "userId":"10152",
        "password":"KNgNaynOMNamTi7xAkeMYJ7OjUKTTEuFQEQIaTxsmCc=,9PO3xflDJY0hCKP8QKn2Rl9m7YKmok3q,"
                   "+SVMcA8lpuo7+Njl3AGZaBvNpWkBZJ4/X1El3IfMge9xIL1Hs8ZGWN+TrT1ZyXR9lBv1rxb50hzXYcIPSsnIDXFzDZpX"
                   "/q7XM6XgQOWzxQQ="
    }

]


class workSpace:
    def __init__(self):
        useService = service[2]
        self.user = useService['userName']
        self.ip = useService['service']
        self.cookie = self.need_Verify_Code()
        self.password = useService['password']
        self.round = useService["round"]
        self.userId = useService['userId']
        self.headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            'content-length': "240",
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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.122 Safari/537.36",
        }
        response = requests.request("GET", url, headers=headers)
        header = eval(str(response.headers))  # 将请求后的字符类型先简单转成str，再换成dict
        set_cookie = header['Set-Cookie']
        cookie = set_cookie[0:43]
        print("cookie：" + str(cookie))
        return cookie

    def login(self):
        url = "http://" + self.ip + "/nky/service/session/login"
        payload = {
            "userName": self.user,
            "password": self.password,
            "round": self.round,
        }
        _headers = self.headers
        del _headers['x-Current-User-Id']
        print(_headers)
        response = requests.request("POST", url, data=json.dumps(payload), headers=_headers)
        print(response.text,response)
        has_time = response.elapsed.microseconds
        return has_time

    def modify_contract(self,ctId):
        """修改合同主表相关数据"""
        modify_ct_url = "http://" + self.ip + "/nky/service/Contract/"+str(ctId)
        payload = {
            "id": str(ctId),
            "amount": "11"
        }
        requests.request("PUT", modify_ct_url,data=json.dumps(payload), headers=self.headers)

    def batchUpdateReimburse(self):
        """批量核销"""
        _url="http://" + self.ip +"/nky/service/reimburse/batchUpdateReimburse"
        _payload={
                "reimburseIds": [
                    11954
                ],
                "closeApply": 'true'


        }
        res=requests.request("POST",_url,data=json.dumps(_payload),headers=self.headers)
        print(res)
        print(res.text)

    def agree(self,_id):
        _url="http://" + self.ip +"/nky/service/ApprovalLog/"+str(_id)
        _payload={
                "id": _id,
                "approvalStatusId": 502,
                "approvalDate": "2022-01-04T06:03:35.168Z",
                "description": "同意，同意，同意",
                "additionalValues": {}
            }
        print(_url,_payload,self.headers)
        res=requests.request("PUT",_url,data=json.dumps(_payload),headers=self.headers)
        print(res.text,res)


if __name__ == "__main__":
    a = workSpace()
    a.login()

    # a.agree(64770)