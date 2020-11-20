# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from service.bpm_service.pay import BA_for_CT, choice_BA, edit_matter1, pay_setting, write_off, choice_budget, RI_labor
import time
from service.bpm_service.common_funcation import enter_apartment, enter_b_supplier, enter_ct_type, enter_pc_type, \
    enter_sign_user, \
    choice_path, submit, agree, RIsubmit, choice_menu, start_add, ag_enter_sign_user


def start_BA_CT(driver):  # 从事前单详情页发起报销
    choice_BA(driver)
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]/td[3]").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//li[text()='申请合同']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='继续申请合同']/..").click()


def pay_1plan(driver):   # 填写付款计划
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="globalLayoutContent"]/div/div/div[3]/div[2]/div/section['
                                  '2]/div/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[4]/div').click()
    driver.find_element(By.XPATH, '//*[@id="globalLayoutContent"]/div/div/div[3]/div[2]/div/section['
                                  '2]/div/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[4]/div/div/div['
                                  '2]/input').send_keys('100')
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()


def edit_ct(driver, ct_name):
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys(ct_name+time.strftime('%m%d%H%M%S'))
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys(ct_name+time.strftime('%m%d%H%M%S'))


def edit_ag(driver, ag_name):
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys(ag_name + time.strftime('%m%d%H%M%S'))
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys(ag_name + time.strftime('%m%d%H%M%S'))


def start_CT_RI(driver):
    driver.find_element(By.XPATH, '//span[text()="合同管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='合同管理']").click()
    driver.refresh()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]/td[1]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.01)
    driver.find_element(By.XPATH, "//button[text()='发起报销']").click()
    time.sleep(0.01)
    driver.find_element(By.XPATH, "//li[text()='一期付款']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()


def choice_CT(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[text()="合同管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='合同管理']").click()


def choice_AG(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[text()="合同管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='框架协议']").click()


def start_no_ct(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='+ 无申请合同']/..").click()


def AG_for_RI(driver):  # 新增框架协议，可用于报销/变更
    choice_menu(driver, '合同管理', '框架协议')
    start_add(driver, '+ 申请框架协议')
    enter_apartment(driver)
    enter_ct_type(driver)
    # enter_sign_user(driver)
    ag_enter_sign_user(driver)
    enter_pc_type(driver)
    choice_path(driver, '框架协议单自审')
    edit_ag(driver, '框架协议')
    submit(driver)
    agree(driver)


def no_ct_for_RI(driver):   # 无申请合同用于报销
    choice_CT(driver)
    start_no_ct(driver)
    pay_1plan(driver)
    enter_apartment(driver)
    enter_sign_user(driver)
    enter_pc_type(driver)
    enter_b_supplier(driver)
    enter_ct_type(driver)
    choice_path(driver, "合同审批单自审")
    edit_ct(driver, '无申请合同')
    submit(driver)
    agree(driver)


def NO_CT_RI(driver):   # 无申请合同报销
    no_ct_for_RI(driver)
    start_CT_RI(driver)
    choice_budget(driver)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    enter_apartment(driver)
    choice_path(driver, "报销申请单自审")
    edit_matter1(driver, "一期报销")
    pay_setting(driver)
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def BA_CT_RI(driver):   # 事前-合同-报销-核销
    BA_for_CT(driver)
    start_BA_CT(driver)
    pay_1plan(driver)
    enter_apartment(driver)
    enter_sign_user(driver)
    enter_pc_type(driver)
    enter_b_supplier(driver)
    enter_ct_type(driver)
    choice_path(driver, "合同审批单自审")
    edit_ct(driver, '测试合同')
    submit(driver)
    agree(driver)
    start_CT_RI(driver)
    enter_apartment(driver)
    choice_path(driver, '报销申请单自审')
    edit_matter1(driver, '一期报销')
    pay_setting(driver)
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def change_CT_RI(driver):  # 无申请合同变更后进行报销
    no_ct_for_RI(driver)
    driver.find_element(By.XPATH, '//span[text()="合同管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='合同管理']").click()
    driver.refresh()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]/td[1]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//button[text()='合同变更']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[@id='nextBtn']").click()
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys('变更'+time.strftime('%m%d%H%M%S'))
    submit(driver)
    agree(driver)
    start_CT_RI(driver)
    choice_budget(driver)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    enter_apartment(driver)
    choice_path(driver, "报销申请单自审")
    edit_matter1(driver, "一期报销")
    pay_setting(driver)
    RIsubmit(driver)
    agree(driver)
    write_off(driver)


def change_AG(driver):
    AG_for_RI(driver)
    choice_menu(driver, '合同管理', '框架协议')
    driver.refresh()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]/td[1]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.01)
    driver.find_element(By.XPATH, "//button[text()='协议变更']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys('变更' + time.strftime('%m%d%H%M%S'))
    submit(driver)
    agree(driver)