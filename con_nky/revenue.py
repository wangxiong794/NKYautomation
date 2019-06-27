'''收入管理'''
from selenium.webdriver.common.by import By
import time
from con_nky.common_funcation import choice_apartment, choice_liucheng, submit,\
    agree
import random
from con_nky.pay import choice_paymethod
def choice_CG(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,'//span[text()="收入管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//a[text()='收费标准']").click()
def choice_RE(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,'//span[text()="收入管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//a[text()='收费管理']").click()
def choice_IC(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,'//span[text()="收入管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//a[text()='收入登记']").click()
def choice_bankacount(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,'//span[text()="收入管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//a[text()='账户管理']").click()
def start_CG(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='+ 发起申请']/..").click()
def start_RE(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='+ 新增收费审批单']/..").click()
def start_IC(driver):
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='+ 发起登记']/..").click()
def choice_acount(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//input[@value='10000']").click()
    driver.find_element(By.XPATH,"//span[text()='确认选择']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[1]/td[1]/span[2]").click()
    driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[3]/td[1]/span[2]").click()
    driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[4]/td[1]/label/span[1]/input").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//span[text()='下一步']/..").click()
def choice_ICRE(driver):
    time.sleep(0.1)
    i=random.randint(0,1)
    if i == 0:
        driver.find_element(By.XPATH,"//input[@class='ant-input']").send_keys('100')
    else:
        driver.find_element(By.XPATH,"//span[text()='选择关联收据']/..").click()
        time.sleep(0.1)
        driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/span/label/span/input").click()
        driver.find_element(By.XPATH,"//span[text()='确认选择']/..").click()
        time.sleep(0.5)
        ICREMONEY=driver.find_element(By.XPATH,"//tbody/tr/td[3]").text
        driver.find_element(By.XPATH,"//input[@class='ant-input']").send_keys(ICREMONEY)
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='下一步']/..").click()
def edit_IC(driver):
    time.sleep(0.1)
    choice_paymethod(driver)
    choice_liucheng(driver,'收入自审')
    driver.find_element(By.XPATH,"//textarea[@id='description']").send_keys('六月零食'+time.strftime('%m%d%H%M%S'))
def edit_CG(driver):
    CG_NAME=choice_apartment(driver)
    CG_NAME=CG_NAME +'的收费标准'+time.strftime('%m%d%H%M%S')
    #标准名称
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys(CG_NAME)
    #标准金额
    driver.find_element(By.XPATH,"//input[@id='amount']").send_keys('100')
    #备注
    driver.find_element(By.XPATH,"//textarea[@id='description']").send_keys(CG_NAME)
    #审批流程
    choice_liucheng(driver,'收费自审')
def edit_RE(driver):
    RE_NAME=choice_apartment(driver)
    RE_NAME=RE_NAME+'的收费单'+time.strftime('%m%d%H%M%S')
    #审批流程
    choice_liucheng(driver,'收据自审')
    #事由
    driver.find_element(By.XPATH,"//textarea[@id='description']").send_keys(RE_NAME)
    #付款单位
    i=str(random.randint(0,100))
    driver.find_element(By.XPATH,"//input[@id='payerCompany']").send_keys(i)
    #收款明细
    driver.find_element(By.XPATH,"//td[@class='ant-table-fixed-columns-in-body order-box___3sLv3']/../td[2]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//body/div[4]/div/div/div/ul/li[1]").click()
    driver.find_element(By.XPATH,"//td[@class='ant-table-fixed-columns-in-body order-box___3sLv3']/../td[4]/div").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//td[@class='ant-table-fixed-columns-in-body order-box___3sLv3']/../td[4]/div/div/div[2]/input").send_keys('5')
def standard_CG(driver):
    choice_CG(driver)
    start_CG(driver)
    edit_CG(driver)
    submit(driver)
    agree(driver)
def standard_RE(driver):
    choice_RE(driver)
    start_RE(driver)
    edit_RE(driver)
    submit(driver)
    agree(driver)
def standard_IC(driver):
    choice_IC(driver)
    start_IC(driver)
    choice_acount(driver)
    choice_ICRE(driver)
    edit_IC(driver)
    submit(driver)
    agree(driver)