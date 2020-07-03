# coding=utf-8

import os

from ddt import ddt, data
import unittest
import json

from config import ip, user_id
from get_root_path import root_dir
from service import login
from service.check import Check
from service.readYaml import operYaml
from service.send import sendRequest
from service.writeLog import writeLog


@ddt
class test_Login(unittest.TestCase):
    yamlPath = ['login', 'login_1.yaml']
    yaml_path = os.path.join(root_dir, "yamlCase")
    for dir in yamlPath:
        yaml_path = os.path.join(yaml_path, dir)
    oper_yaml = operYaml(yaml_path)
    case_list = oper_yaml.caseList()

    method = case_list[0]["method"]
    uri = case_list[1]["uri"]

    # 跳过说明
    # reason = confParam("skip_reason")

    @classmethod
    def setUpClass(cls):

        # 拼接接口地址
        cls.cook = login.need_Verify_Code()
        cls.url = 'http://' + ip + cls.uri

        # 请求信息头
        cls.headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            'content-length': "240",
            'content-type': "application/json; charset=utf-8",
            'Cookie': cls.cook,
            "Host": ip,
            'origin': "http://" + ip,
            "Referer": "http://" + ip + "/nky",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.122 Safari/537.36",
            "x-Current-User-Id": str(user_id),
        }

    # case_list传进去做数据驱动
    @data(*case_list[2:])
    def test_login(self, cases):

        for caseName, caseInfo in cases.items():
            caseName = caseName
            data = json.dumps(caseInfo["data"])
            check = caseInfo["check"]
            self.__dict__['_testMethodDoc'] = caseName

        # 发送请求
        print(data)
        print(type(data))
        response = sendRequest(self.method, self.url, self.headers, data)

        # 接口返回文本信息
        text = response.text
        text_dict = json.loads(text)

        # 写日志
        writeLog(caseName, self.url, data, check, text)

        # 断言
        Check().check(check, text_dict)

        @classmethod
        def tearDownClass(cls):
            pass


if __name__ == "__main__":
    unittest.main()
