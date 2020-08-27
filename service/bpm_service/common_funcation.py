import json
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
from selenium import webdriver
import logging
import time
import os
from get_root_path import root_dir
# http://39.106.158.149/nky
# dev3 47.93.245.21
from config import common_header
from service.connectmysql import DB

# 123.56.223.19
from service.logger import Log

nky_url = 'http://dev2.neikongyi.com/nky'
username = 'chendongxue'
password = 'nky2018'



class con(object):
    def __init__(self, driver):  # 如果不传driver，就默认这个值
        self.dr = driver.find_element_by_xpath
        self.driver = driver
        # self._ip = "47.93.196.74"

    def driverSetting(self):
        self.driver.implicitly_wait(15)
        self.driver.set_window_size(1680, 1050)

    def login(self):
        self.driver.get(nky_url)
        self.dr("//input[@id='userName']").send_keys(username)
        self.dr("//input[@id='password']").send_keys(password)
        self.dr("//button[@data-test-id='LogInButton']").click()
        time.sleep(5)

    def submit(self):
        time.sleep(0.5)
        self.dr("//span[text()='确认提交']/..").click()
        time.sleep(1)
        self.dr("//span[text()='查看详情']/..").click()

    def agree(self):
        time.sleep(1)
        self.dr("//button[text()='同意']").click()
        time.sleep(1)
        self.dr("//span[text()='确 定']/..").click()

    def void(self):
        time.sleep(0.5)
        self.dr("//div[@class='ant-table-body']/table/tbody/tr[1]/td[3]").click()
        time.sleep(0.5)
        self.dr("//button[text()='更多']").click()
        time.sleep(0.5)
        self.dr("//button[text()='作废']").click()
        time.sleep(0.5)
        self.dr("//span[text()='确 定']/..").click()
        self.driver.refresh()
        time.sleep(1)

    def delBill(self):
        time.sleep(1)
        self.driver.refresh()
        time.sleep(0.5)
        self.dr("//button[text()='更多']").click()
        self.dr("//button[text()='删除']").click()
        time.sleep(0.5)
        self.dr("//span[text()='确 定']/..").click()
        time.sleep(0.5)

    def choice_menu(self, menu1, menu2):
        time.sleep(0.5)
        self.dr('//span[text()="' + menu1 + '"]/..').click()
        time.sleep(0.5)
        self.dr("//a[text()='" + menu2 + "']").click()

    def remark(self, remark="remark"):
        self.dr("//textarea[@id='remark']").send_keys(remark)

    def inView(self):
        # from bill list choice the fist bill into view
        time.sleep(1)
        self.dr("//div[@class='ant-table-body']/table/tbody/tr[1]/td[3]").click()

    def cancel(self):
        time.sleep(0.5)
        self.dr("//button[text()='更多']").click()
        time.sleep(0.1)
        self.dr("//button[text()='撤销申请']").click()
        time.sleep(0.5)
        self.dr("//span[text()='确 认']/..").click()
        self.driver.refresh()

    def refuse(self):
        time.sleep(1)
        self.dr("//button[text()='驳回']").click()
        time.sleep(1)
        self.dr("//span[text()='确 定']/..").click()
        time.sleep(0.1)
        self.dr("//span[text()='确认驳回该单据？']/../../div[2]/button[2]").click()
        time.sleep(1)

    def copyCancelBill(self):
        time.sleep(0.5)
        self.dr("//button[text()='复制单据']").click()

    def copyRefuseBill(self):
        self.inView()
        time.sleep(0.5)
        self.dr("//button[text()='复制单据']").click()

    def operator(self):
        # the first user in the list is the purchase operator by default
        self.dr("//div[@id='operUserId']/div").click()
        time.sleep(0.1)
        self.dr("//input[@id='operUserId']").send_keys(Keys.ENTER)

    def enterDepart(self):
        # from department list choice the fist one
        time.sleep(0.5)
        self.dr("//div[@id='departmentId']/div/div").click()
        time.sleep(0.1)
        self.dr("//input[@id='departmentId']").send_keys(Keys.ENTER)

    def _save(self):
        self.dr("//span[text()='保 存']/..").click()
        time.sleep(0.5)

    def _sure(self):
        time.sleep(0.1)
        self.dr("//span[text()='确 定']/..").click()
        time.sleep(1)

    def _more(self):
        time.sleep(0.3)
        self.dr("//button[text()='更多']").click()
        time.sleep(0.3)

    def _nextPage(self):
        self.dr("//span[text()='下一步']/..").click()

    def nextPage(self):
        return self._nextPage()

    def _choicePath(self, pathName):
        self.dr("//div[@id='billFlowDefineId']/div/div").click()
        time.sleep(0.5)
        self.dr("//li[text()='" + pathName + "']").click()

    def quit(self):
        time.sleep(3)
        self.dr('//*[@id="root"]/div/div/div/div[1]/div/span[3]').click()
        time.sleep(0.1)
        self.dr("//li[text()='退出登录']").click()

    def reLogin(self, userName):
        self.dr("//input[@id='userName']").send_keys(userName)
        self.dr("//input[@id='password']").send_keys(password)
        self.dr("//button[@data-test-id='LogInButton']").click()
        time.sleep(5)

    def choiceBudget(self):
        time.sleep(1)
        l1 = str(
            self.dr("//tbody[@class='ant-table-tbody']/tr[1]/td[1]/div").get_attribute(
                "aria-label"))
        if l1 == "展开行":
            self.dr("//tbody[@class='ant-table-tbody']/tr[1]/td[1]").click()
            time.sleep(0.1)
            self.dr("//tbody[@class='ant-table-tbody']/tr[2]/td[1]").click()
        elif l1 == "关闭行":
            l2 = str(self.dr("//tbody[@class='ant-table-tbody']/tr[2]/td[1]/div").get_attribute(
                "aria-label"))
            if l2 == "展开行":
                self.dr("//tbody[@class='ant-table-tbody']/tr[2]/td[1]").click()
                time.sleep(0.1)
                self.dr("//tbody[@class='ant-table-tbody']/tr[3]/td[1]").click()
            else:
                self.dr("//tbody[@class='ant-table-tbody']/tr[3]/td[1]").click()
                time.sleep(0.1)
                self.dr("//tbody[@class='ant-table-tbody']/tr[4]/td[1]").click()
        else:
            print("预算项层级太深")
        time.sleep(0.5)
        self.dr("//span[text()='下一步']/..").click()

    def choicePath(self, pathName):
        time.sleep(0.5)
        self.dr("//div[@id='billFlowDefineId']/div/div").click()
        time.sleep(0.1)
        self.dr("//li[text()='" + pathName + "']").click()

    def editDescription(self, baName):
        self.dr("//textarea[@id='description']").send_keys(baName + str(time.strftime('%m%d%H%M%S')))

    def _cookie(self):
        return self.driver.get_cookies()

    def gqlBillStatus(self, billId):
        g_url = "http://" + self._ip + "/nky/service/graphql"
        check_bill = {
            "query": "{↵  BudgetApplication(criteriaStr: \"(id =" + billId + ")\") {↵    statusId↵  }↵}↵"
        }
        common_header['cookies'] = self._cookie()
        print(common_header['cookies'])
        gql_check_result = requests.request('POST', g_url, headers=common_header, data=json.dumps(check_bill)).json()
        bill_status = str(gql_check_result['data']['BudgetApplication'][0]['statusId'])
        return bill_status

    def budgetMoney(self, money="500"):
        self.dr("//input[@placeholder='请输入申请金额']").send_keys(money)
        self.dr("//span[text()='下一步']/..").click()
        time.sleep(1)
        self.dr("//span[text()='继续留下']/..").click()

    def assertNkyUrl(self, pageUrl):
        Url = self.driver.current_url
        count = 0
        if count < 5:
            while pageUrl in Url:
                pass
            else:
                time.sleep(1)
                count += 1
        else:
            print("current url error!")

    def nextReviewer(self, rolename):
        reviewName = self.dr("//span[text()='" + rolename + "']/../div/div").text
        # self.choice_menu('单位内控设置', '人员管理')
        userDict = {
            '马化腾': 'mahuateng',
            '马云': 'mayun',
            '李彦宏': 'liyanhong',
            '丁磊': 'dinglei',
            '张小龙': 'zhangxiaolong',
            '张小虎': 'zhangxiaohu',
            '张小军': 'zhangxiaojun',
            '王兴': 'wangxing',
            '王文京': 'wangwenjing',
            '赵小云': 'zhaoxiaoyun',
            '赵小风': 'zhaoxiaofeng',
            '赵小雨': 'zhaoxiaoyu',
            '赵小雷': 'zhaoxiaolei',
            '赵小电': 'zhaoxiaodian',
            '董明珠': 'dongmingzhu',
            '雷军': 'leijun',
            '雷鸣': 'leiming',
            '陈东雪': 'chendongxue'
        }
        useName = userDict[reviewName]
        return useName

    def calendar(self):     # 日历
        time.sleep(0.5)
        self.dr("//td[@class='ant-calendar-cell ant-calendar-today ant-calendar-selected-date']/div").click()
        time.sleep(1)
        self.dr("//td[@class='ant-calendar-cell ant-calendar-today ant-calendar-selected-start-date "
                "ant-calendar-selected-date ant-calendar-selected-day']/div").click()



