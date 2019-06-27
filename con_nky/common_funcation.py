from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import random
from selenium import webdriver
#http://39.106.158.149/nky
nky_url='http://39.106.158.149/nky'
username='chendongxue'
password='nky2018'
def login_code(driver):
    driver.get(nky_url)
    driver.find_element(By.ID,"userName").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element_by_xpath("//button").click()
    time.sleep(1)
    try:
        driver.find_element(By.XPATH,"//img[@id='pm-closeGuideViewButton']").click()
    except:
        pass
def submit(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//span[text()='确认提交']/..").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='查看详情']/..").click()
def RIsubmit(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='确认提交']/..").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//span[text()='确 认']/..").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='查看详情']/..").click()
def agree(driver):
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='同 意']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
def refuse(driver):
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='驳 回']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='ant-modal-content']/div[3]/div/button[2]").click()
def creatuser(driver):
    creatusername=driver.find_element(By.XPATH,"//div[@id='createdUserId']/div/div/div[1]").text
    return creatusername
def pay_apply_menu(driver):
    driver.find_element(By.XPATH,"//span[text()='支出管理']/..").click()
    driver.find_element(By.XPATH,"//a[text()='经费申请']").click()
def pay_reimburse_menu(driver):
    driver.find_element(By.XPATH,"//span[text()='支出管理']/..").click()
    driver.find_element(By.XPATH,"//a[text()='报销申请']").click()
def choice_item(driver):
    driver.find_element(By.XPATH,"//span[text()='+ 发起申请']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[3]/td[1]/span[2]").click()
    driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[4]/td[1]/label/span[1]/input").click()
    js='var q=document.querySelector("#root > div > section > section > main").scrollTo(0,1000)'
    driver.execute_script(js)
    time.sleep(1)
    driver.find_element(By.XPATH,"//button").click()
    time.sleep(1)
def fund_detail(driver):
    time.sleep(1)
    driver.find_element(By.XPATH,"//a[text()='+申请明细']").click()
        #明细内容
    driver.find_element(By.XPATH,"//div[@class='ant-table-scroll']/div/table/tbody/tr[1]/td[2]/div").click()
    driver.find_element(By.XPATH,"//div[@class='ant-table-scroll']/div/table/tbody/tr[1]/td[2]/div/input").send_keys("明细"+time.strftime('%d%H%M'))
        #计量单位
    driver.find_element(By.XPATH,"//div[@class='ant-table-scroll']/div/table/tbody/tr[1]/td[2]/div/input").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='ant-table-scroll']/div/table/tbody/tr[1]/td[3]/div/input").send_keys("份")
        #数量
    driver.find_element(By.XPATH,"//div[@class='ant-table-scroll']/div/table/tbody/tr[1]/td[3]/div/input").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH,"//div[@class='ant-table-scroll']/div/table/tbody/tr[1]/td[4]/div/input").send_keys("1")
        #单价
    driver.find_element(By.XPATH,"//div[@class='ant-table-scroll']/div/table/tbody/tr[1]/td[4]/div/input").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH,"//div[@class='ant-table-scroll']/div/table/tbody/tr[1]/td[5]/div/input").send_keys("10")

def fund_train(driver):#在培训经费页面增加培训费
    #培训费
    driver.find_element(By.XPATH,"//a[text()='培训费']").click()
    #日历
    driver.find_element(By.XPATH,"//span[@class='ant-calendar-picker-input ant-input']/input[1]").click()
    driver.find_element(By.XPATH,"//div[@class='ant-calendar-range-part ant-calendar-range-left']/div[2]/div[2]/table/tbody/tr[2]/td[5]/div").click()
    driver.find_element(By.XPATH,"//div[@class='ant-calendar-range-part ant-calendar-range-left']/div[2]/div[2]/table/tbody/tr[2]/td[5]/div").click()
    #地点
    driver.find_element(By.XPATH,"//div[@id='location']").click()
    driver.find_element(By.XPATH,"//input[@id='location']").send_keys('培训地点'+time.strftime('%D'))
    driver.find_element(By.XPATH,"//input[@id='location']").send_keys(Keys.ENTER)
    time.sleep(1)
    #住宿费,伙食费，交通费，其他费用
    driver.find_element(By.XPATH,"//input[@id='lodgingFee']").send_keys('80')
    driver.find_element(By.XPATH,"//input[@id='foodFee']").send_keys('100')
    driver.find_element(By.XPATH,"//input[@id='transportFee']").send_keys('100')
    driver.find_element(By.XPATH,"//input[@id='otherFee']").send_keys('100')
    #参训人数
    driver.find_element(By.XPATH,"//input[@id='trainingNumber']").send_keys("1")
    #工作人员数
    driver.find_element(By.XPATH,"//input[@id='staffNumber']").send_keys("1")
