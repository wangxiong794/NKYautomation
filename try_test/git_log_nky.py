import re
import time
import pandas as pd
import xlrd
import xlwt
from git.repo import Repo
from xlutils.copy import copy
from git import Git
import datetime

global code_base


def git_fetch():
    if code_base == "nky":
        code_path = "E:\\nkyworkspace\\nky\\nky"
    elif code_base == "webapp":
        code_path = "E:\\nkyworkspace\\webapp"
    elif code_base == "bureauweb":
        code_path = "E:\\nkyworkspace\\bureauweb"
    elif code_base == "bureau":
        code_path = "E:\\nkyworkspace\\bureau"
    else:
        code_path = "E:\\nkyworkspace\\mobile"
    g = Git(code_path)
    g.fetch()


def get_object(start_date):
    # 此方法用于针对固定的本地代码分支，拉取指定格式的Git_log信息
    if code_base == "nky":
        code_path = "E:\\nkyworkspace\\nky\\nky"
    elif code_base == "webapp":
        code_path = "E:\\nkyworkspace\\webapp"
    elif code_base == "bureauweb":
        code_path = "E:\\nkyworkspace\\bureauweb"
    elif code_base == "bureau":
        code_path = "E:\\nkyworkspace\\bureau"
    else:
        code_path = "E:\\nkyworkspace\\mobile"
    repo = Repo(path=code_path)
    # a=repo.iter_commits("master")
    # repo = repo.git.log("--since='2022-9-15'", "--until='2022-9-16'")
    # 执行git命令，参数用逗号隔开，Git_bash弹窗中 用空格隔开
    """
    # --stat 查看提交历史，并展示摘要内容（摘要会列出修改的文件以及每个文件中修改了多少行）
    # --shortstat 查看提交历史，并显示摘要内容（只是统计并展示修改了多少内容儿不显示具体哪些文件做出了修改）
    # --pretty xxx 该命令可以用来指定使用不同于默认格式的方式展示提交历史，后面的xxx表示具体的取值，取值有：oneline , short , full , fuller 等
    # --pretty=oneline
    # 执行该命令后会把提交历史的 commit 描述以及校验和 显示在同一行，并且省略默认格式下的其他内容
    # -pretty=short
    # 执行该命令后，只是比默认的格式少了Data日期的描述
    # --pretty=full
    # 执行该命令后，与默认的格式相比少了Data日期的描述，但是增加了commit 提交人信息
    # --name-only
    # 仅在默认格式后面展示已经修改的文件
    # 8.2 git log --abbrev-commit
    # 仅显示 SHA-1 的前几个字符，而非全部字符（这个 SHA-1 字符就是指的校验和，我习惯称为commit id），如下图：
    # 8.3 git log --relative-date
    # 以相对当前的时间展示提交历史
    # 8.4 git log --graph
    # 在展示提交历史前面加入简单的ASCII图形，区分每次提交历史
    # 8.5 git log --oneline
    # log后面直接跟 --oneline 时，显示短的 校验和，并与提交描述显示在同一行
    # 8.6 git log --oneline --graph
    # 以树形结构查看短描述和校验值
    # 8.7 git log -- author=用户名
    # 如：git log --author=CnPeng 就会展示出CnPeng这个用户的修改历史 。注意：这里的用户名，是初始化git 时传入的name . 运行效果如下图：
    # 8.8 git log -- commitor=用户名
    # 如：git log --commitor=CnPeng 就会展示出CnPeng这个用户的提交历史。注意：这里的用户名，是初始化git 时传入的name . 效果图参考上面的author图
    # --since=时间 如：git log --since=1days , 表示，展示1天前的提交历史，具体的时间取值，可以有如下格式： xxxdays , xxxweeks ,
    # 2016-11-25 ， 或 2 years 1 day 3 minutes ago
    # 另外，除了可以使用 --since , 也可以使用 -- after , --util , --before ， 取值方式相同
    # 也可以使用如下这种组合模式：
    # git log --pretty="%h - %s" --author=gitster --since="2008-10-01" \ --before="2008-11-01" --no-merges -- t/
    # 上面的组合模式中，%h , %s 是占位符， 详细的占位符以及含义如下：
    # %H 提交对象（commit）的完整哈希字串
    # %h 提交对象的简短哈希字串
    # %T 树对象（tree）的完整哈希字串
    # %t 树对象的简短哈希字串
    # %P 父对象（parent）的完整哈希字串
    # %p 父对象的简短哈希字串
    # %an 作者（author）的名字
    # %ae 作者的电子邮件地址
    # %ad 作者修订日期（可以用 -date= 选项定制格式）
    # %ar 作者修订日期，按多久以前的方式显示
    # %cn 提交者(committer)的名字
    # %ce 提交者的电子邮件地址
    # %cd 提交日期
    # %cr 提交日期，按多久以前的方式显示
    # %s 提交说明
    """
    # --branches 指所有分支 --remotes 指远程分支，为保证数据准确性，拉取最新的代码git fetch 和git pull
    # repo = str(repo.git.log("--since=1days", "--no-merges", "--branches", "--remotes", "--shortstat",
    #                         "--pretty=startLog%an-%cd"))
    repo = str(
        repo.git.log("--since='%s'" % str(start_date) + " 00:00:00", "--until='%s'" % str(start_date) + " 23:59:59",
                     "--no-merges", "--branches", "--remotes", "--shortstat", "--pretty=startLog%an-%cd"))
    # print(repo)
    # 去掉换行符
    repo = repo.replace('\n', '')
    # 由于git.log命名中，故意增加了startLog字符，用于分割提交记录
    repo = repo.split("startLog")
    # 将得到的list去除空字符串，最终得到的结果应该类似如下
    """
    
    repo = ['Mway-Fri Sep 16 14:47:54 2022 +0800 2 files changed, 2 insertions(+), 1 deletion(-)',
            'Mway-Fri Sep 16 09:44:08 2022 +0800 1 file changed, 2 insertions(+)',
            'yeweigang-Fri Sep 16 09:40:30 2022 +0800 1 file changed, 1 insertion(+), 1 deletion(-)',
            'yeweigang-Fri Sep 16 09:36:52 2022 +0800 55 files changed, 3331 insertions(+), 67 deletions(-)',
            'Mway-Thu Sep 15 18:26:38 2022 +0800 2 files changed, 12 deletions(-)']
    """
    repo = [x.strip() for x in repo if x.strip() != '']
    print(repo)
    return repo


