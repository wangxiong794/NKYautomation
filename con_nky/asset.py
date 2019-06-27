'''资产卡片'''
from selenium.webdriver.common.by import By
import time
from con_nky.common_funcation import submit, agree, choice_apartment
import random
from selenium.webdriver.common.keys import Keys
def choice_ac(driver):#选建卡菜单
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='固定资产']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//a[text()='资产卡片']").click()
def start_ac(driver):#新建卡片
    driver.find_element(By.XPATH,"//span[text()='+ 新建卡片']/..").click()
def choice_data(driver):#选分类
    #选资产分类
    time.sleep(1)
    driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/span[2]").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//tbody/tr[2]/td[1]/span[2]").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//tbody/tr[3]/td[1]/span[2]").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//tbody/tr[4]/td[1]/div/label/span/input").click()
    #下一步
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//span[text()='下一步']/..").click()
def edit_ac(driver):#编辑资产卡片
    #资产名称
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@id='name']/../span/i").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys('自动生成卡片'+str(time.time()))
    #入账形式
    driver.find_element(By.XPATH,"//div[@id='isEntryAccount']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//li[text()='未入账']").click()
    #财政资金
    driver.find_element(By.XPATH,"//input[@id='financeFund']").send_keys('100')
    #使用年限
    driver.find_element(By.XPATH,"//input[@id='deadline']").send_keys('840')
def choice_FASI(driver):#选资产入库的菜单到入库单列表
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='固定资产']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//a[text()='资产入库']").click()
    driver.find_element(By.XPATH,"//div[text()='入库单']").click()
def start_FASI(driver):#新增入库单
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//span[text()='新增入库']/..").click()
def edit_FASI(driver):#编辑入库单
    time.sleep(0.5)
    choice_operuser(driver)#选采购经办人
    #选审批流程
    driver.find_element(By.XPATH,"//div[@id='billFlowDefineId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//li[text()='入库单自审']").click()
