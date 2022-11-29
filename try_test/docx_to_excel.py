# 提取双高建设任务书中的任务信息，并解析到对应Excel中
import os
import re
import xlrd
from xlutils.copy import copy

file_dir = os.path.dirname(os.path.abspath(__file__))
old_file = os.path.join(file_dir, "双高任务书提取原表.xls")
new_file = os.path.join(file_dir, "双高任务书提取文件.xls")
symbol_file = os.path.join(file_dir, "../../三级建设任务分隔符.txt")


def read():
    # 从原表的第一个sheet中解析建设任务
    # book = xlrd.open_workbook(r"双高任务书提取原表.xls", formatting_info=True)

    book = xlrd.open_workbook(old_file, formatting_info=True)
    table = book.sheet_by_index(0)
    nrows = table.nrows  # 包括标题
    # 获取总列数
    ncols = table.ncols
    # 计算出合并的单元格有哪些
    colspan = {}
    if table.merged_cells:
        for item in table.merged_cells:
            for row in range(item[0], item[1]):
                for col in range(item[2], item[3]):
                    # 合并单元格的首格是有值的，所以在这里进行了去重
                    if (row, col) != (item[0], item[2]):
                        colspan.update({(row, col): (item[0], item[2])})
    # 读取每行数据
    data = []
    # 假设分隔符存在数字，则说明建设任务存在序号，分割后还需要拼接序号
    if '①'  in _symbol:
        for i in range(1, nrows):
            row = []
            for j in range(ncols):
                # 假如碰见合并的单元格坐标，取合并的首格的值即可
                if colspan.get((i, j)):
                    row.append(table.cell_value(*colspan.get((i, j))))
                else:
                    # 第4列第4行开始为末级建设任务
                    if i > 2 and j > 2:
                        _data = table.cell_value(i, j)
                        # 将末级建设任务str根据序号拆分成list的末级建设任务
                        row.append(jx_data(_data))
                    else:
                        row.append(table.cell_value(i, j))
            # print(row)
            data.append(row)
    # 假设不存在数字，则用具体符号分割，不需要数字拼接
    else:
        for i in range(1, nrows):
            row = []
            for j in range(ncols):
                # 假如碰见合并的单元格坐标，取合并的首格的值即可
                if colspan.get((i, j)):
                    row.append(table.cell_value(*colspan.get((i, j))))
                else:
                    # 第4列第4行开始为末级建设任务
                    if i > 2 and j > 2:
                        _data = table.cell_value(i, j)
                        # 将末级建设任务str根据序号拆分成list的末级建设任务
                        row.append(jx_data_back(_data))
                    else:
                        row.append(table.cell_value(i, j))
            # print(row)
            data.append(row)
    # 删除第一二行无意义数据
    del data[0]
    del data[0]
    two_task = []
    two_one_task = []
    one_task = []
    # 将列表拍平插入到Excel中
    for row in data:
        task1 = row[1]
        task2 = row[2]
        one_task.append(task1)
        if task2 in two_task:
            pass
        else:
            two_task.append(task2)
            two_one_task.append([task2, task1])
        for task3_2020 in row[3]:
            # print([task1,task2,'2020',task3_2020])
            write_data_item(task1, task2, '2020', task3_2020)
        for task3_2021 in row[4]:
            write_data_item(task1, task2, '2021', task3_2021)
        for task3_2022 in row[5]:
            write_data_item(task1, task2, '2022', task3_2022)
        for task3_2023 in row[6]:
            write_data_item(task1, task2, '2023', task3_2023)
    one_task = list(set(one_task))
    # print(one_task)
    for one in one_task:
        write_one_task(one)
    for _tow in two_one_task:
        write_tow_task(_tow[0], _tow[1], )
    # print(data)
    # # 读取每列数据
    # for j in range(ncols):
    #     col = []
    #     for i in range(1, nrows):
    #         # 假如碰见合并的单元格坐标，取合并的首格的值即可
    #         if colspan.get((i, j)):
    #             col.append(table.cell_value(*colspan.get((i, j))))
    #         else:
    #             col.append(table.cell_value(i, j))
    #     print(col)