# log_path = os.path.join(root_dir, "logs")


class caseLog(object):

    def __init__(self, log_path=os.path.join(root_dir, "logs")):

        # 文件的命名
        self.log_path = log_path
        self.logName = os.path.join(self.log_path, '%s.log' % time.strftime('%Y_%m_%d'))

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logName, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


def login_code(driver):
    driver.get(nky_url)
    driver.find_elements(By.XPATH, "//input[@id='userName']")[0].send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element_by_xpath("//button[@data-test-id='LogInButton']").click()
    time.sleep(5)


def submit(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确认提交']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='查看详情']/..").click()


def quit_nky(driver):
    driver.find_element(By.XPATH, "//div[@class='antd-pro-layouts-basic-layout-right']/span[3]").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//li[text()='退出登录']").click()


def login_again(driver):
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='userName']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element_by_xpath("//button[@data-test-id='LogInButton']").click()
    time.sleep(5)


def choice_menu(driver, menu1, menu2):
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[text()="' + menu1 + '"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='" + menu2 + "']").click()


def start_add(driver, button_name):
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='" + button_name + "']/..").click()


def RIsubmit(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='确认提交']/..").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确 认']/..").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='查看详情']/..").click()


def agree(driver):
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='同意']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()


def cancel(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='撤销申请']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确 认']/..").click()