def write_data(text, write_date):
    # 此方法用于数据解析，将git拿到的内容，转换成想要的数据并保存
    # 参数格式如下
    test_text = ['Mway-Fri Sep 16 14:47:54 2022 +0800 2 files changed, 2 insertions(+), 1 deletion(-)',
                 'Mway-Fri Sep 16 09:44:08 2022 +0800 1 file changed, 2 insertions(+)',
                 'yeweigang-Fri Sep 16 09:40:30 2022 +0800 1 file changed, 1 insertion(+), 1 deletion(-)',
                 'yeweigang-Fri Sep 16 09:36:52 2022 +0800 55 files changed, 3331 insertions(+), 67 deletions(-)',
                 'Mway-Thu Sep 15 18:26:38 2022 +0800 2 files changed, 12 deletions(-)']
    # 定义三个空列表，用于分别存放提交人、增加行、删除行，方便转换成矩阵视图，方便分组求和计数
    if len(text) == 0:
        print("无提交信息，无需记录表格")
    else:
        null_author = []
        null_add_line = []
        null_del_line = []
        # 将列表数据遍历，解析提交信息
        for text1 in text:
            # 用-拆解信息，取左边部分为提交人
            author = str(re.split("-", text1)[0])

            # 获取提交日期信息，用于存放明细表
            sub_time = str(re.findall("\-(.*?)\+0800", text1)).replace('ybj-', "").replace("[\'", "").replace("\']", "")
            # print(sub_time)
            # 周
            week = str(re.split(" ", sub_time)[0])
            week = translate_week(week)
            # 月
            month = str(re.split(" ", sub_time)[1])
            month_number = translate_month(month)
            # 日
            work_day = str(re.split(" ", sub_time)[2])
            # 时间
            work_time = str(re.split(" ", sub_time)[3])
            # 年
            work_year = str(re.split(" ", sub_time)[4])
            work_date = work_year + "-" + month_number + "-" + work_day
            # 用字符串changed分割字符串，取右侧部分，找到提交信息，如【 2 insertions(+), 1 deletion(-)】
            total_line = str(re.split("changed,", text1)[1])
            # 若提交信息中没有新增行，将字符串构造成 新增0行，方便解析
            if "+" not in total_line:
                total_line = "0 insertions(+)," + total_line
            # 若提交信息中没有删除行，将字符串构造成 删除0行，方便解析
            if "-" not in total_line:
                total_line = total_line + ",0 deletions(-)"
            # 用字符串insert分割【 2 insertions(+), 1 deletion(-)】，取左侧部分，替换空格，得到新增行
            add_line = int(re.split("insert", total_line)[0].replace(" ", ""))

            # 用字符串insert分割【 2 insertions(+), 1 deletion(-)】，取右侧部分，只截取数字部分，得到删除行
            del_line = int(re.findall(r'\d+', re.split("insert", total_line)[1])[0])
            # 单次提交大于5000行的数量，均判断为无效提交，因为代码提交
            if add_line > 5000 or del_line > 5000:
                pass
            else:
                # 将获取到的提交人，添加到总的列表中
                null_author.append(author)
                # 将取到的新增行，添加到列表中
                null_add_line.append(add_line)
                # 将取到的删除行，添加到列表中
                null_del_line.append(del_line)
                # 写入明细表
                write_data_item(code_base, translate_author(author), work_date, week, work_time, add_line, del_line)

        # 将三个列表信息转换到矩阵二维表中，来进行分组求和，数据举例
        # 其中第一列为序号，author为提交者，add_line为新增行，del_line为删除行，数据与test_text一致
        """
              author  add_line  del_line
        0       Mway         2         1
        1       Mway         2         0
        2  yeweigang         1         1
        3  yeweigang      3331        67
        4       Mway         0        12
        """
        df = pd.DataFrame({'author': null_author, "add_line": null_add_line, "del_line": null_del_line})
        # 构造新的矩阵，用于存放提交次数，第一行为标题
        # 与mysql的 select count('add_line') from 表 group by 'author' 类似
        """
        author
        Mway         3
        yeweigang    2
        """
        df1 = df.groupby("author").size()
        # 构造了新的矩阵，用于存放新增行合计，数据举例
        # 与mysql的 select sum('add_line') from 表 group by 'author' 类似
        """
        author
        Mway            4
        yeweigang    3332
        """
        add_lines = df.groupby("author")["add_line"].sum()
        # 构造了新的矩阵，用于存放删除行合计，数据举例
        """
        author
        Mway         13
        yeweigang    68
        """
        del_lines = df.groupby("author")["del_line"].sum()
        # 去重代码提交者
        authors = list(set(null_author))
        for author in authors:
            # 根据提交者去寻找新增行的矩阵中对应新增行
            add_line = int(add_lines[author])
            # 根据提交者去寻找删除行的矩阵中对应删除行
            del_line = int(del_lines[author])
            # 根据提交者去寻找提交次数的矩阵中对应次数
            submit_number = int(df1[author])
            # print(author, submit_number, add_line, del_line)
            # 将得到的数据填写到Excel中
            write_excel(code_base, translate_author(author), submit_number, add_line, del_line, write_date)


