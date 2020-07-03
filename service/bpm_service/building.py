"""UI二期建设项目"""
from selenium.webdriver.common.by import By
import time
from service.bpm_service.common_funcation import agree, submit, refuse, cancel, deletebill
from selenium.webdriver.common.keys import Keys
import random


def choicedp(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='建设项目']/..").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//a[text()='项目申报']").click()
    
    
def startdp(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='申报项目']/..").click()
    
    
def editdp(driver): # 自定义枚举若没有，则会失败。为解决软件运行效率，尽量简单
    time.sleep(0.1)
    # 项目类别
    driver.find_element(By.XPATH, "//div[@id='buildingItemTypeId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='标准项目']").click()
    # 项目负责人
    driver.find_element(By.XPATH, "//div[@id='managerId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='wsp']").click()
    # 经费来源
    driver.find_element(By.XPATH, "//div[@id='capitalSourceId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='全额拨款']").click()
    # 拟选公司
    driver.find_element(By.XPATH, "//div[@id='companies']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='永辉超市']").click()
    # 项目名称
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys('项目'+str(time.strftime('%m%d%H%M%S')))
    # 项目介绍
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys('test'+str(time.strftime('%m%d%H%M%S')))
    # 备注说明
    driver.find_element(By.XPATH, "//textarea[@id='remark']").send_keys('备注'+str(time.strftime('%m%d%H%M%S')))
    # 概算金额
    driver.find_element(By.XPATH, "//input[@id='amount']").send_keys('500')


def choicebn(driver):
    # 建设项目-中标单位通报
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='建设项目']/..").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//a[text()="中标单位通报"]').click()

def startbn(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='通报中标']/..").click()
    

def editbn(driver):
    # 项目名称
    driver.find_element(By.XPATH, "//div[@id='buildingPermitId']/div/div").click()
    time.sleep(0.5)
#     driver.find_element(By.XPATH, "//body/div[9]/div/div/div/ul/li[1]").click()
    driver.find_element(By.XPATH, "//input[@id='buildingPermitId']").send_keys(Keys.ENTER)
    # 采购方式
    driver.find_element(By.XPATH, "//div[@id='purchaseMethodId']/div/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//input[@id='purchaseMethodId']").send_keys(Keys.ENTER)
    # 中标单位
    driver.find_element(By.XPATH, "//div[@id='supplierId']/div/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//li[text()='永辉超市']").click()
    # 中标金额
    driver.find_element(By.XPATH, "//input[@id='amount']").send_keys('500')
    # 代理机构
    driver.find_element(By.XPATH, "//input[@id='proxyOrganization']").send_keys('机构'+str(time.strftime('%m%d%H%M%S')))
    # 备注
    driver.find_element(By.XPATH, "//textarea[@id='remark']").send_keys('备注'+str(time.strftime('%m%d%H%M%S')))
    

def choiceuserdn(driver): # 中标单位通报的相关人员
    # js = 'var q = document.querySelector("#root > div > div > div > div.antd-pro-layouts-basic-layout-layoutContent").scrollTo(0,1000)'
    # driver.execute_script(js)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='新增相关人员']").click()
    time.sleep(1)
    # noinspection PyBroadException
    try:
        managerment = ('校领导', '总务部', '安全保卫', '人事部', '教导处')
        managerment1 = random.sample(managerment, 1)
        managerment2 = "".join(managerment1)
        driver.find_element(By.XPATH, "//span[text()='" + managerment2 + "']/../../span[2]/span").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[text()='加入通报 >']/..").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    except Exception:
        print("选择参会人员失败")

def agree_db(driver):
    choicedp(driver)
    startdp(driver)
    editdp(driver)
    submit(driver)
    agree(driver)


def reject_db(driver):
    choicedp(driver)
    startdp(driver)
    editdp(driver)
    submit(driver)
    refuse(driver)
    

def cancel_db(driver):
    choicedp(driver)
    startdp(driver)
    editdp(driver)
    submit(driver)
    cancel(driver)
    deletebill(driver)
    time.sleep(1)

def standardbn(driver):
    choicebn(driver)
    startbn(driver)
    editbn(driver)
    choiceuserdn(driver)
    submit(driver)