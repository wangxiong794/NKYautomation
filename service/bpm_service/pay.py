"""支出管理"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from service.bpm_service import common_funcation
from service.bpm_service.common_funcation import choice_apartment, submit, agree, RIsubmit, enter_apartment, \
    choice_path, invalid, \
    cancel, choice_menu, delete_bill, refuse, choice_calendar, con
from selenium.webdriver.common.keys import Keys
import random
import datetime

date_now = time.strftime("%Ya%mb%dc", time.localtime()).replace('a', "年").replace('b', '月').replace('c', '日')


def choice_BA(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//span[text()="支出管理"]/..').click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[text()='事前申请']").click()
    time.sleep(0.1)


def start_BA(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='+ 发起申请']/..").click()


def choice_budget(driver):  # 选预算项
    time.sleep(1)
    l1 = str(
        driver.find_element(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[1]/td[1]/div").get_attribute("aria-label"))
    if l1 == "展开行":
        driver.find_element(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[1]/td[1]").click()
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[2]/td[1]").click()
    elif l1 == "关闭行":
        l2 = str(driver.find_element(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[2]/td[1]/div").get_attribute(
            "aria-label"))
        time.sleep(0.5)
        if l2 == "展开行":
            driver.find_element(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[2]/td[1]").click()
            time.sleep(0.1)
            driver.find_element(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[3]/td[1]").click()
        elif l2 == "关闭行":
            driver.find_element(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[3]/td[1]").click()
            time.sleep(0.1)
            driver.find_element(By.XPATH, "//tbody[@class='ant-table-tbody']/tr[4]/td[1]").click()
        else:
            print("预算项层级太深,暂不支持")
    else:
        print("预算项层级太深，暂不支持")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()


def edit_money(driver, money):  # 这是事前
    driver.find_element(By.XPATH, "//input[@placeholder='请输入申请金额']").send_keys(money)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='继续留下']/..").click()


def edit_money1(driver, money):  # 这是报销
    driver.find_element(By.XPATH, "//input[@placeholder='请输入报销金额']").send_keys(money)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    time.sleep(1)


def edit_matter(driver, ba_name):
    ba_matter = ba_name + str(time.strftime('%m%d%H%M%S'))
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys(ba_matter)


def edit_matter1(driver, ba_name):
    ba_matter = ba_name + str(time.strftime('%m%d%H%M%S'))
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys(ba_matter)


def pay_setting(driver):
    # 需要先判断是否开启多支付明细，默认不开启
    driver.find_element(By.XPATH, "//div[@id='paySettingId_0']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='paySettingId_0']").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@id='payeeFullName_0']/div/div/ul/li/div/input").send_keys(
        "单位" + str(time.strftime('%m%d%H%M%S')))


def train(driver):  # 增加培训费
    # 培训费
    driver.find_element(By.XPATH, "//button[@testid='2']").click()
    # 培训名称
    driver.find_element(By.XPATH, "//input[@id='trainingFeeName']").send_keys('培训费test')
    # 日历
    driver.find_element(By.XPATH, "//span[@id='date']/span/input[1]").click()
    time.sleep(0.5)
    choice_calendar(driver)
    # 地点
    driver.find_element(By.XPATH, "//input[@id='location']").send_keys('培训地点' + time.strftime('%m%d%H%M%S'))
    # 培训类别
    driver.find_element(By.XPATH, "//div[@id='trainingTypeId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='一类培训']").click()
    time.sleep(1)
    # 参训人数
    driver.find_element(By.XPATH, "//input[@id='trainingNumber']").send_keys("1")
    # 工作人员数
    driver.find_element(By.XPATH, "//input[@id='staffNumber']").send_keys("0")
    driver.find_element(By.XPATH, "//input[@id='teacherNumber']").send_keys('1')
    train_form(driver)
    js = 'var q = document.querySelector("#globalLayoutContent").scrollTo(0,-1000)'
    driver.execute_script(js)
    edit_money(driver, '950')


def train_form(driver):
    driver.find_element(By.XPATH, "//td[@id='0_Number']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='0_Number']/div/div/div/div[2]/input").send_keys('1')
    driver.find_element(By.XPATH, "//td[@id='0_Days']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='0_Days']/div/div/div/div[2]/input").send_keys('1')
    driver.find_element(By.XPATH, "//td[@id='0_Remark']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='0_Remark']/div/div/input").send_keys('住宿费')
    driver.find_element(By.XPATH, "//td[@id='1_Number']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='1_Number']/div/div/div/div[2]/input").send_keys('1')
    driver.find_element(By.XPATH, "//td[@id='1_Days']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='1_Days']/div/div/div/div[2]/input").send_keys('1')
    driver.find_element(By.XPATH, "//td[@id='1_Remark']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='1_Remark']/div/div/input").send_keys('伙食费')
    driver.find_element(By.XPATH, "//td[@id='2_Number']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='2_Number']/div/div/div/div[2]/input").send_keys('1')
    driver.find_element(By.XPATH, "//td[@id='2_Days']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='2_Days']/div/div/div/div[2]/input").send_keys('1')
    driver.find_element(By.XPATH, "//td[@id='2_Remark']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='2_Remark']/div/div/input").send_keys('场地/资料/交通费')
    driver.find_element(By.XPATH, "//td[@id='3_Number']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='3_Number']/div/div/div/div[2]/input").send_keys('1')
    driver.find_element(By.XPATH, "//td[@id='3_Days']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='3_Days']/div/div/div/div[2]/input").send_keys('1')
    driver.find_element(By.XPATH, "//td[@id='3_Remark']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='3_Remark']/div/div/input").send_keys('其他费用')
    driver.find_element(By.XPATH, "//td[@id='4_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='4_Amount']/div/div/div/div[2]/input").send_keys('100')
    driver.find_element(By.XPATH, "//td[@id='4_Remark']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='4_Remark']/div/div/input").send_keys('讲课费(税后总额)')
    driver.find_element(By.XPATH, "//td[@id='5_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='5_Amount']/div/div/div/div[2]/input").send_keys('100')
    driver.find_element(By.XPATH, "//td[@id='5_Remark']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='5_Remark']/div/div/input").send_keys('个人所得税(总额)')
    driver.find_element(By.XPATH, "//td[@id='6_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='6_Amount']/div/div/div/div[2]/input").send_keys('100')
    driver.find_element(By.XPATH, "//td[@id='6_Remark']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='6_Remark']/div/div/input").send_keys('城市间交通费(总额)')


def travel(driver):  # 差旅费测算
    # 差旅费
    driver.find_element(By.XPATH, "//button[@testid='1']").click()
    # 日历
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@title='出差时间']/../div[3]/div/div/div/span/span/span/input[1]").click()
    choice_calendar(driver)

    # 出差地点--第一个地区北京
    driver.find_element(By.XPATH, "//div[@title='出差地点']/../div[3]/div/div/div/span/span").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//li[text()='北京']").click()
    time.sleep(0.1)
    # driver.find_element(By.XPATH, "//li[text()='北京（全市）']").click()
    # driver.find_element(By.XPATH, "//div[@title='交通工具']/../div[3]/div/div/div/span/div").click()
    # time.sleep(0.1)
    # driver.find_element(By.XPATH, "//li[text()='飞机']").click()
    # driver.find_element(By.XPATH, "//div[@title='城市间交通费']/../div[3]/div/div/div/span/div/div[2]/input").click()
    driver.find_element(By.XPATH, "//div[@title='城市间交通费']/../div[3]/div/div/div/span/div/div[2]/input").send_keys(20)
    edit_money(driver, "200")


def travel_form(driver):
    driver.find_element(By.XPATH, "//td[@id='0_Number']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='0_Number']/div/div/div/div[2]/input").send_keys('1')
    driver.find_element(By.XPATH, "//td[@id='0_Days']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='0_Days']/div/div/div/div[2]/input").send_keys('1')
    driver.find_element(By.XPATH, "//td[@id='0_Remark']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='0_Remark']/div/div/input").send_keys('住宿费')
    driver.find_element(By.XPATH, "//td[@id='1_Number']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='1_Number']/div/div/div/div[2]/input").send_keys('1')
    driver.find_element(By.XPATH, "//td[@id='1_Days']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='1_Days']/div/div/div/div[2]/input").send_keys('1')
    driver.find_element(By.XPATH, "//td[@id='1_Remark']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='1_Remark']/div/div/input").send_keys('伙食费')
    driver.find_element(By.XPATH, "//td[@id='2_Number']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='2_Number']/div/div/div/div[2]/input").send_keys('1')
    driver.find_element(By.XPATH, "//td[@id='2_Days']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='2_Days']/div/div/div/div[2]/input").send_keys('1')
    driver.find_element(By.XPATH, "//td[@id='2_Remark']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='2_Remark']/div/div/input").send_keys('其他费用')
    driver.find_element(By.XPATH, "//td[@id='3_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='3_Amount']/div/div/div/div[2]/input").send_keys('20')
    driver.find_element(By.XPATH, "//td[@id='3_Remark']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='3_Remark']/div/div/input").send_keys('会议场地租金')
    driver.find_element(By.XPATH, "//td[@id='4_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='4_Amount']/div/div/div/div[2]/input").send_keys('20')
    driver.find_element(By.XPATH, "//td[@id='4_Remark']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='4_Remark']/div/div/input").send_keys('交通费')
    driver.find_element(By.XPATH, "//td[@id='5_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='5_Amount']/div/div/div/div[2]/input").send_keys('20')
    driver.find_element(By.XPATH, "//td[@id='5_Remark']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='5_Remark']/div/div/input").send_keys('文件印刷费')
    driver.find_element(By.XPATH, "//td[@id='6_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='6_Amount']/div/div/div/div[2]/input").send_keys('20')
    driver.find_element(By.XPATH, "//td[@id='6_Remark']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='6_Remark']/div/div/input").send_keys('医药费')
    driver.find_element(By.XPATH, "//td[@id='7_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='7_Amount']/div/div/div/div[2]/input").send_keys('20')
    driver.find_element(By.XPATH, "//td[@id='7_Remark']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='7_Remark']/div/div/input").send_keys('其他')


def meeting(driver):  # 会议费测算
    # 会议费
    driver.find_element(By.XPATH, "//button[@testid='3']").click()
    driver.find_element(By.XPATH, "//input[@id='meetingName']").send_keys('会议一')
    driver.find_element(By.XPATH, "//span[@id='dateRange']/span/input[1]").click()
    choice_calendar(driver)
    # 参会人数
    driver.find_element(By.XPATH, "//input[@id='meetingAddress']").send_keys('地点一')
    driver.find_element(By.XPATH, "//div[@id='meetingLevelId']/div/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//li[text()='一类会议']").click()

    driver.find_element(By.XPATH, "//input[@id='meetingNumber']").send_keys('1')
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='staffNumber']").send_keys("1")
    travel_form(driver)
    js = 'var q = document.querySelector("#globalLayoutContent").scrollTo(0,-1000)'
    driver.execute_script(js)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    edit_money(driver, '650')


def labor(driver):  # 填经费页面加劳务费，labor:劳务
    # 劳务费
    driver.find_element(By.XPATH, "//button[@testid='4']").click()
    # 新增
    time.sleep(0.5)
    edit_money(driver, '500')


def start_BA_RI0(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='+ 事前申请报销']/..").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@class='ant-spin-container']/ul/li[1]/ul/li/a").click()


def edit_BA_RI(driver, ba_ri_des):
    time.sleep(1)
    # 选流程
    driver.find_element(By.XPATH, "//div[@id='billFlowDefineId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='报销申请单自审']").click()
    # 选择支付方式
    choice_paymethod(driver)
    # 选择收款单位
    driver.find_element(By.XPATH, "//div[@id='payee']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@id='payee']/div/div/ul/li/div/input").send_keys('随意增加')
    driver.find_element(By.XPATH, "//div[@id='payee']/div/div/ul/li/div/input").send_keys(Keys.ENTER)
    # 重新编辑事由
    driver.find_element(By.XPATH, "//textarea").clear()
    driver.find_element(By.XPATH, "//textarea").send_keys(ba_ri_des + str(time.time()))


def BA_RI(driver):
    choice_RI(driver)  # 选菜单
    start_BA_RI(driver)  # 选择经费单报销
    edit_BA_RI(driver, '经费报销')
    RIsubmit(driver)
    agree(driver)


def choice_RI(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[text()="支出管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='报销申请']").click()


def start_NORI(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='+ 无申请报销']/..").click()


def start_AGRI(driver):
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='+ 事前申请报销']/..").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[text()='框架协议']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='globalLayoutContent']/div/div[2]/div/div/div/div/div/div/div/div/div["
                                  "2]/div/div/table/tbody/tr[1]/td/a").click()


def choice_paymethod(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//div[@id='paySettingId']/div/div").click()
    paymethod = ('支票', '现金', '财政统发', '其他')
    paymethod = random.sample(paymethod, 1)
    paymethod = "".join(paymethod)
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='" + paymethod + "']").click()


def company(driver):
    driver.find_element(By.XPATH, "//input[@id='payee']").send_keys('付款单位')


def BA_recopy(driver):  # 复制单据，先撤销再驳回，最后再作废
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='撤销申请']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='确 认']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='复制单据']").click()
    submit(driver)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='驳回']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确认驳回该单据？']/../../div[2]/button[2]").click()
    time.sleep(1)
    choice_BA(driver)
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]/td[1]/div").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='复制单据']").click()
    driver.find_element(By.XPATH, "//textarea[@id='description']").clear()
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys("作废" + str(time.strftime('%m%d%H%M%S')))
    submit(driver)
    agree(driver)
    time.sleep(1)
    choice_BA(driver)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]/td[1]/div").click()
    time.sleep(1)
    invalid(driver)


def official(driver):  # 接待费标准测算
    driver.find_element(By.XPATH, "//button[@testid='5']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//input[@id='guestUnit']").send_keys("单位" + str(time.strftime('%m%d%H%M%S')))
    driver.find_element(By.XPATH, "//input[@id='guestLeaderName']").send_keys("领队" + str(time.strftime('%m%d%H%M%S')))
    driver.find_element(By.XPATH, "//div[@id='staffRankId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='staffRankId']").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//span[@id='receptionDate']").click()
    time.sleep(1)
    time.sleep(0.5)
    choice_calendar(driver)
    driver.find_element(By.XPATH, "//input[@id='receptionNumber']").send_keys(1)
    driver.find_element(By.XPATH, "//input[@id='guestNumber']").send_keys(1)
    driver.find_element(By.XPATH, "//input[@id='accompanyNumber']").send_keys(1)
    driver.find_element(By.XPATH, "//input[@id='otherCost']").send_keys(100)
    driver.find_element(By.XPATH, '//input[@placeholder="请输入申请金额"]').send_keys(500)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='继续留下']/..").click()


def start_BA_RI(driver):
    choice_BA(driver)
    time.sleep(0.1)
    driver.refresh()
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]/td[1]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='发起报销']").click()


def start_IM_RI(driver):
    choice_menu(driver, "支出管理", "预付申请")
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//button[text()='发起报销']").click()


def RI_official(driver):
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='officialLetter']").send_keys('接待公函')
    time.sleep(0.2)
    driver.find_element(By.XPATH, "//input[@id='guestName_0']").send_keys('对象1')
    driver.find_element(By.XPATH, "//input[@id='guestUnit_0']").send_keys('单位1')
    driver.find_element(By.XPATH, "//div[@id='staffRankId_0']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='staffRankId_0']").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//div[@id='guestNameAccompany_0']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@id='guestNameAccompany_0']/div/div/ul/li/div/input").send_keys('陪玩1')
    driver.find_element(By.XPATH, "//div[@id='staffRankIdAccompany_0']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='staffRankIdAccompany_0']").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//input[@id='guestUnitAccompany_0']").send_keys('test')
    # 工作餐
    js = 'var q =document.querySelector("#globalLayoutContent").scrollTo(0,1000)'
    driver.execute_script(js)
    work_food_path = "//div[text()='工作餐']/../div[2]/div/div/div/div/div/div[1]/div/table/tbody/tr"
    driver.find_element(By.XPATH, work_food_path + "/td[2]/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//a[text()='今天']").click()
    driver.find_element(By.XPATH, work_food_path + "/td[3]/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, work_food_path + "/td[3]/div/div/input").send_keys('场所1')
    driver.find_element(By.XPATH, work_food_path + "/td[6]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, work_food_path + "/td[6]/div/div/div/div[2]/input").send_keys('360')

    # 交通费用
    transport_path = "//div[text()='工作餐']/../div[4]/div/div/div/div/div/div[1]/div/table/tbody/tr"
    driver.find_element(By.XPATH, transport_path + "/td[2]/div").click()
    time.sleep(0.1)
    # /html/body/div[7]/div/div/div/div/div[2]/div[3]/span/a
    driver.find_element(By.XPATH, "//a[text()='今天']").click()
    driver.find_element(By.XPATH, transport_path + "/td[3]/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, transport_path + "/td[3]/div/div/input").send_keys('交通项目1')
    driver.find_element(By.XPATH, transport_path + "/td[4]/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, transport_path + "/td[4]/div/div/input").send_keys('1')
    driver.find_element(By.XPATH, transport_path + "/td[5]/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, transport_path + "/td[5]/div/div/input").send_keys('路线1')
    driver.find_element(By.XPATH, transport_path + "/td[6]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, transport_path + "/td[6]/div/div/div/div[2]/input").send_keys('100')
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()


def RI_train(driver):  # 有培训费测算时发起报销
    time.sleep(0.5)
    js = 'var q = document.querySelector("#globalLayoutContent").scrollTo(0,1000)'
    driver.execute_script(js)
    driver.find_element(By.XPATH, "//td[@id='0_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='0_Amount']/div/div/div/div[2]/input").send_keys('400')
    driver.find_element(By.XPATH, "//td[@id='1_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='1_Amount']/div/div/div/div[2]/input").send_keys('150')
    driver.find_element(By.XPATH, "//td[@id='2_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='2_Amount']/div/div/div/div[2]/input").send_keys('70')
    driver.find_element(By.XPATH, "//td[@id='3_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='3_Amount']/div/div/div/div[2]/input").send_keys('30')
    driver.find_element(By.XPATH, "//td[@id='4_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='4_Amount']/div/div/div/div[2]/input").send_keys('100')
    driver.find_element(By.XPATH, "//td[@id='5_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='5_Amount']/div/div/div/div[2]/input").send_keys('100')
    driver.find_element(By.XPATH, "//td[@id='6_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='6_Amount']/div/div/div/div[2]/input").send_keys('100')


def RI_meeting(driver):  # 会议费报销
    time.sleep(0.5)
    time.sleep(0.5)
    js = 'var q = document.querySelector("#globalLayoutContent").scrollTo(0,1000)'
    driver.execute_script(js)
    driver.find_element(By.XPATH, "//td[@id='0_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='0_Amount']/div/div/div/div[2]/input").send_keys('400')
    driver.find_element(By.XPATH, "//td[@id='1_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='1_Amount']/div/div/div/div[2]/input").send_keys('150')
    driver.find_element(By.XPATH, "//td[@id='2_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='2_Amount']/div/div/div/div[2]/input").send_keys('100')
    driver.find_element(By.XPATH, "//td[@id='3_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='3_Amount']/div/div/div/div[2]/input").send_keys('20')
    driver.find_element(By.XPATH, "//td[@id='4_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='4_Amount']/div/div/div/div[2]/input").send_keys('20')
    driver.find_element(By.XPATH, "//td[@id='5_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='5_Amount']/div/div/div/div[2]/input").send_keys('20')
    driver.find_element(By.XPATH, "//td[@id='6_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='6_Amount']/div/div/div/div[2]/input").send_keys('20')
    driver.find_element(By.XPATH, "//td[@id='7_Amount']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='7_Amount']/div/div/div/div[2]/input").send_keys('20')
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    time.sleep(1)


def RI_travel(driver):  # 差旅费报销
    time.sleep(0.5)
    # 系统内人员
    driver.find_element(By.XPATH, "//div[@id='travelSystemUsers_0']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='travelSystemUsers_0']").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//div[@id='trafficToolStr_0']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='trafficToolStr_0']").send_keys(Keys.ENTER)
    #   费用明细
    js = 'var q=document.querySelector("#globalLayoutContent").scrollTo(0,10000)'
    driver.execute_script(js)
    driver.find_element(By.XPATH, "//input[@id='transportFeeAmount_0']").send_keys('20')
    driver.find_element(By.XPATH, "//input[@id='busFeeAmount_0']").send_keys('80')
    driver.find_element(By.XPATH, "//input[@id='lodgingFeeAmount_0']").send_keys('0')
    driver.find_element(By.XPATH, "//input[@id='foodFeeAmount_0']").send_keys('100')
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    time.sleep(1)


def RI_labor(driver):  # 劳务费报销
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[@testid='labor']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//div[@class='reimburse-labor-to-view']/div/div[2]/div/section["
                                  "2]/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr/td[2]/div").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@placeholder='请输入专家姓名']").send_keys('叶安世')
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//td[text()='叶安世']/..").click()
    time.sleep(0.2)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    time.sleep(0.5)
    # 劳务分类
    driver.find_element(By.XPATH, "//div[@class='reimburse-labor-to-view']/div/div[2]/div/section["
                                  "2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[3]/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='专家劳务']").click()
    # 税后实发单价
    # driver.find_element(By.XPATH, "//div[@class='reimburse-labor-to-view']/div/div[2]/div/section["
    #                               "2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[6]/div").click()
    # time.sleep(0.1)
    # driver.find_element(By.XPATH, "//div[@class='reimburse-labor-to-view']/div/div[2]/div/section["
    #                               "2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[6]/div/div/div["
    #                               "2]/input").send_keys('500')
    # 数量
    js = 'var q=document.querySelector("#globalLayoutContent > div > div.reimburse-labor-to-view > div > ' \
         'div.antd-pro-components-v2-card-view-card-wrapper > div > section:nth-child(2) > div > div > div > div > ' \
         'div > div > div.ant-table-scroll > div").scrollTo(400,0) '
    driver.execute_script(js)
    time.sleep(0.5)
    # //div[@class='reimburse-labor-to-view']/div/div[2]/div/section[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[8]/div"
    driver.find_element(By.XPATH, "//td[@id='0_hours']/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//td[@id='0_hours']/div/div/div/div[2]/input").send_keys('1')
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    time.sleep(1)


def capital_access(driver):  # 资金领用
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    driver.find_element(By.XPATH, "//button[text()='资金领用']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@id='checkOwnerId']/div/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//input[@id='checkOwnerId']").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//div[@id='checkNumber']/div").click()
    time.sleep(0.5)
    check_number = '支票号' + time.strftime('%m%d%H%M%S')
    driver.find_element(By.XPATH, "//input[@id='checkNumber']").send_keys(check_number)
    driver.find_element(By.XPATH, "//li[text()='" + check_number + "']").click()
    driver.find_element(By.XPATH, "//span[text()='确认领用']/..").click()


def write_off(driver):  # 核销
    choice_RI(driver)
    driver.refresh()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]").click()
    time.sleep(1)
    capital_access(driver)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    driver.find_element(By.XPATH, "//button[text()='经费核销']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()


def add_im0(driver):  # 从列表上新增预付单
    time.sleep(0.1)
    choice_menu(driver, '支出管理', '预付申请')
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='+ 发起预付']/..").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a").click()


def add_im1(driver):  # 从事前单详情页上新增预付单
    time.sleep(0.1)
    choice_menu(driver, '支出管理', '事前申请')
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//tbody/tr[1]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='发起预付']").click()


def edit_im(driver, im_name):
    time.sleep(0.5)
    enter_apartment(driver)
    choice_path(driver, "预付申请单自审")
    driver.find_element(By.XPATH, "//div[@id='paySettingId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='paySettingId']").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@id='payeeFullName']/div/div/ul/li/div/input").send_keys(
        "单位" + str(time.strftime('%m%d%H%M%S')))
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys(im_name)


def apply_detail(driver):  # 输入产品或资产
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[@testid='applyDetails']").click()
    time.sleep(0.5)
    # 明细内容
    driver.find_element(By.XPATH, "//td[@id='0_name']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='0_name']/div/div/input").send_keys('明细' + time.strftime('%m%d%H%M%S'))
    # 型号
    driver.find_element(By.XPATH, "//td[@id='0_specification']/div").click()

    driver.find_element(By.XPATH, "//td[@id='0_specification']/div/div/input").send_keys('型号' + time.strftime('%H%M%S'))
    # 计量单位
    driver.find_element(By.XPATH, "//td[@id='0_unitId']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='支']").click()
    # 数量
    driver.find_element(By.XPATH, "//td[@id='0_quantity']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='0_quantity']/div/div/div/div[2]/input").send_keys('2')
    js = 'var q=document.querySelector("#applyEdit_fee_applyDetails > div.antd-pro-components-v2-card-card-card > ' \
         'div:nth-child(3) > div > div > div > div > div > div.ant-table-scroll > div").scrollTo(1000,0) '
    driver.execute_script(js)
    time.sleep(0.1)
    # 单价
    driver.find_element(By.XPATH, "//td[@id='0_price']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='0_price']/div/div/div/div[2]/input").send_keys('100')
    # 推荐供应商
    driver.find_element(By.XPATH, "//td[@id='0_supplierId']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='0_supplierId']/div/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
    # 政采目录
    driver.find_element(By.XPATH, "//td[@id='0_governmentPurchaseCatalogueId']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,
                        "//td[@id='0_governmentPurchaseCatalogueId']/div/div/div/div/div/div/div/input").send_keys(
        Keys.ENTER)
    # 备注
    driver.find_element(By.XPATH, "//td[@id='0_description']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='0_description']/div/div/input").send_keys(
        '备注' + time.strftime('%m%d%H%M%S'))


def choice_apply_detail(driver):  # 选择产品或者明细，需要准备两条产品信息，台式机与卷纸
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[@testid='applyDetails']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//td[@id='0_name']/div/i").click()
    time.sleep(1)
    # 直接选产品编码为1与2，且为常用
    driver.find_element(By.XPATH, "//tr[@data-row-key='10000']").click()
    driver.find_element(By.XPATH, "//tr[@data-row-key='10001']").click()
    # driver.find_element(By.XPATH, "//td[text()='2']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    # 数量
    driver.find_element(By.XPATH, "//td[@id='0_quantity']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='0_quantity']/div/div/div/div[2]/input").send_keys('2')
    driver.find_element(By.XPATH, "//td[@id='1_quantity']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='1_quantity']/div/div/div/div[2]/input").send_keys('2')


def is_purchase(driver):
    driver.find_element(By.XPATH, "//div[@id='isPurchase']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='是']").click()


def is_contract(driver):
    driver.find_element(By.XPATH, "//div[@id='isContract']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='是']").click()


def ba_supplier(driver):  # 拟选供应商
    driver.find_element(By.XPATH, "//a[text()='+拟选供应商']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//div[text()='北京行控科技有限公司']/../../td[1]/span/label/span/input").click()
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()


def BA_for_PR(driver):  # 干净的事前单，可用于采购
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    edit_money(driver, '200')
    enter_apartment(driver)
    ba_supplier(driver)
    choice_path(driver, '事前申请单自审')
    is_purchase(driver)
    edit_matter(driver, '用于采购')
    submit(driver)
    agree(driver)


def BA_for_CT(driver):  # 干净的事前单，可用于合同
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    edit_money(driver, '200')
    enter_apartment(driver)
    choice_path(driver, '事前申请单自审')
    # noinspection PyBroadException
    try:
        is_contract(driver)
    except Exception:
        pass
    edit_matter(driver, '用于合同')
    submit(driver)
    agree(driver)


def choice_detail_BA(driver):  # 选择明细的事前单，可用于采购，采购白屏
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    choice_apply_detail(driver)
    edit_money(driver, '220')
    enter_apartment(driver)
    choice_path(driver, '事前申请单自审')
    is_purchase(driver)
    edit_matter(driver, '产品明细')
    submit(driver)
    agree(driver)


def apply_detail_BA(driver):  # 输入明细的事前单，可用于采购
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    apply_detail(driver)
    edit_money(driver, '200')
    enter_apartment(driver)
    choice_path(driver, '事前申请单自审')
    is_purchase(driver)
    edit_matter(driver, '申请明细')
    submit(driver)
    agree(driver)


def standard_BA(driver):  # 标准无测算的经费单
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    edit_money(driver, '100')
    enter_apartment(driver)
    edit_matter(driver, '无测算')
    choice_path(driver, "事前申请单自审")
    submit(driver)
    agree(driver)
    choice_RI(driver)
    start_BA_RI(driver)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    enter_apartment(driver)
    choice_path(driver, "报销申请单自审")
    pay_setting(driver)
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def standard_BA_copy(driver):  # 标准无测算的经费单复制单据
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    edit_money(driver, '100')
    enter_apartment(driver)
    edit_matter(driver, '无测算经费')
    choice_path(driver, "事前申请单自审")
    submit(driver)
    BA_recopy(driver)


def train_BA_RI(driver):  # 培训费测算与报销
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    time.sleep(0.5)
    train(driver)
    enter_apartment(driver)
    choice_path(driver, "事前申请单自审")
    edit_matter(driver, '培训费测算')
    submit(driver)
    agree(driver)
    time.sleep(1)
    start_BA_RI(driver)
    RI_train(driver)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    enter_apartment(driver)
    choice_path(driver, "报销申请单自审")
    edit_matter1(driver, "培训费报销")
    pay_setting(driver)
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def choice_MA(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//button[@testid='relatedBill']").click()
    time.sleep(0.1)

    driver.find_element(By.XPATH, "//button[text()='关联单据']").click()
    time.sleep(0.2)
    # TODO 若没有事项申请单，此处会报错，应该要写断言，还不知道咋写
    ma_path = driver.find_element(By.XPATH,"//div[@class='ant-modal-body']/div/div/div/div/div/div/div/div[2]/table/tbody/tr[1]")

    ma_path.click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()


def standard_NORI(driver):
    choice_RI(driver)
    start_NORI(driver)
    choice_budget(driver)
    # choice_MA(driver) # 选关联事项申请单
    RI_labor(driver)
    edit_money1(driver, '500')
    enter_apartment(driver)
    choice_path(driver, '报销申请单自审')
    edit_matter1(driver, '劳务费报销')
    pay_setting(driver)
    RIsubmit(driver)
    cancel(driver)
    driver.find_element(By.XPATH, "//button[text()='复制单据']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    edit_matter1(driver, "复制")
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def standard_NORI1(driver):
    choice_RI(driver)
    start_NORI(driver)
    choice_budget(driver)
    # choice_MA(driver) # 选关联事项申请单
    # RI_labor(driver)
    edit_money1(driver, '500')
    enter_apartment(driver)
    choice_path(driver, '报销申请单自审')
    edit_matter1(driver, '无申请报销')
    pay_setting(driver)
    RIsubmit(driver)
    cancel(driver)
    driver.find_element(By.XPATH, "//button[text()='复制单据']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    edit_matter1(driver, "复制")
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def standard_NORI2(driver):
    choice_RI(driver)
    start_NORI(driver)
    choice_budget(driver)
    # choice_MA(driver) # 选关联事项申请单
    # RI_labor(driver)

    driver.find_element(By.XPATH, "//button[@testid='official']").click()
    time.sleep(0.5)
    RI_official(driver)
    edit_money1(driver, '500')
    enter_apartment(driver)
    choice_path(driver, '报销申请单自审')
    edit_matter1(driver, '无申请报销')
    pay_setting(driver)
    RIsubmit(driver)
    cancel(driver)
    driver.find_element(By.XPATH, "//button[text()='复制单据']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    edit_matter1(driver, "复制")
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def standard_NORI3(driver):
    choice_RI(driver)
    start_NORI(driver)
    choice_budget(driver)
    choice_MA(driver)  # 选关联事项申请单
    time.sleep(0.1)
    js = 'var q = document.querySelector("#globalLayoutContent").scrollTo(0,-400)'
    # RI_labor(driver)
    driver.execute(js)
    RI_official(driver)
    driver.find_element(By.XPATH, "//button[@testid='official']")
    time.sleep(0.5)
    RI_official(driver)
    edit_money1(driver, '500')
    enter_apartment(driver)
    choice_path(driver, '报销申请单自审')
    edit_matter1(driver, '无申请报销')
    pay_setting(driver)
    RIsubmit(driver)
    cancel(driver)
    driver.find_element(By.XPATH, "//button[text()='复制单据']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    edit_matter1(driver, "复制")
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def invalid_NO_RI(driver):  # 作废报销单
    choice_RI(driver)
    start_NORI(driver)
    choice_budget(driver)
    # choice_MA(driver) # 选关联事项申请单
    # RI_labor(driver)
    edit_money1(driver, '500')
    enter_apartment(driver)
    choice_path(driver, '报销申请单自审')
    edit_matter1(driver, '无申请报销')
    pay_setting(driver)
    RIsubmit(driver)
    agree(driver)
    choice_menu(driver, "支出管理", "报销申请")
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]/td[1]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='作废']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    driver.refresh()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='删除']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()


def invalid_NO_RI1(driver):  # 作废报销单
    choice_RI(driver)
    start_NORI(driver)
    choice_budget(driver)
    # choice_MA(driver) # 选关联事项申请单
    RI_labor(driver)
    edit_money1(driver, '500')
    enter_apartment(driver)
    choice_path(driver, '报销申请单自审')
    edit_matter1(driver, '无申请报销')
    pay_setting(driver)
    RIsubmit(driver)
    agree(driver)
    choice_menu(driver, "支出管理", "报销申请")
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]/td[1]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='作废']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    driver.refresh()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='删除']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()


def invalid_NO_RI2(driver):  # 作废报销单
    choice_RI(driver)
    start_NORI(driver)
    choice_budget(driver)
    # choice_MA(driver) # 选关联事项申请单
    # RI_labor(driver)
    driver.find_element(By.XPATH, "//button[@testid='official']").click()
    RI_official(driver)
    edit_money1(driver, '500')
    enter_apartment(driver)
    choice_path(driver, '报销申请单自审')
    edit_matter1(driver, '无申请报销')
    pay_setting(driver)
    RIsubmit(driver)
    agree(driver)
    choice_menu(driver, "支出管理", "报销申请")
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]/td[1]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='作废']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    driver.refresh()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='删除']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()


def standard_AGRI(driver):
    choice_RI(driver)
    time.sleep(1)
    start_AGRI(driver)
    time.sleep(1)
    choice_budget(driver)
    # choice_MA(driver)
    RI_labor(driver)
    edit_money1(driver, '500')
    enter_apartment(driver)
    # choice_paymethod(driver)
    # company(driver)
    choice_path(driver, '报销申请单自审')
    pay_setting(driver)
    edit_matter1(driver, '劳务费报销')
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def standard_AGRI1(driver):
    choice_RI(driver)
    time.sleep(1)
    start_AGRI(driver)
    time.sleep(1)
    choice_budget(driver)
    # choice_MA(driver)
    # RI_labor(driver)
    edit_money1(driver, '500')
    enter_apartment(driver)
    # choice_paymethod(driver)
    # company(driver)
    choice_path(driver, '报销申请单自审')
    pay_setting(driver)
    edit_matter1(driver, '劳务费报销')
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def official_BA_RI(driver):  # 接待费测算与报销
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    official(driver)
    enter_apartment(driver)
    choice_path(driver, "事前申请单自审")
    edit_matter(driver, "接待费测算")
    submit(driver)
    agree(driver)
    start_BA_RI(driver)
    RI_official(driver)
    enter_apartment(driver)
    edit_matter1(driver, "接待费报销")
    choice_path(driver, "报销申请单自审")
    pay_setting(driver)
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def meeting_BA_RI(driver):  # 会议费测算与报销
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    meeting(driver)
    enter_apartment(driver)
    choice_path(driver, "事前申请单自审")
    edit_matter(driver, "会议费测算")
    submit(driver)
    agree(driver)
    start_BA_RI(driver)
    RI_meeting(driver)
    enter_apartment(driver)
    choice_path(driver, "报销申请单自审")
    edit_matter1(driver, "会议费报销")
    pay_setting(driver)
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def travel_BA_RI(driver):  # 差旅费测算与报销
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    travel(driver)
    enter_apartment(driver)
    choice_path(driver, "事前申请单自审")
    edit_matter(driver, "差旅费测算")
    submit(driver)
    agree(driver)
    start_BA_RI(driver)
    RI_travel(driver)
    enter_apartment(driver)
    choice_path(driver, '报销申请单自审')
    edit_matter1(driver, '差旅费报销')
    pay_setting(driver)
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def labor_BA_RI(driver):  # 劳务费测算与驳回
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    labor(driver)
    enter_apartment(driver)
    choice_path(driver, '事前申请单自审')
    edit_matter(driver, "劳务费测算")
    submit(driver)
    agree(driver)
    start_BA_RI(driver)
    RI_labor(driver)
    enter_apartment(driver)
    choice_path(driver, '报销申请单自审')
    edit_matter1(driver, "劳务费报销")
    pay_setting(driver)
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def IM0(driver):  # 从列表页
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    edit_money(driver, '100')
    enter_apartment(driver)
    edit_matter(driver, '发起事前、通过、发起预付、通过、发起报销、通过、核销')
    choice_path(driver, "事前申请单自审")
    submit(driver)
    agree(driver)
    add_im0(driver)
    edit_im(driver, '列表页发起预付、通过、发起报销、通过、核销')
    submit(driver)
    agree(driver)
    choice_RI(driver)
    start_IM_RI(driver)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    enter_apartment(driver)
    choice_path(driver, "报销申请单自审")
    pay_setting(driver)
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def IM1(driver):  # 从详情页
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    edit_money(driver, '100')
    enter_apartment(driver)
    edit_matter(driver, '发起事前、通过、发起预付、通过、发起报销、通过、核销')
    choice_path(driver, "事前申请单自审")
    submit(driver)
    agree(driver)
    add_im1(driver)
    edit_im(driver, '详情页发起预付、通过、发起报销、通过、核销')
    submit(driver)
    agree(driver)
    choice_RI(driver)
    start_IM_RI(driver)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    enter_apartment(driver)
    choice_path(driver, "报销申请单自审")
    pay_setting(driver)
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def IM2(driver):  # 从列表页
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    edit_money(driver, '100')
    enter_apartment(driver)
    edit_matter(driver, '发起事前、通过、发起预付、撤销、删除')
    choice_path(driver, "事前申请单自审")
    submit(driver)
    agree(driver)
    add_im0(driver)
    edit_im(driver, '列表页发起预付、撤销、删除')
    submit(driver)
    cancel(driver)
    delete_bill(driver)


def IM3(driver):  # 从详情页
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    edit_money(driver, '100')
    enter_apartment(driver)
    edit_matter(driver, '发起事前、通过、发起预付、驳回、删除')
    choice_path(driver, "事前申请单自审")
    submit(driver)
    agree(driver)
    add_im1(driver)
    edit_im(driver, '详情页发起预付、驳回、删除')
    submit(driver)
    refuse(driver)
    time.sleep(0.5)
    choice_menu(driver,"支出管理", "预付申请")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]/td[1]/div").click()
    time.sleep(0.5)
    delete_bill(driver)


class Pay(con):

    def menu(self):
        self.choice_menu('支出管理', '事前申请')

    def add(self):
        time.sleep(0.5)
        self.dr("//span[text()='+ 发起申请']/..").click()

    def editMoney(self, money='500',placeholder='请输入申请金额'):
        self.dr("//input[@placeholder='"+placeholder+"']").send_keys(money)
        self.dr("//span[text()='下一步']/..").click()
        time.sleep(1)
        self.dr("//span[text()='继续留下']/..").click()

    def viewAddReimburse(self):
        # from budgetApplication billView add reimburse
        self._more()
        self.dr("//li[text()='发起报销']").click()

    def payDetail(self):
        # 需要先判断是否开启多支付明细，默认不开启
        self.dr("//div[@id='paySettingId_0']/div/div").click()
        time.sleep(0.1)
        self.dr("//input[@id='paySettingId_0']").send_keys(Keys.ENTER)
        time.sleep(1)
        self.dr("//div[@id='payeeFullName_0']/div/div/ul/li/div/input").send_keys("单位")

    def editReimburse(self,money="500"):
        # self.dr("//input[@placeholder='请输入报销金额']").send_keys(money)
        self._nextPage()
        # self.enterDepart()
        self.choicePath('报销申请单自审')
        self.payDetail()

    def submitReimburse(self):
        time.sleep(0.1)
        self.dr("//span[text()='确认提交']/..").click()
        time.sleep(0.5)
        self.dr("//span[text()='确 认']/..").click()
        time.sleep(0.1)
        self.dr("//span[text()='查看详情']/..").click()

    def check(self):
        # reimburse bill use
        self._more()
        self.dr("//button[text()='资金领用']").click()
        time.sleep(1)
        self.dr("//div[@id='checkOwnerId']/div/div").click()
        time.sleep(0.5)
        self.dr("//input[@id='checkOwnerId']").send_keys(Keys.ENTER)
        self.dr("//div[@id='checkNumber']/div").click()
        time.sleep(0.5)
        check_number = '支票号' + time.strftime('%m%d%H%M%S')
        self.dr("//input[@id='checkNumber']").send_keys(check_number)
        self.dr("//li[text()='" + check_number + "']").click()
        self.dr("//span[text()='确认领用']/..").click()

    def useCheck(self):
        self.choice_menu('支出管理', "报销申请")
        self.inView()
        self.check()
        self._more()
        self.dr("//button[text()='经费核销']").click()
        self._sure()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    common_funcation.login_code(driver)
    IM2(driver)
