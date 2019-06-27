''''''
from con_nky.constructionProject import choice_apartment
from con_nky.common_funcation import agree, submit
import random
'''
Created on 2019年1月30日

@author: 13348
'''
from selenium.webdriver.common.by import By
import time

#========合同申请========
def contract_before(driver,number):
    #合同管理
    driver.find_element(By.XPATH,'//span[text()="合同管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//a[text()='合同管理']").click()
    #申请合同
    time.sleep(1)
    driver.find_element_by_xpath("//span[text()='+ 申请合同']/..").click()
    #选申请
    time.sleep(1)
    driver.find_element_by_xpath("//div[@class='ant-spin-container']/div[1]/ul/li").click()
    #继续申请合同
    try:
        time.sleep(1)
        driver.find_element(By.XPATH,"//span[text()='继续申请合同']/..").click() 
    except:
        pass
    #填单据--合同名称
    time.sleep(1)
    ct_apartment=choice_apartment(driver)
    ct_name=driver.find_element(By.XPATH,"//div[@id='createdUserId']/div/div/div[1]").text
    contract_name=number+ct_name+'为'+ct_apartment+'部门申请的合同'+time.strftime('%F-%H%M%S')
    driver.find_element_by_xpath("//input[@id='name']").send_keys(contract_name)
    b_party=driver.find_element(By.XPATH,"//input[@id='bSupplierName']").get_attribute("value")
    if len(b_party)==0:
        time.sleep(1)
        driver.find_element_by_xpath("//input[@id='bSupplierName']/../span/button").click()
        time.sleep(1)
        driver.find_element_by_xpath("//tbody/tr[1]/td[1]/span/label/span/input").click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[text()='确认选择']/..").click()
    else:
        pass
    #获取可报经费
    time.sleep(1)
    money=driver.find_element(By.XPATH,"//label[text()='可用金额']/../../div[2]/div/span/div/div[2]/input").get_attribute("value")
    #填单据--审批流程
    driver.find_element_by_xpath("//div[@id='billFlowDefineId']/div").click()
    driver.find_element_by_xpath("//li[text()='合同自审']").click()
    choice_contractPurchaseCatalog(driver)
    choice_contractType(driver)
    driver.find_element_by_xpath("//textarea[@id='description']").send_keys(contract_name)
    #滑动鼠标
    js='var q=document.querySelector("#root > div > section > section > main").scrollTo(0,1000)'
    driver.execute_script(js)
    return money
def choice_contractPurchaseCatalog(driver):#采购类型
    driver.find_element(By.XPATH,"//div[@id='contractPurchaseCatalogId']/div/div").click()
    ct_catalog=('货物类 ','工程类','服务类')
    ct_catalog1=random.sample(ct_catalog,1)
    ct_catalog2="".join(ct_catalog1)
    time.sleep(1)
    driver.find_element(By.XPATH,"//li[text()='"+ct_catalog2+"']").click()
def choice_contractType(driver):
    driver.find_element(By.XPATH,"//div[@id='contractTypeId']/div/div").click()
    ct_type=('财产租赁合同','仓储保管合同','加工承揽合同','建设工程勘察设计合同','货物运输合同','产权转移合同','营业资金帐薄','购销合同','建筑安装工程承包合同','技术合同','借款合同','财产保险合同','零印花税合同')
    ct_type1=random.sample(ct_type,1)
    ct_type2="".join(ct_type1)
    time.sleep(1)
    driver.find_element(By.XPATH,"//li[text()='"+ct_type2+"']").click()
def contract1(driver,money): 
    #填单据--合同付款计划--新增明细//div[@class='normal___3yB_h']/div[3]/div[4]/div/div[1]/div[2]/div/button
    driver.find_element(By.XPATH,"//div[@class='normal___3yB_h']/div[3]/div[3]/div/div/div[2]/div/button").click()
    #一期付款金额
    driver.find_element_by_xpath("//input[@id='amount_1']").send_keys(money)

def contract2(driver,money): 
    #填单据--合同付款计划--新增明细
    driver.find_element_by_xpath("//div[@class='normal___3yB_h']/div[3]/div[3]/div/div[1]/div[2]/div/button").click()
    #一期付款金额
    driver.find_element_by_xpath("//input[@id='amount_1']").send_keys(money)
    #新增第二个明细
    driver.find_element_by_xpath("//div[@class='normal___3yB_h']/div[3]/div[3]/div/div[1]/div[2]/div/button").click()
    #二期付款金额
    driver.find_element_by_xpath("//input[@id='amount_2']").send_keys(money)
    #更改预算年度
    driver.find_element(By.XPATH,"//div[@id='budgetYear_2']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//li[text()='未来年度']").click()
def contract_after(driver):    
    #确认提交
    driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']").click()
    #查看详情
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[@class='ant-btn']").click()
    #同意
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='同 意']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
def contract_change(driver):#合同变更
    #合同管理
    driver.find_element(By.XPATH,'//span[text()="合同管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//a[text()='合同管理']").click()  
    #选当前页面第一个合同
    driver.refresh()
    time.sleep(1)
    driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/div").click()
    #合同变更
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='合同变更']/..").click()
    #情况事由重新输入
    driver.find_element(By.XPATH,"//textarea").send_keys('合同变更')
    submit(driver)
    agree(driver)