def delete_bill(driver):
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    driver.find_element(By.XPATH, "//button[text()='删除']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    time.sleep(0.5)


def agree_new(driver):
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='同意']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()


def refuse(driver):
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='驳回']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确认驳回该单据？']/../../div[2]/button[2]").click()
    time.sleep(1)


def creatuser(driver):
    creatusername = driver.find_element(By.XPATH, "//div[@id='createdUserId']/div/div/div[1]").text
    return creatusername


def pay_apply_menu(driver):
    driver.find_element(By.XPATH, "//span[text()='支出管理']/..").click()
    driver.find_element(By.XPATH, "//a[text()='经费申请']").click()


def pay_reimburse_menu(driver):
    driver.find_element(By.XPATH, "//span[text()='支出管理']/..").click()
    driver.find_element(By.XPATH, "//a[text()='报销申请']").click()


def choice_item(driver):
    driver.find_element(By.XPATH, "//span[text()='+ 发起申请']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[3]/td[1]/span[2]").click()
    driver.find_element(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[4]/td[1]/label/span[1]/input").click()
    js = 'var q=document.querySelector("#root > div > section > section > main").scrollTo(0,1000)'
    driver.execute_script(js)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button").click()
    time.sleep(1)


def fund_detail(driver):
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[text()='+申请明细']").click()
    # 明细内容
    driver.find_element(By.XPATH, "//div[@class='ant-table-scroll']/div/table/tbody/tr[1]/td[2]/div").click()
    driver.find_element(By.XPATH, "//div[@class='ant-table-scroll']/div/table/tbody/tr[1]/td[2]/div/input").send_keys(
        "明细" + time.strftime('%d%H%M'))
    # 计量单位
    driver.find_element(By.XPATH, "//div[@class='ant-table-scroll']/div/table/tbody/tr[1]/td[2]/div/input").send_keys(
        Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@class='ant-table-scroll']/div/table/tbody/tr[1]/td[3]/div/input").send_keys(
        "份")
    # 数量
    driver.find_element(By.XPATH, "//div[@class='ant-table-scroll']/div/table/tbody/tr[1]/td[3]/div/input").send_keys(
        Keys.ENTER)
    driver.find_element(By.XPATH, "//div[@class='ant-table-scroll']/div/table/tbody/tr[1]/td[4]/div/input").send_keys(
        "1")
    # 单价
    driver.find_element(By.XPATH, "//div[@class='ant-table-scroll']/div/table/tbody/tr[1]/td[4]/div/input").send_keys(
        Keys.ENTER)
    driver.find_element(By.XPATH, "//div[@class='ant-table-scroll']/div/table/tbody/tr[1]/td[5]/div/input").send_keys(
        "10")


