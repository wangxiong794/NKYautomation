import time
from selenium.webdriver.common.by import By
import random
from con_nky.common_funcation import choice_apartment, submit, agree
from selenium.webdriver.common.keys import Keys
def choice_PR(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,'//span[text()="采购管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//a[text()='采购审批']").click()
def choice_AT(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,'//span[text()="采购管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//a[text()='验收管理']").click()
def start_AT(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='发起验收']/..").click()
def choice_PRAT(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/span/label/span/input").click()
    driver.find_element(By.XPATH,"//span[text()='下一步']/..").click()
def edit_detail(driver,i):
    i=str(i)
    driver.find_element(By.XPATH,"//div[@class='ant-table-body']/table/tbody/tr["+i+"]/td[9]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//div[@class='ant-table-body']/table/tbody/tr["+i+"]/td[9]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//div[@class='ant-table-body']/table/tbody/tr["+i+"]/td[9]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH,"//span[text()='下一步']/..").click()
    try:
        driver.find_element(By.XPATH,"//textarea").send_keys('测试验收'+str(time.time()))
    except:
        i=int(i)
        i=i+1
        return edit_detail(driver, i)    
def edit_AT(driver):
    driver.find_element(By.XPATH,"//div[text()='+ 新增']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[@title='校领导']/../span[2]/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[2]/button[1]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
def start_PR(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='+ 发起申请']/..").click()
def choice_BAPR(driver):
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='ant-table-body']/table/tbody/tr[1]/td[1]/span/label/span/input").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='下一步']/..").click()
def choice_detail(driver):
    time.sleep(0.1)
    i=random.randint(0,1)
    i=0
    if i == 0:
        try:
            driver.find_element(By.XPATH,"//span[text()='跳过']/..").click()
        except:
            driver.execute_script('var q=document.querySelector("#root > div > div > div > div.content___3gQPC.ant-layout-content > div > div.wrapper___2zsno > div.table-wrapper____T-JE > div > div > div > div > div > div.ant-table-fixed-right > div > div > table > tbody > tr > td > a").click(1)')
            driver.find_element(By.XPATH,"//span[text()='跳 过']/..").click()
    else:
        driver.find_element(By.XPATH,"//th[@class='ant-table-fixed-columns-in-body order-box___3sLv3 ant-table-align-center']/../../../tbody/tr/td[2]/div").click()
        time.sleep(0.1)
        driver.find_element(By.XPATH,"//span[@class='ant-input-suffix']/i").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[text()='全部分类']").click()
        time.sleep(0.1)
        a=str(random.randint(1,10))
        driver.find_element(By.XPATH,"//th[@class='ant-table-selection-column']/../../../../../div[2]/table/tbody/tr["+a+"]/td[1]/span/label/span/input").click()
        driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//td[@class='ant-table-fixed-columns-in-body order-box___3sLv3']/../td[5]/div").click()
        time.sleep(0.1)
        driver.find_element(By.XPATH,"//input[@class='ant-input-number-input']").send_keys('1')
        time.sleep(0.1)
        driver.find_element(By.XPATH,"//span[text()='下一步']/..").click()
def choice_PRlogid(driver):#选产品目录
    driver.find_element(By.XPATH,"//div[@id='purchaseCatalogId']/div/div").click()
    PRlog=('货物类 ','工程类','服务类')
    PRlog=random.sample(PRlog,1)
    PRlog="".join(PRlog)
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//li[text()='"+PRlog+"']").click()
def choice_supllier(driver):
    driver.find_element(By.XPATH,"//span[text()='选供应商']/..").click()
    time.sleep(0.1)
    d=str(random.randint(1,3))
    driver.find_element(By.XPATH,"//tbody/tr["+d+"]/td[1]/span/label/span/input").click()
    driver.find_element(By.XPATH,"//span[text()='确认选择']/..").click()
def edit_PR(driver):
    time.sleep(0.1)
    PRapart=choice_apartment(driver)
    choice_PRlogid(driver)
    choice_PRlogid(driver)
#     #清除采购组织方式和采购方式
#     driver.execute_script('var q=document.querySelector("#purchaseTypeId > div > div > ul > li.ant-select-selection__choice > span > i").click(1)')
#     driver.execute_script('var q=document.querySelector("#purchaseMethodId > div > div > ul > li.ant-select-selection__choice > span > i").click(1)')
#     #选采购组织方式和采购方式
#     driver.execute_script('var q=document.querySelector("#purchaseTypeId > div > div > div").click(1)')
#     c=random.randint(0,2)
#     if c==0:
#         time.sleep(1)
#         driver.find_element(By.XPATH,"li[text()='自行采购']").click()
#     elif c==1:
#         time.sleep(1)
#         driver.find_element(By.XPATH,"li[text()='政府采购']").click()
#     else:
#         time.sleep(1)
#         driver.find_element(By.XPATH,"li[text()='自行采购']").click()
#         driver.find_element(By.XPATH,"li[text()='政府采购']").click()
    time.sleep(0.1)
    PRapart=PRapart+'的采购单'+time.strftime('%m%d%H%M%S')
    driver.find_element(By.XPATH,"//textarea[@id='procurement']").send_keys(PRapart)
    choice_supllier(driver)
def standard_PR(driver):
    choice_PR(driver)
    start_PR(driver)
    choice_BAPR(driver)
    choice_detail(driver)
    edit_PR(driver)
    submit(driver)
    agree(driver)

def standard_AT(driver):
    choice_AT(driver)
    start_AT(driver)
    choice_BAPR(driver)
    edit_detail(driver,1)
    edit_AT(driver)
    time.sleep(0.5)
    driver.execute_script('var q=document.querySelector("#root > div > div > div > div.content___3gQPC.ant-layout-content").scrollTo(0,1000)')
    submit(driver)