def edit_FASI_detail(driver):#手动新增入库明细
    driver.find_element(By.XPATH,"//*[@id='root']/div/section/section/main/div/div[3]/\
    div[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[2]/div").click()
    time.sleep(0.1)
    FASI_name='入库新增明细'+time.strftime('%m%d%H%M%S')
    driver.find_element(By.XPATH,"//*[@id='root']/div/section/section/main/div/div[3]/\
    div[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[2]/div/span/input").send_keys(FASI_name)
    #计量单位
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/\
    div[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[3]/div').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/\
    div[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[3]/div').click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//li[text()='个']").click()
    #数量
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/\
    div[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[4]/div').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/\
    div[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[4]/div').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/\
    div[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[4]/div/div/div[2]/input').send_keys('10')
    time.sleep(1)
    #单价
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/\
    div[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[5]/div').click()
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/\
    div[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[5]/div').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/\
    div[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[5]/div/div/div[2]/input').send_keys(Keys.BACK_SPACE)
    time.sleep(0.1)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/\
    div[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[5]/div/div/div[2]/input').send_keys(Keys.BACK_SPACE)
    time.sleep(0.1)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/\
    div[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[5]/div/div/div[2]/input').send_keys(Keys.BACK_SPACE)
    time.sleep(0.1)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/\
    div[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[5]/div/div/div[2]/input').send_keys('10')
    #备注
    time.sleep(0.1)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/\
    div[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[7]/div').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/\
    div[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[7]/div').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/\
    div[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[7]/div/input').send_keys('自动生成')
def choice_operuser(driver):#选采购经办人
    driver.find_element(By.XPATH,"//div[@id='operUserId']/div/div").click()
    time.sleep(0.5)
    p_user=('马化腾','马云','李彦宏','叶伟刚','张小龙','张小虎','张小军')
    p_user1=random.sample(p_user,1)
    p_user2="".join(p_user1)
    driver.find_element(By.XPATH,"//li[text()='"+ p_user2 +"']").click()
def choice_FART(driver):#选退换单的菜单
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='固定资产']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//a[text()='资产退还']").click()
def start_FART(driver):#新增退还
    driver.find_element(By.XPATH,"//span[text()='新增退还']/..").click()
def edit_FART(driver):#编辑资产退换单
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@id='backUserId']/div/div").click()
    #选退还人
    f_user=('马化腾','马云','李彦宏','叶伟刚','张小龙','张小虎','张小军')
    f_user1=random.sample(f_user,1)
    f_user2="".join(f_user1)
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//li[text()='"+ f_user2 +"']").click()
    #选退换部门
    choice_apartment(driver)
    #获取制单人
    c_user=driver.find_element(By.XPATH,"//div[@id='createUserName']/div/div").text
    #输入事由
    c_des=c_user+'为'+f_user2+'退还'+str(time.time())
    driver.find_element(By.XPATH,"//input[@id='description']").send_keys(c_des)
    #退还明细
    driver.find_element(By.XPATH,"//*[@id='root']/div/section/section/main/div/div[3]/div[2]/\
    div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[3]/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@aria-label='Close']/../div[2]/div/div/div/div[2]/\
    div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span/label/span/input").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
    #选存放位置
    time.sleep(3)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div[2]/\
    div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[9]/div').click()
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div[2]/\
    div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[9]/div/div/div/div/div[2]/div/input').send_keys(Keys.ENTER)
def choice_FARP(driver):#选菜单
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='固定资产']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//a[text()='资产领用']").click()
def start_FARP(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='新增领用']/..").click()
def edit_FARP(driver):#编辑领用单
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@id='consumerUserId']/div/div").click()
    #选领用人
    f_user=('马化腾','马云','李彦宏','叶伟刚','张小龙','张小虎','张小军')
    f_user1=random.sample(f_user,1)
    f_user2="".join(f_user1)
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//li[text()='"+ f_user2 +"']").click()
    #选领用部门
    choice_apartment(driver)
    #获取制单人
    c_user=driver.find_element(By.XPATH,"//div[@id='createdUserId']/div/div/div[1]").text
    #输入事由
    c_des=c_user+'为'+f_user2+'领用'+str(time.time())
    driver.find_element(By.XPATH,"//input[@id='description']").send_keys(c_des)
    #领用明细
    driver.find_element(By.XPATH,"//*[@id='root']/div/section/section/main/div/div[3]/div[2]/\
    div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[3]/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@aria-label='Close']/../div[2]/div/div/div/div[2]/\
    div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span/label/span/input").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
    #选存放位置
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div[2]/\
    div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[8]/div').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/section/section/main/div/div[3]/div[2]/\
    div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[8]/div/div/div/div/div[2]/div/input').send_keys(Keys.ENTER)
def choice_LCSI(driver):#低值易耗品入库-选菜单
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//span[text()='低值易耗品']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//a[text()='入库管理']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH,"//div[text()='入库单']").click()
def start_LCSI(driver):#新增入库单
    driver.find_element(By.XPATH,"//span[text()='新增入库单']").click()

def LCSI_01(driver):#低值易耗品入库单
    choice_LCSI(driver)
    start_LCSI(driver)
def FART_01(driver):#固定资产出库单
    choice_FART(driver)
    start_FART(driver)
    edit_FART(driver)
    time.sleep(1)
    submit(driver)
    agree(driver)
def FARP_01(driver):#固定资产领用单
    choice_FARP(driver)
    start_FARP(driver)
    edit_FARP(driver)
    time.sleep(1)
    submit(driver)
    agree(driver)
def FASI_01(driver):#固定资产入库单
    choice_FASI(driver)#选菜单
    start_FASI(driver)#发起入库
    edit_FASI(driver)#编辑入库单基本信息
    edit_FASI_detail(driver)#编辑入库单入库明细
    time.sleep(1)
    submit(driver)#确认提交
    agree(driver)#自审同意
def ac_01(driver):
    choice_ac(driver)
    start_ac(driver)
    choice_data(driver)
    edit_ac(driver)
    submit(driver)
    time.sleep(5)