def fund_train(driver):  # 在培训经费页面增加培训费
    # 培训费
    driver.find_element(By.XPATH, "//a[text()='培训费']").click()
    # 日历
    driver.find_element(By.XPATH, "//span[@class='ant-calendar-picker-input ant-input']/input[1]").click()
    driver.find_element(By.XPATH, "//div[@class='ant-calendar-range-part ant-calendar-range-left']/div[2]/div["
                                  "2]/table/tbody/tr[2]/td[5]/div").click()
    driver.find_element(By.XPATH, "//div[@class='ant-calendar-range-part ant-calendar-range-left']/div[2]/div["
                                  "2]/table/tbody/tr[2]/td[5]/div").click()
    # 地点
    driver.find_element(By.XPATH, "//div[@id='location']").click()
    driver.find_element(By.XPATH, "//input[@id='location']").send_keys('培训地点' + time.strftime('%D'))
    driver.find_element(By.XPATH, "//input[@id='location']").send_keys(Keys.ENTER)
    time.sleep(1)
    # 住宿费,伙食费，交通费，其他费用
    driver.find_element(By.XPATH, "//input[@id='lodgingFee']").send_keys('80')
    driver.find_element(By.XPATH, "//input[@id='foodFee']").send_keys('100')
    driver.find_element(By.XPATH, "//input[@id='transportFee']").send_keys('100')
    driver.find_element(By.XPATH, "//input[@id='otherFee']").send_keys('100')
    # 参训人数
    driver.find_element(By.XPATH, "//input[@id='trainingNumber']").send_keys("1")
    # 工作人员数
    driver.find_element(By.XPATH, "//input[@id='staffNumber']").send_keys("1")


def fund_travel(driver):  # 填经费页面增加 差旅费
    # 差旅费
    driver.find_element(By.XPATH, "//a[text()='差旅费']").click()
    # 日历
    driver.find_element(By.XPATH, "//span[@class='ant-calendar-picker-input ant-input']/input[1]").click()
    driver.find_element(By.XPATH, "//div[@class='ant-calendar-range-part ant-calendar-range-left']/div[2]/div["
                                  "2]/table/tbody/tr[2]/td[5]/div").click()
    driver.find_element(By.XPATH, "//div[@class='ant-calendar-range-part ant-calendar-range-left']/div[2]/div["
                                  "2]/table/tbody/tr[2]/td[5]/div").click()
    # 出差地点--第一个地区北京
    driver.find_element(By.XPATH, "//input[@id='addressId']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//ul[@class='ant-cascader-menu']/li[1]").click()
    driver.find_element(By.XPATH, "//input[@id='transportFee']").send_keys('100')


def fund_meeting(driver):  # 填经费页面增加  会议费
    # 会议费
    driver.find_element(By.XPATH, "//a[text()='会议费']").click()
    # 日历
    driver.find_element(By.XPATH, "//span[@class='ant-calendar-picker-input ant-input']/input[1]").click()
    driver.find_element(By.XPATH,
                        "//div[@class='ant-calendar-range-part ant-calendar-range-left']/div[2]/div[2]/table/tbody/tr[2]/td[5]/div").click()
    driver.find_element(By.XPATH,
                        "//div[@class='ant-calendar-range-part ant-calendar-range-left']/div[2]/div[2]/table/tbody/tr[2]/td[5]/div").click()
    # 参会人数
    driver.find_element(By.XPATH, "//input[@id='meetingNumber']").send_keys('1')
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='staffNumber']").send_keys("1")
    # 住宿费，伙食费，其他费用
    driver.find_element(By.XPATH, "//input[@id='lodgingFee']").send_keys("100")
    driver.find_element(By.XPATH, "//input[@id='foodFee']").send_keys("100")
    driver.find_element(By.XPATH, "//input[@id='otherFee']").send_keys("100")


def fund_labor(driver):  # 填经费页面加劳务费，labor:劳务
    # 劳务费
    driver.find_element(By.XPATH, "//a[text()='劳务费']").click()
    driver.set_window_size(1366, 768)
    # 新增
    driver.find_element(By.XPATH, "//div[@class='footer-btn___1zl3U']").click()
    # 保存
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[text()='保存']").click()