def read_indicator():
    book = xlrd.open_workbook(old_file, formatting_info=True)
    table = book.sheet_by_index(1)
    nrows = table.nrows  # 包括标题
    # 获取总列数
    ncols = table.ncols
    # 计算出合并的单元格有哪些
    colspan = {}
    if table.merged_cells:
        for item in table.merged_cells:
            for row in range(item[0], item[1]):
                for col in range(item[2], item[3]):
                    # 合并单元格的首格是有值的，所以在这里进行了去重
                    if (row, col) != (item[0], item[2]):
                        colspan.update({(row, col): (item[0], item[2])})
    # 读取每行数据
    data = []
    unit_total = []
    for i in range(1, nrows):
        row = []
        for j in range(ncols):
            # 假如碰见合并的单元格坐标，取合并的首格的值即可
            if colspan.get((i, j)):
                row.append(table.cell_value(*colspan.get((i, j))))
            else:
                row.append(table.cell_value(i, j))
        # print(row)
        data.append(row)
    task1 = []
    for row_data in data:
        if row_data[3] == '':
            task1.append(row_data[2])
            data.remove(row_data)
    # print(data)
    # print(task1)
    for task_data in data:
        taskid = re.split('\s', task_data[2])[0]
        # print(taskid)
        taskid = taskid[0:taskid.rfind('.')]
        # print(taskid)
        for task in task1:
            # print(task[0:5])
            # if taskid == re.split('\s', task)[0]:
            if taskid == task[0:5]:
                # task_indicator = task
                task_data.append(task)
                break
        if len(task_data) < 5:
            task_data.append('')
        # print(task_data)
        # 取计量单位
        unit = re.findall(r'[（](.+?)[）]', str(task_data[2]))
        # print(unit)
        if len(unit) == 0:
            unit = ''
        else:
            unit = unit[-1]
            unit_total.append(unit)
        if '~' in str(task_data[3]):
            target_no_unit = str(task_data[3])[:-1]
            target_class = '数值范围'
            # unit = str(task_data[3])[-1]
        else:
            target_no_unit = re.findall(r'\d+(?:\.\d+)?', str(task_data[3]))
            # print(target_no_unit)
            if len(target_no_unit) == 0:
                target_no_unit = task_data[3]
                target_class = '文本'
            else:
                if unit == '%':
                    target_no_unit = float(target_no_unit[0]) * 100
                    target_class = '数值'
                else:
                    target_no_unit = target_no_unit[0]
                    target_class = '数值'
        if str(task_data[3])[:1] in ('>', '≥', '＜', '≤'):
            mark = str(task_data[3])[:1]
        else:
            mark = ''
        # print(unit)
        task_data.append(unit)
        task_data.append(target_no_unit)
        task_data.append(mark)
        task_data.append(target_class)
        print(task_data)
        write_data_indicator(task_data[0], task_data[1], str(task_data[2]).replace('\xa0', ''), task_data[3],
                             task_data[4], task_data[5], task_data[6], task_data[7], task_data[8])
    unit_total = list(set(unit_total))
    for _unit in unit_total:
        write_unit(_unit)
        # new_data.append(task_data)


def write_unit(unit):
    # 将每次执行数据写入到Excel
    # 读取Excel文件，若该Excel已被其他程序打开，则会运行报错
    wb = xlrd.open_workbook(new_file, encoding_override='utf-8',
                            formatting_info=True)
    # copy读取信息
    wt = copy(wb)
    # 获取Excel中第一个sheet
    st = wb.sheet_by_index(3)
    # 在此sheet中寻找数据的最大行数
    max_row = st.nrows
    # 获取复制后读取的Excel文件信息中的第一个sheet
    w = wt.get_sheet(3)
    # 开始写入信息，每次循环最大行数max_row固定
    w.write(max_row, 0, unit)
    # 保存Excel文件
    wt.save('双高任务书提取文件.xls')