def fund_travel(driver):#填经费页面增加 差旅费
    #差旅费
    driver.find_element(By.XPATH,"//a[text()='差旅费']").click()
    #日历
    driver.find_element(By.XPATH,"//span[@class='ant-calendar-picker-input ant-input']/input[1]").click()
    driver.find_element(By.XPATH,"//div[@class='ant-calendar-range-part ant-calendar-range-left']/div[2]/div[2]/table/tbody/tr[2]/td[5]/div").click()
    driver.find_element(By.XPATH,"//div[@class='ant-calendar-range-part ant-calendar-range-left']/div[2]/div[2]/table/tbody/tr[2]/td[5]/div").click()
    #出差地点--第一个地区北京
    driver.find_element(By.XPATH,"//input[@id='addressId']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//ul[@class='ant-cascader-menu']/li[1]").click()
    driver.find_element(By.XPATH,"//input[@id='transportFee']").send_keys('100')
     
def fund_meeting(driver):#填经费页面增加  会议费
    #会议费
    driver.find_element(By.XPATH,"//a[text()='会议费']").click()
    #日历
    driver.find_element(By.XPATH,"//span[@class='ant-calendar-picker-input ant-input']/input[1]").click()
    driver.find_element(By.XPATH,"//div[@class='ant-calendar-range-part ant-calendar-range-left']/div[2]/div[2]/table/tbody/tr[2]/td[5]/div").click()
    driver.find_element(By.XPATH,"//div[@class='ant-calendar-range-part ant-calendar-range-left']/div[2]/div[2]/table/tbody/tr[2]/td[5]/div").click()
    #参会人数
    driver.find_element(By.XPATH,"//input[@id='meetingNumber']").send_keys('1')
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@id='staffNumber']").send_keys("1")
    #住宿费，伙食费，其他费用
    driver.find_element(By.XPATH,"//input[@id='lodgingFee']").send_keys("100")
    driver.find_element(By.XPATH,"//input[@id='foodFee']").send_keys("100")
    driver.find_element(By.XPATH,"//input[@id='otherFee']").send_keys("100")
def fund_labor(driver):#填经费页面加劳务费，labor:劳务
    #劳务费
    driver.find_element(By.XPATH,"//a[text()='劳务费']").click()
    driver.set_window_size(1366,768)
    #新增
    driver.find_element(By.XPATH,"//div[@class='footer-btn___1zl3U']").click()
    #保存
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='保存']").click()
def choice_fund(driver):
    fund_detail(driver)
    fund_labor(driver)
    a=random.randint(1,3)
    if a==1:
        fund_meeting(driver)
    elif a==2:
        fund_train(driver)
    else:
        fund_travel(driver)
    time.sleep(1)
    js='var q=document.querySelector("#root > div > section > section > main").scrollTo(0,0)'
    driver.execute_script(js)
    driver.find_element(By.XPATH,"//input[@placeholder='请输入申请金额']").send_keys('99.99')
    driver.find_element(By.XPATH,"//span[text()='下一步']/..").click()
def pay_apply_submit(driver):
    pay_apartment=choice_apartment(driver)
    pay_des=pay_apartment+'的经费单'+time.strftime('%F-%H%M%S')
    driver.find_element(By.XPATH,"//textarea").send_keys(pay_des)
    driver.find_element(By.XPATH,"//a[text()='+拟选供应商']").click()
    choice_supplier(driver)
    submit(driver)
    return pay_des
