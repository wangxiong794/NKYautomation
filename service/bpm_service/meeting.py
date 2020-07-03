import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from service.bpm_service.common_funcation import choice_menu, start_add, choice_path, enter_apartment, submit, cancel, deletebill, \
    refuse, agree, invalid
from service.bpm_service.pay import edit_matter, edit_matter1


def cs_date(driver):    # 议事会签选时间
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[@id='applyDate']/div/input").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//a[text()='今天']").click()


def enter_host_user(driver):    # 议事会签选主持人
    driver.find_element(By.XPATH, "//div[@id='hostUserId']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='hostUserId']").send_keys(Keys.ENTER)


def enter_record_user(driver):  # 议事会签选记录人
    driver.find_element(By.XPATH, "//div[@id='recordUserId']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='recordUserId']").send_keys(Keys.ENTER)


def enter_cs_type(driver):  # 议事会签会议类型
    driver.find_element(By.XPATH, "//div[@id='countersignTypeId']/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='countersignTypeId']").send_keys(Keys.ENTER)


def choice_user(driver):    # 议事会签选参会人员
    driver.find_element(By.XPATH, "//button[text()='新增参会人员']").click()
    time.sleep(1)
    managerment = ('校领导', '总务部', '安全保卫', '人事部', '教导处')
    managerment1 = random.sample(managerment, 1)
    managerment2 = "".join(managerment1)
    driver.find_element(By.XPATH, "//span[text()='" + managerment2 + "']/../../span[2]/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='加入参会 >']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()


def cancel_MA(driver):  # 撤销删除
    choice_menu(driver, '重要事项', '事项申请')
    start_add(driver, '发起申请')
    enter_apartment(driver)
    driver.find_element(By.XPATH, "//input[@id='amount']").send_keys('100')
    edit_matter(driver,'事项申请')
    submit(driver)
    cancel(driver)
    deletebill(driver)


def copy_MA(driver):    # 驳回复制 通过
    choice_menu(driver, '重要事项', '事项申请')
    start_add(driver, '发起申请')
    enter_apartment(driver)
    driver.find_element(By.XPATH, "//input[@id='amount']").send_keys('100')
    edit_matter(driver, '事项申请')
    submit(driver)
    refuse(driver)
    time.sleep(0.1)
    choice_menu(driver, '重要事项', '事项申请')
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]/td[1]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='复制单据']").click()
    edit_matter(driver, '驳回复制')
    submit(driver)
    agree(driver)


def invalid_MA(driver):  # 通过 作废
    choice_menu(driver, '重要事项', '事项申请')
    start_add(driver, '发起申请')
    enter_apartment(driver)
    driver.find_element(By.XPATH, "//input[@id='amount']").send_keys('100')
    edit_matter(driver, '事项申请')
    submit(driver)
    agree(driver)
    time.sleep(0.1)
    choice_menu(driver, '重要事项', '事项申请')
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]/td[1]/div").click()
    time.sleep(1)
    invalid(driver)


def CS(driver): # 发起议事会签
    choice_menu(driver, '重要事项', '议事会签')
    start_add(driver, "+ 发起会签")
    cs_date(driver)
    driver.find_element(By.XPATH, "//input[@id='location']").send_keys('地点'+time.strftime('%m%d%H%M%S'))
    cs_date(driver)
    enter_host_user(driver)
    enter_record_user(driver)
    enter_cs_type(driver)
    edit_matter1(driver, '会签测试')
    choice_user(driver)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//textarea").send_keys('测试'+time.strftime('%m%d%H%M%S'))
    submit(driver)