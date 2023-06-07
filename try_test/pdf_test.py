# 读取解析PDF文件
import os
import random
import re

import pdfplumber


def read_pdf():
    data = ''
    with pdfplumber.open('test.pdf') as pdf:
        for page in pdf.pages:
            old_data = page.extract_text()
            data = data + old_data

        # print('----分页分隔-----')
    # question=re.findall('[\.](.+?)[？]',data)

    with open('test1.docx', 'w') as a:
        a.write(data)
        a.close()


def read_txt():
    with open('test.txt', 'r') as f:
        _data = f.read()
        print(len(_data))
        _list = re.split("\.*\答案：", _data)
        da = []
        _wt = []

        for quest in _list:
            new_data = re.split("\n", quest)
            for a in new_data:
                if len(a) == 0:
                    new_data.remove(a)
                if a == ' ':
                    new_data.remove(a)
            if len(new_data) > 5 or len(new_data) == 1:
                da.append(new_data[0])
                del new_data[0]

            if len(new_data) != 0:
                _wt.append(new_data)
        # print(_wt)
        # print(da)
        return _wt, da


def work(_wt, _da):
    zj=0
    zq=0
    c=[]
    while True:
        a = random.randint(0, 198)
        if a in c:
            pass
        else:
            for b in _wt[a]:
                print(b)
            # print(_wt[a])
            print("\n")
            ans = input("选择答案(退出按Q):")
            if ans == _da[a].replace(" ", ''):
                print("答案正确！正确选"+ _da[a])
                zq=zq+1
                c.append(a)
            elif ans == "Q":
                print("退出答题成功")
                break
            else:
                print("答案错误，正确为：" + _da[a])
            zj=zj+1
            print("总计做题："+str(zj)+"，正确【"+str(zq)+"】道题，加油呀!")

a = read_txt()
work(a[0], a[1])
# print(data)
# print(question)
# print(len(question))
