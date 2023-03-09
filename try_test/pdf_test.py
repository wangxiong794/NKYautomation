# 读取解析PDF文件
import os
import re

import pdfplumber

data = ''
with pdfplumber.open('test.pdf') as pdf:
    for page in pdf.pages:
        old_data = page.extract_text()
        data=data+old_data

        # print('----分页分隔-----')
# question=re.findall('[\.](.+?)[？]',data)
with open('test1.docx','w') as a:
    a.write(data)
    a.close()
# print(data)
# print(question)
# print(len(question))