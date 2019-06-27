'''预算管理'''
from selenium.webdriver.common.by import By
import time
def adjust_before(driver):
    #预算管理》调整申请
    driver.find_element(By.XPATH,"//ul/li[3]").click()
    driver.find_element(By.XPATH,"//ul/li[3]/div/div/div/a[2]").click()
def adjust_budget1(driver,amount):#调增+调减
    #发起预算调整
    driver.find_element(By.XPATH,"//button[@class='ant-btn ant-dropdown-trigger ant-btn-primary']").click()
    #预算调整
    time.sleep(1)
    driver.find_element(By.XPATH,"//li[text()='预算调整']").click()
    #选择预算项
    time.sleep(1)
    driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[2]/td[1]/span[2]").click()
    driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[3]/td[1]/label/span[1]/input").click()
    driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[4]/td[1]/span[2]").click()
    driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[5]/td[1]/label/span[1]/input").click()
    driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']").click()
    #填金额
    driver.find_element(By.XPATH,"//form/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div/div/div/span/span/input").send_keys(amount)
    driver.find_element(By.XPATH,"//form/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div/div/div/span/span/input").send_keys(amount)
    #调增修改为调减
    time.sleep(1)
    driver.find_element(By.XPATH,"//form/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/span/div").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//li[@class='ant-select-dropdown-menu-item']").click()
def adjust_budget2(driver,amount):#预算追加
    #发起预算调整
    driver.find_element(By.XPATH,"//button[@class='ant-btn ant-dropdown-trigger ant-btn-primary']").click()
    #预算追加
    time.sleep(1)
    driver.find_element(By.XPATH,"//li[text()='预算追加']").click()
    #选择预算项
    time.sleep(1)
    driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[2]/td[1]/span[2]").click()
    driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[3]/td[1]/label/span[1]/input").click()
    driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']").click()
    #填金额
    driver.find_element(By.XPATH,"//form/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div/div/div/span/span/input").send_keys(amount)
#     driver.find_element(By.XPATH,"//form/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div/div/div/span/span/input").send_keys(amount)
#     #调增修改为调减
#     driver.find_element(By.XPATH,"//form/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/span/div").click()
#     time.sleep(1)
#     driver.find_element(By.XPATH,"//li[@class='ant-select-dropdown-menu-item']").click()
def adjust_budget3(driver,amount):#预算调减
    #发起预算调整
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='+ 发起预算调整 ']/..").click()
    #预算调减
    driver.find_element(By.XPATH,"//li[text()='预算调减']").click()
    #选择预算项
    time.sleep(1)
    driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[2]/td[1]/span[2]").click()
    driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[3]/td[1]/label/span[1]/input").click()
    driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']").click()
    #填金额
    driver.find_element(By.XPATH,"//form/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div/div/div/span/span/input").send_keys(amount)
    
def adjust_verification(driver,amount,reason):
    #预算管理》调整申请
    driver.find_element(By.XPATH,"//ul/li[3]").click()
    driver.find_element(By.XPATH,"//ul/li[3]/div/div/div/a[2]").click()
    #发起预算调整
    driver.find_element(By.XPATH,"//button[@class='ant-btn ant-dropdown-trigger']").click()
    #垫支预算调整
    time.sleep(1)
    driver.find_element(By.XPATH,"//li[text()='垫支预算调整']").click()
    #选择报销单》第一10报销单
    time.sleep(1)
    driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/span/label/span/input").click()
    #确认选择
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确认选择']/..").click()
    #获取提示信息
    message1=driver.find_element(By.XPATH,"//div[@class='desc___1th_y']").text
    message1=message1[-8:-7]
    if message1=='1':
        time.sleep(1)
        driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[8]/td[1]/span[2]").click()
        driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[9]/td[1]/label/span[1]/input").click()
    elif message1=='3':
        time.sleep(1)
        driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[8]/td[1]/span[2]").click()
        driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[9]/td[1]/label/span[1]/input").click()
    else:
        pass
    try:
        #下一步
        time.sleep(1)
        driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']").click()
    except:
        time.sleep(1)
        driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[8]/td[1]/span[2]").click()
        driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']/tr[9]/td[1]/label/span[1]/input").click()
        driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']").click()

    #调整金额
    driver.find_element(By.XPATH,"//form/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/span/span/input").send_keys(amount)
    driver.find_element(By.XPATH,"//form/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/span/span/input").send_keys(amount)
    #调增修改为调减
    driver.find_element(By.XPATH,"//form/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/span/div").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//li[@class='ant-select-dropdown-menu-item']").click()
    #下一步
    driver.find_element(By.XPATH,"//button[@id='nextBtn']").click()
    #流程
    driver.find_element(By.XPATH,"//div[@id='billFlowDefineId']").click()
    driver.find_element(By.XPATH,"//li[text()='调整自审']").click()
    #事由
    driver.find_element(By.XPATH,"//textarea").send_keys(reason)
    #确认提交
    driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']").click()
    #查看详情
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[@class='ant-btn']").click()
    #同意
    driver.find_element(By.CSS_SELECTOR,"button.ant-btn.ant-btn-primary").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='ant-modal-content']/div[3]/div/button[2]").click()
    time.sleep(1)
    return message1
def adjust_verification1(driver,amount,reason):#核销金额调减
    #预算管理》调整申请
    driver.find_element(By.XPATH,"//ul/li[3]").click()
    driver.find_element(By.XPATH,"//ul/li[3]/div/div/div/a[2]").click()
    #发起预算调整
    driver.find_element(By.XPATH,"//button[@class='ant-btn ant-dropdown-trigger']").click()
    #核销金额调减
    driver.find_element(By.XPATH,"//li[text()='核销金额调减']").click()
    #选择报销单》第一个报销单
    time.sleep(1)
    driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/span/label/span/input").click()
    #确认选择
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确认选择']/..").click()
    #下一步
    driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']").click()
    #调整金额
    driver.find_element(By.XPATH,"//form/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/span/span/input").send_keys(amount)
    #下一步
    driver.find_element(By.XPATH,"//button[@id='nextBtn']").click()
    #流程
    driver.find_element(By.XPATH,"//div[@id='billFlowDefineId']").click()
    driver.find_element(By.XPATH,"//li[text()='调整自审']").click()
    #事由
    driver.find_element(By.XPATH,"//textarea").send_keys(reason)
    #确认提交
    driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']").click()
    #查看详情
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[@class='ant-btn']").click()
    #同意
    driver.find_element(By.CSS_SELECTOR,"button.ant-btn.ant-btn-primary").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='ant-modal-content']/div[3]/div/button[2]").click()
    time.sleep(1)

def adjust_after(driver,reason):
    #下一步
    driver.find_element(By.XPATH,"//button[@id='nextBtn']").click()
    #流程
    driver.find_element(By.XPATH,"//div[@id='billFlowDefineId']/div/div").click()
    driver.find_element(By.XPATH,"//li[text()='调整自审']").click()
    #事由
    driver.find_element(By.XPATH,"//textarea").send_keys(reason)
    #确认提交
    driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']").click()
    #查看详情
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[@class='ant-btn']").click()
    #同意
    driver.find_element(By.CSS_SELECTOR,"button.ant-btn.ant-btn-primary").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='ant-modal-content']/div[3]/div/button[2]").click()
    time.sleep(1)