def CT_copy(driver,new_reason):#撤销申请 +复制单据
    #确认提交
    driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']").click()
    #查看详情
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[@class='ant-btn']").click()
    #撤销申请
    driver.find_element(By.XPATH,"//div[@class='columnContent___UU8iM']/div[4]/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
    #复制单据
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[@class='ant-btn']").click()
    #更改事由
    driver.find_element(By.XPATH,"//textarea").send_keys('复制单据')
    submit(driver)
    #同意
    time.sleep(1)
    n_text=driver.find_element(By.XPATH,"//span[text()='同 意']/..").text
    agree(driver)
    return n_text
def talk(driver,say):#新增讨论
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='新增讨论']/..").click()
    driver.find_element(By.XPATH,"//textarea[@class='ant-input']").send_keys(say)
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='提 交']/..").click()
def CT_copy_discussion(driver,new_reason):#讨论+复制单据
    #确认提交
    driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']").click()
    #查看详情
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[@class='ant-btn']").click()
    #新增讨论
    talk(driver, say='撤销合同前的讨论'+time.strftime('%Y%m%d%H%M%S'))
    #撤销申请
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='撤销申请']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
    #再次新增讨论
    time.sleep(1)
    talk(driver,say='已撤销状态的讨论'+time.strftime('%Y%m%d%H%M%S'))
    #复制单据
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='复制单据']/..").click()
    #更改事由
    driver.find_element(By.XPATH,"//textarea").clear()
    driver.find_element(By.XPATH,"//textarea").send_keys(new_reason)
    #确认提交
    driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']").click()
    #查看详情
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[@class='ant-btn']").click()
    #验证讨论是否复制过来
    n_text=driver.find_element(By.XPATH,"//div[@class='ant-list-empty-text']").text
    driver.find_element(By.XPATH,"//span[text()='同 意']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
    return n_text
def CT_refuse(driver,new_reason):#驳回+复制单据
    #确认提交
    driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']").click()
    #查看详情
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[@class='ant-btn']").click()
    #撤销申请
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='驳 回']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
    #合同管理
    time.sleep(1)
    driver.find_element(By.XPATH,'//span[text()="合同管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//a[text()='合同管理']").click()
    #去除审批中，已通过，选被驳回
    driver.refresh()
    driver.find_element(By.XPATH,"//div[@id='审批状态']/div/span/i").click()
    driver.find_element(By.XPATH,"//div[@id='审批状态']/div//div").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//li[text()='被驳回']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='查 询']/..").click()
    #选第一个被驳回的合同申请单
    time.sleep(1)
    driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/div").click()
    #复制单据
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[@class='ant-btn']").click()
    #更改事由
    driver.find_element(By.XPATH,"//textarea").clear()
    driver.find_element(By.XPATH,"//textarea").send_keys(new_reason)
    #确认提交
    time.sleep(1)
    driver.find_element_by_xpath("//span[text()='确认提交']/..").click()
    #查看详情
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[@class='ant-btn']").click()
    #同意
    time.sleep(1)
    n_text=driver.find_element(By.XPATH,"//span[text()='同 意']/..").text
    return n_text