def choice_fund(driver):
    fund_detail(driver)
    fund_labor(driver)
    a = random.randint(1, 3)
    if a == 1:
        fund_meeting(driver)
    elif a == 2:
        fund_train(driver)
    else:
        fund_travel(driver)
    time.sleep(1)
    js = 'var q=document.querySelector("#root > div > section > section > main").scrollTo(0,0)'
    driver.execute_script(js)
    driver.find_element(By.XPATH, "//input[@placeholder='请输入申请金额']").send_keys('99.99')
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()


def pay_apply_submit(driver):
    pay_apartment = choice_apartment(driver)
    pay_des = pay_apartment + '的经费单' + time.strftime('%F-%H%M%S')
    driver.find_element(By.XPATH, "//textarea").send_keys(pay_des)
    driver.find_element(By.XPATH, "//a[text()='+拟选供应商']").click()
    choice_supplier(driver)
    submit(driver)
    return pay_des


def choice_apartment(driver):  # 选部门
    #     p_department2='return p_department2'
    #     return p_department2
    #     pass
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//div[@id='departmentId']/div/div").click()
    # p_department = ('安全保卫', '人事部', '教导处', '德育处', '教科研', '工会', '财务部')
    # p_department1 = random.sample(p_department, 1)
    # p_department2 = "".join(p_department1)
    # time.sleep(0.5)
    # driver.find_element(By.XPATH, "//li[text()='" + p_department2 + "']").click()
    driver.find_element(By.XPATH, "//input[@id='departmentId']").send_keys(Keys.ENTER)
    # return p_department2


def enter_apartment(driver):  # 输入第一个部门
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@id='departmentId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='departmentId']").send_keys(Keys.ENTER)


def choice_calendar(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//td[@class='ant-calendar-cell ant-calendar-today ant-calendar-selected-date']/div").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//td[@class='ant-calendar-cell ant-calendar-today ant-calendar-selected-start-date "
                                  "ant-calendar-selected-date ant-calendar-selected-day']/div").click()


def choice_path(driver, path_name):
    driver.find_element(By.XPATH, "//div[@id='billFlowDefineId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='" + path_name + "']").click()


def choiceapartment(driver):
    driver.find_element(By.XPATH, "//div[@id='departmentId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='departmentId']").send_keys(Keys.ENTER)


def input_apartment(driver):  # 第一个部门
    # noinspection PyBroadException
    try:
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//div[@id='departmentId']/div/div").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@id='departmentId']").send_keys(Keys.ENTER)
    except Exception:
        print("无部门可选")


def choice_supplier(driver):
    a = str(random.randint(10001, 10003))
    driver.find_element(By.XPATH, "//tr[@data-row-key='" + a + "']/td[1]/span/label/span/input").click()
    driver.find_element(By.XPATH, "//span[text()='确认选择']/..").click()


def pay_find(driver, pay_des):
    driver.find_element(By.XPATH, "//div[text()='展开']").click()
    driver.find_element(By.XPATH, "//i[@aria-label='图标: close-circle']").click()
    driver.find_element(By.XPATH, "//input[@id='事由']").send_keys(pay_des)
    driver.find_element(By.XPATH, "//span[text()='查 询']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div").click()


def purchase_edit(driver):
    driver.find_element(By.XPATH, "//span[text()='申请采购']/..").click()
    js = 'var q=document.querySelector("#root > div > section > section > main").scrollTo(0,1000)'
    driver.execute_script(js)
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='选供应商']/..").click()
    choice_supplier(driver)
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='确认提交']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='确 认']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='查看详情']/..").click()
    agree(driver)


def choice_contractPurchaseCatalog(driver):  # 采购类型
    driver.find_element(By.XPATH, "//div[@id='contractPurchaseCatalogId']/div/div").click()
    ct_catalog = ('货物类 ', '工程类', '服务类')
    ct_catalog1 = random.sample(ct_catalog, 1)
    ct_catalog2 = "".join(ct_catalog1)
    time.sleep(1)
    driver.find_element(By.XPATH, "//li[text()='" + ct_catalog2 + "']").click()


