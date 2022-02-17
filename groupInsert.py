# coding=utf-8
# 处理大集中升级的数据

import re

myneed = open(r'F:\workspace\宁夏大集中升级\10114原州区第十四小学\原州区十四小1月6日nky.sql','r',encoding='utf-8')
needsql = open(r'F:\workspace\宁夏大集中升级\10114原州区第十四小学\原州区十四小1月6日insert_nky.sql','w',encoding='utf-8')
txt_lines = myneed.readlines()
for line in txt_lines:
    print(line)
    need_sql = re.match(r'^INSERT INTO .* VALUES', line)
    print(need_sql)
    if need_sql != None:
        print(need_sql)
        needsql.write(line)
        continue
    else:
        continue
