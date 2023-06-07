# 通过Excel下载附件
import os

import xlrd
import paramiko


def read(row):
    book = xlrd.open_workbook(r"./童心家园幼儿园合同附件.xls")
    sheet = book.sheet_by_index(0)
    # print(sheet.cell_value(1, 1))
    data = [sheet.cell_value(row, 1), sheet.cell_value(row, 6), sheet.cell_value(row, 7)]
    return data


def get_file():
    hostname = '39.105.112.114'
    port = 22
    username = 'root'
    password = 'lanny123#@!'

    # local_path = local_path + '/' + str[_data[1]]
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password)
    sftp = ssh.open_sftp()
    root_dir = os.path.dirname(os.path.abspath(__file__))
    for i in range(1,77):
        _data = read(i)
        remote_path = '/var/lib/tomcat8/webapps/uploadFiles' + str(_data[2])
        local_path = os.path.join(root_dir, 'file', _data[0])
        if not os.path.exists(local_path):
            os.makedirs(local_path)
        local_path2 = os.path.join(local_path, _data[1])
        print(_data[1])
        sftp.get(remote_path, local_path2)

    ssh.close()


# for i in range(1, 1075):
#     name = read(i)
#     get_file(name)
get_file()