def choice_contractType(driver):
    driver.find_element(By.XPATH, "//div[@id='contractTypeId']/div/div").click()
    ct_type = (
        '财产租赁合同', '仓储保管合同', '加工承揽合同', '建设工程勘察设计合同', '货物运输合同', '产权转移合同', '营业资金帐薄', '购销合同', '建筑安装工程承包合同', '技术合同', '借款合同',
        '财产保险合同', '零印花税合同')
    ct_type1 = random.sample(ct_type, 1)
    ct_type2 = "".join(ct_type1)
    time.sleep(1)
    driver.find_element(By.XPATH, "//li[text()='" + ct_type2 + "']").click()


def contract_edit(driver, contract_name):
    driver.find_element(By.XPATH, "//span[text()='申请合同']/..").click()
    driver.find_element_by_xpath("//input[@id='bSupplierName']/../span/button").click()
    choice_supplier(driver)
    choice_contractPurchaseCatalog(driver)
    choice_contractType(driver)
    driver.find_element_by_xpath("//input[@id='name']").send_keys(contract_name)
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys(contract_name)
    driver.find_element(By.XPATH, "//div[@class='normal___3yB_h']/div[3]/div[3]/div/div/div[2]/div/button").click()
    money = driver.find_element(By.XPATH,
                                "//label[text()='可用金额']/../../div[2]/div/span/div/div[2]/input").get_attribute("value")
    driver.find_element_by_xpath("//input[@id='amount_1']").send_keys(money)
    submit(driver)
    agree(driver)


def reimburse_edit(driver):
    driver.find_element(By.XPATH, "//span[text()='+ 发起报销']/..").click()
    driver.find_element(By.XPATH, "//div[@class='ant-tabs-nav ant-tabs-nav-animated']/div[1]/div[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@class='ant-spin-container']/div[1]/ul/li").click()
    submit(driver)
    agree(driver)


def pay_check(driver):
    driver.find_element(By.XPATH, "//span[text()='资金领用']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='payeeBankAccount']").click()
    driver.find_element(By.XPATH, "//div[@id='checkOwnerId']/div/div").click()
    a = str(random.randint(1, 10))
    driver.find_element(By.XPATH, "//ul[@role='listbox']/li[" + a + "]").click()
    driver.find_element(By.XPATH, "//span[text()='确认领用']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='核销预算']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='确认核销']/..").click()
    time.sleep(1)


def choice_liucheng(driver, liucheng):
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@id='billFlowDefineId']/div/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//li[text()='" + liucheng + "']").click()


def all_main(driver):
    pay_apply_menu(driver)
    choice_item(driver)
    choice_fund(driver)
    pay_des = pay_apply_submit(driver)
    agree(driver)

    pay_apply_menu(driver)
    pay_find(driver, pay_des)
    purchase_edit(driver)

    pay_apply_menu(driver)
    time.sleep(1)
    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div").click()
    contract_edit(driver, pay_des)

    pay_reimburse_menu(driver)
    reimburse_edit(driver)
    pay_find(driver, pay_des)
    pay_check(driver)


def enter_ct_type(driver):  # 选第一个合同类型
    driver.find_element(By.XPATH, "//div[@id='contractTypeId']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='contractTypeId']").send_keys(Keys.ENTER)


def enter_b_supplier(driver):  # 乙方选第一个供应商
    driver.find_element(By.XPATH, "//div[@id='bSupplierId']/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//tr[@data-row-key='10000']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    time.sleep(0.1)
    # driver.find_element(By.XPATH, "//input[@id='bSupplierId']").send_keys(Keys.ENTER)


def enter_sign_user(driver):  # 签订人选第一条
    driver.find_element(By.XPATH, "//div[@id='signUsers']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='signUsers']").send_keys(Keys.ENTER)


def ag_enter_sign_user(driver):  # 协议与合同不一样
    driver.find_element(By.XPATH, "//div[@id='signUserId']/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//input[@id='signUserId']").send_keys(Keys.ENTER)


def enter_pc_type(driver):  # 采购类型选第一个
    driver.find_element(By.XPATH, "//div[@id='contractPurchaseCatalogId']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='contractPurchaseCatalogId']").send_keys(Keys.ENTER)


def invalid(driver):  # 作废
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='作废']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    time.sleep(1)


if __name__ == '__main__':
    # br = webdriver.Chrome()
    # br.maximize_window()
    # br.implicitly_wait(15)
    # c = con(br)
    # c.login()
    c = con()
    a= c.budgetAvailable()
    print(a)