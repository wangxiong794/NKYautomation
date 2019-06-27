'''建设项目'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
import time
from con_nky.common_funcation import submit, agree
from selenium.webdriver.common.keys import Keys
def DP(driver):
    #建设项目-项目申报
    driver.find_element(By.XPATH,"//span[text()='建设项目']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//a[text()='项目申报']").click()
    #申报项目
    WebDriverWait(driver,15).until(expected_conditions.element_to_be_clickable((By.XPATH,"//span[text()='+ 申报项目']/..")),'项目申报')
    driver.find_element(By.XPATH,"//span[text()='+ 申报项目']/..").click()
    p_apartment=choice_apartment(driver)
    p_type=choice_projecttype(driver)
    p_manager=choice_manager(driver)
    p_source=choice_capitalsource(driver)
    p_compan=choice_companies(driver)
    p_name=driver.find_element(By.XPATH,"//div[@id='createdUserId']/div/div/div[1]").text
    #项目名称
    project_description=p_name+'为'+p_apartment+'申请的项目,项目类别为'+p_type+',经费来源为'+p_source+'，项目负责人为'+p_manager+'的项目。其拟选公司为：'+p_compan+time.strftime('%F-%H%M%S')
    project_name='由'+p_manager+'负责'+p_apartment+'部门的项目'+time.strftime('%F-%H%M%S')
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys(project_name)
    #概算金额
    project_money=('111111.11','222222.22','333333.33')
    project_money1=random.sample(project_money,1)
    project_money2="".join(project_money1)
    driver.find_element(By.XPATH,"//input[@id='amount']").send_keys(project_money2)
    #审批流程
    driver.find_element(By.XPATH,"//div[@id='billFlowDefineId']/div/div").click()
    driver.find_element(By.XPATH,"//li[text()='项目自审']").click()
    #项目介绍
    driver.find_element(By.XPATH,"//textarea[@id='description']").send_keys(project_description)
    #备注
    project_description1=project_description
    for i in range(1,10):
        i = str(i)
        project_description1=project_description1 + project_description +i
    driver.find_element(By.XPATH,"//textarea[@id='remark']").send_keys(project_description1)
    submit(driver)
    agree(driver)
def choice_apartment(driver):#选部门
    driver.find_element(By.XPATH,"//div[@id='departmentId']/div/div").click()
    p_department=('安全保卫','人事部','教导处','德育处','教科研','工会','财务部')
    p_department1=random.sample(p_department,1)
    p_department2="".join(p_department1)
    driver.find_element(By.XPATH,"//li[text()='"+ p_department2 +"']").click()
    return p_department2
def choice_manager(driver):#项目负责人
    driver.find_element(By.XPATH,"//div[@id='managerId']/div/div").click()
    p_manager=('管理员','马化腾','马云','李彦宏','丁磊','张小龙')
    p_manager1=random.sample(p_manager,1)
    p_manager2="".join(p_manager1)
    time.sleep(1)
    driver.find_element(By.XPATH,"//li[text()='"+ p_manager2 +"']").click()
    return p_manager2
def choice_projecttype(driver):#选项目类别
    driver.find_element(By.XPATH,"//div[@id='buildingItemTypeId']/div/div").click()
    buildingItemType=('标准项目','文本项目','数值项目','包装项目','其他项目')
    buildingItemType1=random.sample(buildingItemType,1)
    buildingItemType2="".join(buildingItemType1)
    driver.find_element(By.XPATH,"//li[text()='"+ buildingItemType2 +"']").click()
    return buildingItemType2
def choice_capitalsource(driver):#选经费来源
    driver.find_element(By.XPATH,"//div[@id='capitalSourceId']/div/div").click()
    p_capitalSource=('全额拨款','定额补助','差额补助','自收自支','经费自筹','非财政补助','经费自理','众筹经费')
    p_capitalSource1=random.sample(p_capitalSource,1)
    p_capitalSource2="".join(p_capitalSource1)
    time.sleep(1)
    driver.find_element(By.XPATH,"//li[text()='"+p_capitalSource2+"']").click()
    return p_capitalSource2
def choice_companies(driver):#拟选公司
    driver.find_element(By.XPATH,"//div[@id='companies']/div/div").click()
    p_companies=('北京行控科技','政法财务中心','天猫超市','这是一个公司特别长吗这是一个公司特别长吗这是一个公司特别长吗这是一个公司特别长吗')
    p_companies1=random.sample(p_companies,1)
    p_companies2="".join(p_companies1)
    time.sleep(1)
    driver.find_element(By.XPATH,"//li[text()='"+p_companies2+"']").click()
    return p_companies2
def choice_supplier(driver):#中标单位
    driver.find_element(By.XPATH,"//div[@id='supplierId']/div/div").click()
    p_supplier=('北京行控科技','政法财务中心','天猫超市','这是一个公司特别长吗这是一个公司特别长吗这是一个公司特别长吗这是一个公司特别长吗')
    p_supplier1=random.sample(p_supplier,1)
    p_supplier2="".join(p_supplier1)
    time.sleep(1)
    driver.find_element(By.XPATH,"//li[text()='"+p_supplier2+"']").click()
def BN(driver):
    #建设项目-中标单位通报
    driver.find_element(By.XPATH,"//span[text()='建设项目']/..").click()
    driver.find_element(By.XPATH,'//a[text()="中标单位通报"]').click()
    #通报中标
    driver.find_element(By.XPATH,"//span[text()='+ 通报中标']/..").click()
    #项目名称
    driver.find_element(By.XPATH,"//div[@id='buildingPermitId']/div/div").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@id='buildingPermitId']/div/div/div/div/input").send_keys(Keys.ENTER)
    #概算金额
    p_amount=('111111.11','222222.22','333333.33','444444.44','555555.55','666666.66','777777.77','888888.88','999999.99')
    p_amount1=random.sample(p_amount,1)
    p_amount2="".join(p_amount1)
    driver.find_element(By.XPATH,"//input[@id='amount']").send_keys(p_amount2)
    choice_apartment(driver)
    choice_purchasetype(driver)
    choice_supplier(driver)
    related_personal(driver)
    submit(driver)
    
def choice_purchasetype(driver):
    driver.find_element(By.XPATH,"//div[@id='purchaseTypeId']/div/div").click()
    purchaseType=('政府采购','自行采购')
    purchaseType1=random.sample(purchaseType,1)
    purchaseType2="".join(purchaseType1)
    driver.find_element(By.XPATH,"//li[text()='"+purchaseType2+"']").click()
    driver.find_element(By.XPATH,"//div[@id='purchaseMethodId']/div/div").click()
    if purchaseType2=='自行采购':
        purchaseMethod=('自行比选','预选供应商','零星采购')
    else:
        purchaseMethod=('邀请招标','竞争性谈判','单一来源','询价','竞争性磋商','公开招标','协议采购')
    purchaseMethod1=random.sample(purchaseMethod,1)
    purchaseMethod2="".join(purchaseMethod1)
    driver.find_element(By.XPATH,"//li[text()='"+purchaseMethod2+"']").click()
def related_personal(driver):
    time.sleep(1)
    js='var q=document.querySelector("#root > div > div > div > div.content___3gQPC.ant-layout-content").scrollTo(0,1000)'
    driver.execute_script(js)
    driver.find_element(By.XPATH,"//div[text()='+ 新增']").click()
    time.sleep(2)
    managerment=('校领导','总务部','安全保卫','人事部','教导处')
    managerment1=random.sample(managerment,1)
    managerment2="".join(managerment1)
    driver.find_element(By.XPATH,"//span[text()='"+managerment2+"']/../../span[2]/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='加入通报']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
    time.sleep(1)