def read_amount():
    # 从原表的第三个sheet中解析建设任务的项目资金
    book = xlrd.open_workbook(old_file, formatting_info=True)
    table = book.sheet_by_index(2)
    nrows = table.nrows  # 包括标题
    # 获取总列数
    ncols = table.ncols
    # 计算出合并的单元格有哪些
    colspan = {}
    if table.merged_cells:
        for item in table.merged_cells:
            for row in range(item[0], item[1]):
                for col in range(item[2], item[3]):
                    # 合并单元格的首格是有值的，所以在这里进行了去重
                    if (row, col) != (item[0], item[2]):
                        colspan.update({(row, col): (item[0], item[2])})
    # 读取每行数据
    data = []
    for i in range(1, nrows):
        row = []
        for j in range(ncols):
            # 假如碰见合并的单元格坐标，取合并的首格的值即可
            if colspan.get((i, j)):
                row.append(table.cell_value(*colspan.get((i, j))))
            else:
                # # 第4列第4行开始为末级建设任务
                # if i > 2 and j > 2:
                #     _data = table.cell_value(i, j)
                #     # 将末级建设任务str根据序号拆分成list的末级建设任务
                #     row.append(jx_data(_data))
                # else:
                row.append(table.cell_value(i, j))
        del row[3]
        del row[4]
        del row[5]
        del row[6]
        del row[7]
        del row[8]
        del row[2]
        # print(row)
        if row[1] == '小计':
            pass
        else:
            data.append(row)
    del data[0]
    del data[0]
    del data[0]
    for a_data in data:
        # print(a_data)
        write_data_amount(a_data[0], a_data[1], int(a_data[2]) * 10000, int(a_data[3]) * 10000, int(a_data[4]) * 10000,
                          int(a_data[5]) * 10000, int(a_data[6]) * 10000)


def write_data_indicator(ind1, ind2, ind3, target, task, unit, target_no_unit, mark, target_class):
    # 将每次执行数据写入到Excel
    # 读取Excel文件，若该Excel已被其他程序打开，则会运行报错
    wb = xlrd.open_workbook(new_file, encoding_override='utf-8',
                            formatting_info=True)
    # copy读取信息
    wt = copy(wb)
    # 获取Excel中第一个sheet
    st = wb.sheet_by_index(1)
    # 在此sheet中寻找数据的最大行数
    max_row = st.nrows
    # 获取复制后读取的Excel文件信息中的第一个sheet
    w = wt.get_sheet(1)
    # 开始写入信息，每次循环最大行数max_row固定
    w.write(max_row, 0, ind1)
    w.write(max_row, 1, ind2)
    w.write(max_row, 2, ind3)
    w.write(max_row, 3, target)
    w.write(max_row, 4, task)
    w.write(max_row, 5, unit)
    w.write(max_row, 6, target_no_unit)
    w.write(max_row, 7, mark)
    w.write(max_row, 8, target_class)
    # 保存Excel文件
    wt.save('双高任务书提取文件.xls')


def write_data_amount(task1, task2, zy_amount, df_amount, jb_amount, hy_amount, xx_amount):
    # 将每次执行数据写入到Excel
    # 读取Excel文件，若该Excel已被其他程序打开，则会运行报错
    wb = xlrd.open_workbook(new_file, encoding_override='utf-8',
                            formatting_info=True)
    # copy读取信息
    wt = copy(wb)
    # 获取Excel中第一个sheet
    st = wb.sheet_by_index(2)
    # 在此sheet中寻找数据的最大行数
    max_row = st.nrows
    # 获取复制后读取的Excel文件信息中的第一个sheet
    w = wt.get_sheet(2)
    # 开始写入信息，每次循环最大行数max_row固定
    w.write(max_row, 0, task1)
    w.write(max_row, 1, task2)
    w.write(max_row, 2, zy_amount)
    w.write(max_row, 3, df_amount)
    w.write(max_row, 4, jb_amount)
    w.write(max_row, 5, hy_amount)
    w.write(max_row, 6, xx_amount)
    # 保存Excel文件
    wt.save('双高任务书提取文件.xls')


