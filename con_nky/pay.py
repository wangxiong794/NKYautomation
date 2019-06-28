'''支出管理'''
from selenium.webdriver.common.by import By
import time
from con_nky.common_funcation import choice_apartment, submit, agree, RIsubmit
from selenium.webdriver.common.keys import Keys
import random
def choice_BA(driver):
    driver.find_element(By.XPATH,'//span[text()="支出管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//a[text()='经费申请']").click()
    
def start_BA(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//span[text()='+ 发起申请']/..").click()
def choice_budget(driver):#选预算项
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[3]/td[1]/span[2]").click()
    driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[4]/td[1]/label/span[1]/input").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//span[text()='下一步']/..").click()
def edit_money(driver):
    driver.find_element(By.XPATH,"//input[@placeholder='请输入申请金额']").send_keys('100')
    driver.find_element(By.XPATH,"//span[text()='下一步']/..").click()
def edit_matter(driver,testmoney):
    BA_matter="六月零食经费"+str(time.strftime('%m%d%H%M%S'))+testmoney
    driver.find_element(By.XPATH,"//textarea[@id='description']").send_keys(BA_matter)
def fund_train(driver):#在培训经费页面增加培训费
    #培训费
    driver.find_element(By.XPATH,"//a[text()='培训费']").click()
    #日历
    driver.find_element(By.XPATH,"//span[@class='ant-calendar-picker-input ant-input']/input[1]").click()
    driver.find_element(By.XPATH,"//div[@class='ant-calendar-range-part ant-calendar-range-left']/div[2]/div[2]/table/tbody/tr[2]/td[5]/div").click()
    driver.find_element(By.XPATH,"//div[@class='ant-calendar-range-part ant-calendar-range-left']/div[2]/div[2]/table/tbody/tr[2]/td[5]/div").click()
    #地点
    driver.find_element(By.XPATH,"//div[@id='location']").click()
    driver.find_element(By.XPATH,"//input[@id='location']").send_keys('培训地点'+time.strftime('%m%d%H%M%S'))
    driver.find_element(By.XPATH,"//input[@id='location']").send_keys(Keys.ENTER)
    time.sleep(1)
    #住宿费,伙食费，交通费，其他费用
#     driver.find_element(By.XPATH,"//input[@id='lodgingFee']").send_keys('80')
#     driver.find_element(By.XPATH,"//input[@id='foodFee']").send_keys('100')
#     driver.find_element(By.XPATH,"//input[@id='transportFee']").send_keys('100')
#     driver.find_element(By.XPATH,"//input[@id='otherFee']").send_keys('100')
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
#     #住宿费，伙食费，其他费用
#     driver.find_element(By.XPATH,"//input[@id='lodgingFee']").send_keys("100")
#     driver.find_element(By.XPATH,"//input[@id='foodFee']").send_keys("100")
#     driver.find_element(By.XPATH,"//input[@id='otherFee']").send_keys("100")
def fund_labor(driver):#填经费页面加劳务费，labor:劳务
    #劳务费
    driver.find_element(By.XPATH,"//a[text()='劳务费']").click()
    #新增
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//div[@class='footer-btn___1zl3U']").click()    
    #保存
    time.sleep(1)
    driver.find_element(By.XPATH,"//a[text()='保存']").click()
def choice_RI(driver):
    driver.find_element(By.XPATH,'//span[text()="支出管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//a[text()='报销申请']").click()
def start_NORI(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='+ 无申请报销']/..").click()
def start_AGRI(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='+ 发起报销']/..").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//div[@class='ant-tabs-nav ant-tabs-nav-animated']/div[1]/div[3]").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='ant-spin-container']/ul/li[1]/ul/li/a").click()
def choice_paymethod(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//div[@id='paymentMethodId']/div/div").click()
    paymethod=('支票','现金','财政统发','其他')
    paymethod=random.sample(paymethod,1)
    paymethod="".join(paymethod)
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//li[text()='"+paymethod+"']").click()
def standard_BA(driver):
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    edit_money(driver)
    choice_apartment(driver)
    edit_matter(driver,'')
    submit(driver)
    agree(driver)
def choice_one_BA(driver):
    choice_BA(driver)
    start_BA(driver)
    choice_budget(driver)
    time.sleep(0.5)
    testmoney=('培训费','差旅费','会议费','劳务费') 
    testmoney=random.sample(testmoney,1)
    testmoney="".join(testmoney)
    if testmoney=='培训费':
        fund_train(driver)
    elif testmoney == '差旅费':
        fund_travel(driver)
    elif testmoney == '会议费':
        fund_meeting(driver)
    else:
        fund_labor(driver)
    edit_money(driver)
    choice_apartment(driver)
    edit_matter(driver,testmoney)
    submit(driver)
    agree(driver)
def choice_MA(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='关联单据']/..").click()
    time.sleep(0.2)
    driver.find_element(By.XPATH,"//div[@class='ant-table-scroll']/div[2]/table/tbody/tr[1]/td[1]/span/label/span/input").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='确认选择']/..").click()
def standard_NORI(driver):
    choice_RI(driver)
    start_NORI(driver)
    choice_budget(driver)
    i=random.randint(0,1)
    if i == 0:
        mades=''
    if i == 1:
        choice_MA(driver)
        mades='AG'
    edit_money(driver)
    choice_apartment(driver)
    choice_paymethod(driver)
    edit_matter(driver,mades)
    RIsubmit(driver)
    agree(driver)
def standart_AGRI(driver):
    choice_RI(driver)
    start_AGRI(driver)
    choice_budget(driver) 
    i=random.randint(0,1)
    if i == 0:
        mades='AG'
    if i == 1:
        choice_MA(driver)
        mades='AGMA'
    edit_money(driver)
    choice_apartment(driver)
    choice_paymethod(driver)
    edit_matter(driver,mades)
    RIsubmit(driver)
    agree(driver)