def translate_month(_month):
    _data = {
        "Jan": "1", "Feb": "2", "Mar": "3", "Apr": "4", "May": "5", "Jun": "6", "Jul": "7", "Aug": "8", "Sep": "9",
        "Oct": "10", "Nov": "11", "Dec": "12"
    }
    if _month in _data:
        return _data[_month]
    else:
        return _month


def translate_author(_name):
    _data = {
        "bryan": "叶柏军",
        "huanglijie": "黄李洁",
        "lenovo": "lenovo",
        "Mway": "侯明未",
        "nkybj01": "纪向峰",
        "tangting": "唐婷",
        "wumusenlin000": "张森林",
        "yeweigang": "叶伟刚",
        "yingxu.xuying": "徐莹",
        "yingxu.yingxu": "徐莹",
        "ywg": "叶伟刚",
        "1169307736": "侯明未",
        "ShunPing Wang":"王顺平",
        "王顺平":"王顺平"

    }
    if _name in _data:
        return _data[_name]
    else:
        return _name


def translate_week(_week_day):
    _data = {
        'Sun': "星期天",
        'Mon': "星期一",
        'Tue': "星期二",
        'Wed': "星期三",
        'Thu': "星期四",
        'Fri': "星期五",
        'Sat': "星期六"
    }
    if _week_day in _data:
        return _data[_week_day]
    else:
        return _week_day


