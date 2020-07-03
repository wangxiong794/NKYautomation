"""收入管理"""
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys

from service.bpm_service.common_funcation import choice_apartment, choice_liucheng, submit, agree, cancel, deletebill, refuse, \
    enter_apartment
import random
from service.bpm_service.pay import choice_paymethod

# TODO
def choice_CG(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//span[text()="收入管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='收费标准']").click()


def choice_RE(driver):
    time.sleep(1)
    driver.find_element(By.XPATH, '//span[text()="收入管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='收费管理']").click()


def choice_IC(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//span[text()="收入管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='收入登记']").click()


def choice_bankacount(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[text()="收入管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='账户管理']").click()


def start_CG(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='新增标准']/..").click()


def start_RE(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='新增收费']/..").click()


def start_IC(driver):
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='发起登记']/..").click()


def choice_acount(driver):  # 选择账户
    time.sleep(0.5)
    # noinspection PyBroadException
    try:
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@value='1']/../../../../../td[2]").click()
    except Exception:
        print("无可用收款账户进行选择")
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()


def choice_budget(driver):  # 选择预算项
    # noinspection PyBroadException
    try:
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//span[text()='预算项目']/../../../../../../tbody/tr[1]/td[1]/div").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//span[text()='预算项目']/../../../../../../tbody/tr[2]/td[2]").click()
    except Exception:
        print("项目层级过深")
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()


def choice_ICRE(driver):
    # noinspection PyBroadException
    try:
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//button[text()='关联收费审批单']").click()
        time.sleep(0.5)
        # driver.find_element(By.XPATH, "//span[text()='单据编号']/../../../../../../../../div[2]/table/tbody/tr[1]/td[1]/span/label/span/input").click()
        driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]").click()
        driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
        time.sleep(0.5)
    except Exception:

        driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
        print("无可用关联收费审批单")
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@placeholder='请输入金额']").send_keys('500')
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()


def edit_IC(driver):
    time.sleep(0.1)
    choice_paymethod(driver)
    choice_liucheng(driver, '收入登记单自审')
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys('登记单' + str(time.strftime('%m%d%H%M%S')))


def edit_CG(driver):
    # CG_NAME = choice_apartment(driver)
    enter_apartment(driver)
    cg_name = '收费标准' + time.strftime('%m%d%H%M%S')
    # 标准名称
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys(cg_name)
    # 标准金额
    driver.find_element(By.XPATH, "//input[@id='amount']").send_keys('100')
    # 备注
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys(cg_name)
    # 审批流程
    choice_liucheng(driver, '收费标准单自审')


def copy_CG(driver):    # 复制单据
    time.sleep(1)
    driver.back()   # 返回上一步操作
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    driver.find_element(By.XPATH, "//button[text()='复制单据']").click()
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys("复制")
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys("驳回单据复制过来的")


def edit_RE(driver):
    # RE_NAME = choice_apartment(driver)
    enter_apartment(driver)
    re_name =  '收费审批单' + time.strftime('%m%d%H%M%S')
    # 审批流程
    choice_liucheng(driver, '收费审批单自审')
    # 事由
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys(re_name)
    # 付款单位
    i = str(random.randint(0, 100))
    driver.find_element(By.XPATH, "//input[@id='payerCompany']").send_keys("单位"+i)
    # 收款明细
    driver.find_element(By.XPATH, "//td[@id='0_chargeStandardId']/div").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//td[@id='0_chargeStandardId']/div/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
    # driver.find_element(By.XPATH, "//body/div[6]/div/div/div/ul/li[1]").click()
    driver.find_element(By.XPATH, "//td[@id='0_number']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//td[@id='0_number']/div/div/div/div[2]/input").send_keys('5')


def standard_CG(driver):    # 新增收费标准单 审批通过
    choice_CG(driver)
    start_CG(driver)
    edit_CG(driver)
    submit(driver)
    agree(driver)


def cancel_CG(driver):  # 新增收费标准单 撤销并删除
    choice_CG(driver)
    start_CG(driver)
    edit_CG(driver)
    submit(driver)
    cancel(driver)
    deletebill(driver)


def reject_CG(driver):  # 新增收费标准单 驳回复制 复制单据
    choice_CG(driver)
    start_CG(driver)
    edit_CG(driver)
    submit(driver)
    refuse(driver)
    copy_CG(driver)
    submit(driver)


def standard_RE(driver):    # 新增收费审批单 审批通过
    choice_RE(driver)
    start_RE(driver)
    edit_RE(driver)
    submit(driver)
    agree(driver)


def cancel_RE(driver):      # 新增收费审批单 撤销并删除
    choice_RE(driver)
    start_RE(driver)
    edit_RE(driver)
    submit(driver)
    cancel(driver)
    deletebill(driver)


def reject_RE(driver):      # 新增收费审批单 驳回
    choice_RE(driver)
    start_RE(driver)
    edit_RE(driver)
    submit(driver)
    refuse(driver)


def standard_IC(driver):    # 审批通过收入登记
    choice_IC(driver)
    start_IC(driver)
    choice_acount(driver)
    choice_budget(driver)
    choice_ICRE(driver)
    edit_IC(driver)
    submit(driver)
    time.sleep(5)   # 存在提示成功的提示语冗余的BUG，需要等待提示消失
    agree(driver)


def cancel_IC(driver):  # 撤销并删除收入登记
    choice_IC(driver)
    start_IC(driver)
    choice_acount(driver)
    choice_budget(driver)
    choice_ICRE(driver)
    edit_IC(driver)
    submit(driver)
    time.sleep(5)
    cancel(driver)
    deletebill(driver)


def reject_IC(driver):  # 驳回收入登记
    choice_IC(driver)
    start_IC(driver)
    choice_acount(driver)
    choice_budget(driver)
    choice_ICRE(driver)
    edit_IC(driver)
    submit(driver)
    time.sleep(5)
    refuse(driver)