def choice_apartment(driver):#选部门
#     p_department2='return p_department2'
#     return p_department2
#     pass
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//div[@id='departmentId']/div/div").click()
    p_department=('安全保卫','人事部','教导处','德育处','教科研','工会','财务部')
    p_department1=random.sample(p_department,1)
    p_department2="".join(p_department1)
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//li[text()='"+ p_department2 +"']").click()
    return p_department2
def choice_supplier(driver):
    a=str(random.randint(10001,10003))
    driver.find_element(By.XPATH,"//tr[@data-row-key='"+a+"']/td[1]/span/label/span/input").click()
    driver.find_element(By.XPATH,"//span[text()='确认选择']/..").click()
def pay_find(driver,pay_des):
    driver.find_element(By.XPATH,"//div[text()='展开']").click()
    driver.find_element(By.XPATH,"//i[@aria-label='图标: close-circle']").click()
    driver.find_element(By.XPATH,"//input[@id='事由']").send_keys(pay_des)
    driver.find_element(By.XPATH,"//span[text()='查 询']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/div").click()
def purchase_edit(driver):
    driver.find_element(By.XPATH,"//span[text()='申请采购']/..").click()
    js='var q=document.querySelector("#root > div > section > section > main").scrollTo(0,1000)'
    driver.execute_script(js)
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='选供应商']/..").click()
    choice_supplier(driver)
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确认提交']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确 认']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='查看详情']/..").click()
    agree(driver)
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

def contract_edit(driver,contract_name):
    driver.find_element(By.XPATH,"//span[text()='申请合同']/..").click()
    driver.find_element_by_xpath("//input[@id='bSupplierName']/../span/button").click()
    choice_supplier(driver)
    choice_contractPurchaseCatalog(driver)
    choice_contractType(driver)
    driver.find_element_by_xpath("//input[@id='name']").send_keys(contract_name)
    driver.find_element(By.XPATH,"//textarea[@id='description']").send_keys(contract_name)
    driver.find_element(By.XPATH,"//div[@class='normal___3yB_h']/div[3]/div[3]/div/div/div[2]/div/button").click()
    money=driver.find_element(By.XPATH,"//label[text()='可用金额']/../../div[2]/div/span/div/div[2]/input").get_attribute("value")
    driver.find_element_by_xpath("//input[@id='amount_1']").send_keys(money)
    submit(driver)
    agree(driver)
def reimburse_edit(driver):
    driver.find_element(By.XPATH,"//span[text()='+ 发起报销']/..").click()
    driver.find_element(By.XPATH,"//div[@class='ant-tabs-nav ant-tabs-nav-animated']/div[1]/div[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='ant-spin-container']/div[1]/ul/li").click()
    submit(driver)
    agree(driver)
def pay_check(driver):
    driver.find_element(By.XPATH,"//span[text()='资金领用']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@id='payeeBankAccount']").click()
    driver.find_element(By.XPATH,"//div[@id='checkOwnerId']/div/div").click()
    a=str(random.randint(1,10))
    driver.find_element(By.XPATH,"//ul[@role='listbox']/li["+a+"]").click()
    driver.find_element(By.XPATH,"//span[text()='确认领用']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='核销预算']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确认核销']/..").click()
    time.sleep(1)
def choice_liucheng(driver,liucheng):
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//div[@id='billFlowDefineId']/div/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//li[text()='"+liucheng+"']").click()
def all_main(driver):
    pay_apply_menu(driver)
    choice_item(driver)
    choice_fund(driver)
    pay_des=pay_apply_submit(driver)
    agree(driver)
    
    pay_apply_menu(driver)
    pay_find(driver, pay_des)
    purchase_edit(driver)
    
    pay_apply_menu(driver)
    time.sleep(1)
    driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/div").click()
    contract_edit(driver,pay_des)
    
    pay_reimburse_menu(driver)
    reimburse_edit(driver)
    pay_find(driver, pay_des)
    pay_check(driver)
if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.implicitly_wait(15)
    login_code(driver)
    all_main(driver)