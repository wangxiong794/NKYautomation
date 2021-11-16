import json

import requests
from service.rw_cookie import write_file
from config import ip,user,user_id,run_id,password

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_mainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())



def need_Verify_Code():  # 获取cookie
    url = "http://" + ip + "/nky/service/session/needVerifyCode"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Host": ip,
        "Referer": "http://" + ip + "/nky",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.122 Safari/537.36",
    }
    response = requests.request("GET", url,headers=headers)
    header = eval(str(response.headers))  # 将请求后的字符类型先简单转成str，再换成dict
    set_cookie = header['Set-Cookie']
    cookie = set_cookie[0:43]
    write_file('"'+cookie+'"')
    # print("cookie：" + str(cookie))
    return cookie


def login(cookies):
    url = "http://" + ip + "/nky/service/session/login"
    payload ={
        "userName": user,
        "password": password,
        "round": run_id,
    }
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        'content-length': "240",
        'content-type': "application/json; charset=utf-8",
        'Cookie': cookies,
        "Host": ip,
        'origin': "http://" + ip,
        "Referer": "http://" + ip + "/nky",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.122 Safari/537.36",
        "x-Current-User-Id": user_id,
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    # print("登录状态"+str(response))


def get_cookie_login():
    url = "http://" + ip + "/nky/service/session/needVerifyCode"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Host": ip,
        "Referer": "http://" + ip + "/nky",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.122 Safari/537.36",
    }
    response = requests.request("GET", url, headers=headers)
    header = eval(str(response.headers))  # 将请求后的字符类型先简单转成str，再换成dict
    set_cookie = header['Set-Cookie']
    cookie = set_cookie[0:43]
    write_file('"' + cookie + '"')
    # print("cookie：" + str(cookie))
    login_url = "http://" + ip + "/nky/service/session/login"
    login_payload = {
        "userName": user,
        "password": password,
        "round": run_id,
    }
    login_headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        'content-length': "240",
        'content-type': "application/json; charset=utf-8",
        'Cookie': cookie,
        "Host": ip,
        'origin': "http://" + ip,
        "Referer": "http://" + ip + "/nky",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.122 Safari/537.36",
        "x-Current-User-Id": str(user_id),
    }
    login_response = requests.request("POST", login_url, data=json.dumps(login_payload), headers=login_headers)
    print("登录状态"+str(login_response))
    return cookie

if __name__ == "__main__":
    get_cookie_login()