def write_data_item(code, author, work_date, week, work_time, add_line, del_line,
                    xls_path='code_log.xls'):
    # 将每次执行数据写入到Excel
    # 读取Excel文件，若该Excel已被其他程序打开，则会运行报错
    wb = xlrd.open_workbook('E:\\eclipse\\NKYautomation\\try_test\\code_log.xls', encoding_override='utf-8',
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
    w.write(max_row, 0, code)
    # 因考虑到代码每日运行统计代码提交量，记录执行日期
    w.write(max_row, 1, author)
    w.write(max_row, 2, work_date)
    w.write(max_row, 3, week)
    w.write(max_row, 4, work_time)
    w.write(max_row, 5, add_line)
    w.write(max_row, 6, del_line)
    w.write(max_row, 7, "=WEEKNUM(C%s)" % str(max_row + 1))
    # 保存Excel文件
    wt.save('code_log.xls')


def write_excel(code, author, submit_number, add_line, del_line, write_date, xls_path='code_log.xls'):
    # 将每次执行数据写入到Excel
    # 读取Excel文件，若该Excel已被其他程序打开，则会运行报错
    wb = xlrd.open_workbook('E:\\eclipse\\NKYautomation\\try_test\\code_log.xls', encoding_override='utf-8',
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
    w.write(max_row, 0, code)
    # 因考虑到代码每日运行统计代码提交量，记录执行日期
    # w.write(max_row, 1, time.strftime("%Y-%m-%d %H:%M"))
    w.write(max_row, 1, str(write_date))
    w.write(max_row, 2, author)
    w.write(max_row, 3, submit_number)
    w.write(max_row, 4, add_line)
    w.write(max_row, 5, del_line)
    w.write(max_row, 6, "=WEEKNUM(B%s)" % str(max_row + 1))
    # 保存Excel文件
    wt.save('code_log.xls')


# def os_git():
#     # _dir = os.listdir("E:\\nkyworkspace\\nky")
#     # _dir=os.dir
#     # print(_dir)
#     os.chdir("E:\\nkyworkspace\\nky\\nky")
#     result = os.popen("git log --since=1days").read().strip()
#     # result=os.popen()
#     # a=result.read().encode("urf-8")
#     print(result)

# git log  --since='2022-2-9' --until='2022-3-18' --format='%aN' | sort -u | while read name; do echo -en "$name,"; git log --since='2022-2-9' --until='2022-3-18' --author="$name" --numstat --pretty=tformat: --no-merges | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines, %s, removed lines, %s, total lines, %s\n", add, subs, loc }' -; done >> 2022_2_mobile_code.csv;


if __name__ == "__main__":
    # a = get_object("webapp")
    # write_data(a)
    for code_base in ( "nky","bureau"):
        # code_base = "bureauweb"
        git_fetch()
        begin = datetime.date(2021, 1, 1)
        end = datetime.date(2021, 12, 31)
        for d in range((end - begin).days + 1):
            day = begin + datetime.timedelta(d)
            print(day)
            a = get_object(day)
            write_data(a, day)
