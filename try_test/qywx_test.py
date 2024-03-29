# coding=utf-8
import json
import requests


def get_provider_token():
    # 获取服务商凭证
    _url = 'https://qyapi.weixin.qq.com/cgi-bin/service/get_provider_token'
    _payload = {
        # 替换服务商自己的CorpID和secret，参数在企业微信-服务商后台-应用管理-通用开发参数查找
        "corpid": "ww0d8d895844978572",
        "provider_secret": "kDPLlGRjyRJAuXJaEWEjklXiQ57Qsf7tB9Or8hjlp8_8i8Sw7PWk59ynRaHEpBjl"
    }
    _response = requests.request("POST", _url, data=json.dumps(_payload)).text
    # print(_response)
    provider_access_token = json.loads(_response)['provider_access_token']
    print(provider_access_token)
    return provider_access_token


def corpid_to_opencorpid(provider_access_token):
    # 将明文corpid转换为第三方应用获取的corpid
    _url = 'https://qyapi.weixin.qq.com/cgi-bin/service/corpid_to_opencorpid?provider_access_token='+provider_access_token
    _payload = {
        # 参数corpid需要替换客户的CropID
        "corpid": "ww185138e258230a69"
    }
    _response = requests.request("POST", _url, data=json.dumps(_payload)).text
    print(_response)


def close():
    requests.session().close()

if __name__ == "__main__":
    a = get_provider_token()
    corpid_to_opencorpid(a)
    close()