def jx_data(_data):
    # re.split('a') 表示以a分割，加上r中括号，表示多个符号隔开，加上r小括号，表示保留分隔符
    _list = re.split(r"([%s])" % _symbol, _data)
    # _list = re.split(r"；", _data)
    # 分割后因为第一个①左侧没有值，是空字符串，删掉一个
    del _list[0]
    # 因为通过数字分割，代表三级任务有序号，还需要将分隔符号与建设任务拼接
    # List[0::2]从第一位以2的倍数取，加上a=[1,2,3,4,5,6],a[0::2]=[1,3,5],a[1::2]=[2,4,6]
    # 通过join将奇数位加上偶数位
    _list = ["".join(i) for i in zip(_list[0::2], _list[1::2])]
    return _list


def jx_data_back(_data):
    # jx_data分割时，序号在前面，此方法用于分割符号在后边，不需要拼接数字情况使用
    _list = re.split(r"[%s]" % _symbol, _data)
    # 末尾不一定有句号，所以不确定是否需要删除最后一个元素
    # 假设末尾是句号，而分隔符刚好为句号，则列表最后一个数为空字符串，假设末尾没有符合，则列表最后一个不为空字符
    # 本来可以考虑加个循环体判断最后是否为空字符，但该函数在for循环中调用，性能会降低许多
    # if len(_list) == 0:
    #     del _list[-1]
    # else:
    #     pass
    # print(_list)
    return _list


def write_data_item(task_1, task_2, years, task_3):
    # 将每次执行数据写入到Excel
    # 读取Excel文件，若该Excel已被其他程序打开，则会运行报错
    wb = xlrd.open_workbook(new_file, encoding_override='utf-8',
                            formatting_info=True)
    # copy读取信息
    wt = copy(wb)
    # 获取Excel中第一个sheet
    st = wb.sheet_by_index(0)
    # 在此sheet中寻找数据的最大行数
    max_row = st.nrows
    # 获取复制后读取的Excel文件信息中的第一个sheet
    w = wt.get_sheet(0)
    # 开始写入信息，每次循环最大行数max_row固定
    w.write(max_row, 0, task_1)
    w.write(max_row, 1, task_2)
    w.write(max_row, 2, years)
    w.write(max_row, 3, task_3)
    # 保存Excel文件
    wt.save('双高任务书提取文件.xls')


def write_tow_task(task_2, task_1):
    # 将每次执行数据写入到Excel
    # 读取Excel文件，若该Excel已被其他程序打开，则会运行报错
    wb = xlrd.open_workbook(new_file, encoding_override='utf-8',
                            formatting_info=True)
    # copy读取信息
    wt = copy(wb)
    # 获取Excel中第一个sheet
    st = wb.sheet_by_index(0)
    # 在此sheet中寻找数据的最大行数
    max_row = st.nrows
    # 获取复制后读取的Excel文件信息中的第一个sheet
    w = wt.get_sheet(0)
    # 开始写入信息，每次循环最大行数max_row固定
    w.write(max_row, 1, task_2)
    w.write(max_row, 0, task_1)
    # 保存Excel文件
    wt.save('双高任务书提取文件.xls')


def write_one_task(task_1):
    # 将每次执行数据写入到Excel
    # 读取Excel文件，若该Excel已被其他程序打开，则会运行报错
    wb = xlrd.open_workbook(new_file, encoding_override='utf-8',
                            formatting_info=True)
    # copy读取信息
    wt = copy(wb)
    # 获取Excel中第一个sheet
    st = wb.sheet_by_index(0)
    # 在此sheet中寻找数据的最大行数
    max_row = st.nrows
    # 获取复制后读取的Excel文件信息中的第一个sheet
    w = wt.get_sheet(0)
    # 开始写入信息，每次循环最大行数max_row固定
    w.write(max_row, 0, task_1)
    # 保存Excel文件
    wt.save('双高任务书提取文件.xls')


def read_symbol():
    # 读取分隔符
    if os.path.exists(symbol_file):
        with open(symbol_file, 'r', encoding='utf-8') as f:
            three_symbol = str(f.read())
    else:
        three_symbol = " "
    return three_symbol


if __name__ == "__main__":
    _symbol = read_symbol()
    # if len(_symbol) == 0:
    #     _symbol = "①②③④⑤⑥⑦⑧⑨"
    print("正在开始提取，请稍后,三级任务分隔符为%s" % _symbol)
    # read()
    read_indicator()
    # read_amount()
    print("提取完成，请查看双高任务书提取文件")
