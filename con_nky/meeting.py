'''重要事项'''
import random
from con_nky.constructionProject import choice_apartment
from con_nky.common_funcation import  submit
'''
Created on 2019年2月14日
框架协议的底层文件
@author: WXYYAJW
'''
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
def AG(driver,AG_name):
    #重要事项--框架协议
    choice_AG(driver)
    #申请框架协议
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='+ 申请框架协议']/..").click()
    #选择申请部门
    driver.find_element(By.XPATH,"//div[text()='请选择申请部门']/..").click()
    driver.find_element(By.XPATH,"//li[text()='党务']").click()
    #合同类型
    driver.find_element(By.XPATH,"//div[text()='请选择合同类型']/..").click()
    driver.find_element(By.XPATH,"//li[text()='仓储保管合同']").click()
    #采购类型
    driver.find_element(By.XPATH,"//div[text()='请选择采购类型']/..").click()
    driver.find_element(By.XPATH,"//li[text()='工程类']").click()
    #审批流程
    driver.find_element(By.XPATH,"//div[text()='请选择审批流程']/..").click()
    driver.find_element(By.XPATH,"//li[text()='协议自审']").click()
       
    #合同名称+事由
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys(AG_name)
    driver.find_element(By.XPATH,"//textarea").send_keys(AG_name)
    #确认提交
    driver.find_element(By.XPATH,"//span[text()='确认提交']/..").click()
    #查看详情+同意
    driver.find_element(By.XPATH,"//span[text()='查看详情']/..").click()
    driver.find_element(By.XPATH,"//span[text()='同 意']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
    return AG_name
def AG_cancel(driver,AG_name):
    #重要事项--框架协议
    choice_AG(driver)
    #申请框架协议
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='+ 申请框架协议']/..").click()
    #选择申请部门
    driver.find_element(By.XPATH,"//div[text()='请选择申请部门']/..").click()
    driver.find_element(By.XPATH,"//li[text()='党务']").click()
    #合同类型
    driver.find_element(By.XPATH,"//div[text()='请选择合同类型']/..").click()
    driver.find_element(By.XPATH,"//li[text()='仓储保管合同']").click()
    #采购类型
    driver.find_element(By.XPATH,"//div[text()='请选择采购类型']/..").click()
    driver.find_element(By.XPATH,"//li[text()='工程类']").click()
    #审批流程
    driver.find_element(By.XPATH,"//div[text()='请选择审批流程']/..").click()
    driver.find_element(By.XPATH,"//li[text()='协议自审']").click()       
    #合同名称+事由
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys(AG_name)
    driver.find_element(By.XPATH,"//textarea").send_keys(AG_name)
    #确认提交
    driver.find_element(By.XPATH,"//span[text()='确认提交']/..").click()
    #查看详情+撤销申请+复制单据
    driver.find_element(By.XPATH,"//span[text()='查看详情']/..").click()
    driver.find_element(By.XPATH,"//span[text()='撤销申请']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
    time.sleep(1)
    driver.refresh()
    driver.find_element(By.XPATH,"//span[text()='复制单据']/..").click()
    #重新设定合同名称和事由
    driver.find_element(By.XPATH,"//input[@id='name']").clear()
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys('复制的'+AG_name)
    driver.find_element(By.XPATH,"//textarea").clear()
    driver.find_element(By.XPATH,"//textarea").send_keys('复制的'+AG_name)
    AG_name=driver.find_element(By.XPATH,"//textarea").text
    #确认提交
    driver.find_element(By.XPATH,"//span[text()='确认提交']/..").click()
    #查看详情+撤销申请+复制单据
    driver.find_element(By.XPATH,"//span[text()='查看详情']/..").click()
    WebDriverWait(driver,15).until(expected_conditions.element_to_be_clickable((By.XPATH,"//span[text()='同 意']/..")),'等同意页面出来')
    driver.find_element(By.XPATH,"//span[text()='同 意']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
    return AG_name
def choice_AG(driver):
    #重要事项--框架协议
    time.sleep(1)
    driver.find_element(By.XPATH,'//span[text()="重要事项"]/..').click()
    driver.find_element(By.XPATH,'//a[text()="框架协议"]').click() 
def AG_refuse(driver,AG_name):#驳回框架协议
    choice_AG(driver)
     
    #申请框架协议
    driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']").click()
    #选择申请部门
    driver.find_element(By.XPATH,"//div[text()='请选择申请部门']/..").click()
    driver.find_element(By.XPATH,"//li[text()='党务']").click()
    #合同类型
    driver.find_element(By.XPATH,"//div[text()='请选择合同类型']/..").click()
    driver.find_element(By.XPATH,"//li[text()='仓储保管合同']").click()
    #采购类型
    driver.find_element(By.XPATH,"//div[text()='请选择采购类型']/..").click()
    driver.find_element(By.XPATH,"//li[text()='工程类']").click()
    #审批流程
    driver.find_element(By.XPATH,"//div[text()='请选择审批流程']/..").click()
    driver.find_element(By.XPATH,"//li[text()='协议自审']").click()
       
    #合同名称+事由
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys(AG_name)
    driver.find_element(By.XPATH,"//textarea").send_keys(AG_name)
    #确认提交
    driver.find_element(By.XPATH,"//span[text()='确认提交']/..").click()
    #查看详情+撤销申请+复制单据
    driver.find_element(By.XPATH,"//span[text()='查看详情']/..").click()
    driver.find_element(By.XPATH,"//span[text()='驳 回']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
    time.sleep(1)
    driver.refresh()
    #重要事项--框架协议
    choice_AG(driver)
    #输入事由+查询
    driver.refresh()
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@id='事由']").clear()
    driver.find_element(By.XPATH,"//input[@id='事由']").send_keys(AG_name)
    #审批状态添加
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@id='审批状态']/div/span/i").click()
    driver.find_element(By.XPATH,"//div[@id='审批状态']").click()
    driver.find_element(By.XPATH,"//li[text()='被驳回']").click()
    driver.find_element(By.XPATH,"//span[text()='查 询']/..").click()
    try:
        #进入详情页+复制单据
        time.sleep(1)
        driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/div").click()
        driver.find_element(By.XPATH,"//span[text()='复制单据']/..").click()
    except:
        pass
    #重新设定合同名称和事由
    driver.find_element(By.XPATH,"//input[@id='name']").clear()
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys('驳回复制的'+AG_name)
    driver.find_element(By.XPATH,"//textarea").clear()
    driver.find_element(By.XPATH,"//textarea").send_keys('驳回复制的'+AG_name)
    AG_name=driver.find_element(By.XPATH,"//textarea").text
    #确认提交
    driver.find_element(By.XPATH,"//span[text()='确认提交']/..").click()
    #查看详情+撤销申请+复制单据
    driver.find_element(By.XPATH,"//span[text()='查看详情']/..").click()
    driver.find_element(By.XPATH,"//span[text()='同 意']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
    return AG_name
def AG_change(driver,AG_name):
    #重要事项--框架协议
    choice_AG(driver)
    #切换高级查询+查询
    driver.refresh()
    #输入事由+查询
    driver.find_element(By.XPATH,"//input[@id='事由']").clear()
    driver.find_element(By.XPATH,"//input[@id='事由']").send_keys(AG_name)
    WebDriverWait(driver,15).until(expected_conditions.element_to_be_clickable((By.XPATH,"//tbody/tr[1]/td[1]/div")))
    driver.find_element(By.XPATH,"//span[text()='查 询']/..").click()
    #进入详情页+复制单据
    time.sleep(3)
    driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/div").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='协议变更']/..").click()        
    #重新设定合同名称+事由
    time.sleep(1)
    long_name=driver.find_element(By.XPATH,"//input[@id='name']").get_attribute('value')
    long_name=int(len(long_name))
    driver.find_element(By.XPATH,"//input[@id='name']").click()
    i=1
    while i < long_name+1:       
        driver.find_element(By.XPATH,"//input[@id='name']").send_keys(Keys.BACK_SPACE)
        i=i+1
    else:
        driver.find_element(By.XPATH,"//input[@id='name']").send_keys('变更的'+AG_name)
        driver.find_element(By.XPATH,"//textarea").clear()
        driver.find_element(By.XPATH,"//textarea").send_keys('变更的'+AG_name)
        AG_new_name=driver.find_element(By.XPATH,"//textarea").text
        #确认提交
        driver.find_element(By.XPATH,"//span[text()='确认提交']/..").click()
        #查看详情+撤销申请+复制单据
        driver.find_element(By.XPATH,"//span[text()='查看详情']/..").click()
        driver.find_element(By.XPATH,"//span[text()='同 意']/..").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
        #重要事项--框架协议
        time.sleep(1)
        WebDriverWait(driver,15).until(expected_conditions.presence_of_element_located((By.XPATH,'//ul/li[7]')),'菜单还未加载出来')
        driver.find_element(By.XPATH,'//ul/li[9]').click()
        driver.find_element(By.XPATH,'//ul/li[9]/div/div/div/a[3]').click()
        #刷新隐藏菜单栏+切换高级查询
        driver.refresh()
#         driver.find_element(By.XPATH,"//i[@class='anticon anticon-filter ant-popover-open']").click()
        time.sleep(1)
        AG_1_name=driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/div").text
        if AG_new_name == AG_1_name:
            print("变更成功")
        else:
            print('变更失败')   
def AG_check(driver,AG_new_name):
    choice_AG(driver)
    #刷新隐藏菜单栏+切换高级查询
    driver.refresh()
#     driver.find_element(By.XPATH,"//i[@class='anticon anticon-filter ant-popover-open']").click()
    #输入事由+查询
    driver.find_element(By.XPATH,"//span[text='重 置']/..").click()
#     len_des=driver.find_element(By.XPATH,"//input[@id='description']").get_attribute('vlaue')
#     if len_des is None:
#         pass
#     else:
#         len_des=int(len(len_des))
#         print(len_des)
#         a=1
#         if len_des == 0:
#             pass
#         else:
#             while a<len_des+1:
#                 driver.find_element(By.XPATH,"//input[@id='description']").send_keys(Keys.BACK_SPACE)
#                 a=a+1
#             else:
#                 pass
#             pass
    driver.find_element(By.XPATH,"//input[@id='事由']").send_keys(AG_new_name)
    driver.find_element(By.XPATH,"//span[text()='查 询']/..").click()
    #获取申请单的数据
    text_=driver.find_element(By.XPATH,"//div[@class='ant-spin-container']/div[2]/div[1]/div[2]/div/a/span").text
    if text_ == AG_new_name:
        print('创建成功，协议名称为：',AG_new_name)
    else:
        print('创建失败',AG_new_name,text_)
'''
事项申请单的相关测试用例
'''

def choice_MA(driver):
    driver.find_element(By.XPATH,'//span[text()="重要事项"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//a[text()='事项申请']").click()
    

def MA_before(driver):
    #重要事项--事项申请
    choice_MA(driver)
    #发起申请
    driver.refresh()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='+ 发起申请']/..").click()
    #使用部门
    ma_apartment=choice_apartment(driver)
    ma_name=driver.find_element(By.XPATH,"//div[@id='createdUserId']/div/div/div[1]").text
    #事由
    MA_name=ma_name+'为'+ma_apartment+'部门做的事项申请单'+time.strftime('%F-%H%M%S')
    ma_remark=MA_name
    for i in range(1,10):
        i=str(i)
        ma_remark=ma_remark+MA_name+i
    driver.find_element(By.XPATH,"//textarea[@id='description']").send_keys(MA_name)
    driver.find_element(By.XPATH,"//textarea[@id='remark']").send_keys(ma_remark)
    submit(driver)
    return MA_name

def MA2(driver,MA_name):#撤销申请
    driver.find_element(By.XPATH,"//span[text()='撤销申请']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
    driver.refresh()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='复制单据']/..").click()
    #更改事由
    driver.find_element(By.XPATH,"//textarea").clear()
    driver.find_element(By.XPATH,"//textarea").send_keys(MA_name+'撤销复制')
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确认提交']/..").click()
    #查看详情
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='查看详情']/..").click()
def MA3(driver,MA_name):#驳回申请
    driver.find_element(By.XPATH,"//span[text()='驳 回']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
    #找到该驳回单据
    time.sleep(1)
    choice_MA(driver)
    #筛选审批状态
    driver.refresh()
#     driver.find_element(By.XPATH,"//div[@id='statusId']/div/span/i").click()
#     driver.find_element(By.XPATH,"//div[@id='statusId']/div//div").click()
#     time.sleep(1)
#     driver.find_element(By.XPATH,"//li[text()='被驳回']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@id='审批状态']/div/span/i").click()
    #检索该事由
    driver.find_element(By.XPATH,"//input[@id='事由']").send_keys(MA_name)
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='查 询']/..").click()
    #选择第一个事由
    time.sleep(1)
    driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/div").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='复制单据']/..").click()
    #更改事由
    driver.find_element(By.XPATH,"//textarea").clear()
    driver.find_element(By.XPATH,"//textarea").send_keys(MA_name+'驳回复制')
    driver.find_element(By.XPATH,"//span[text()='确认提交']/..").click()
    #查看详情
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='查看详情']/..").click()

def countersign(driver):#发起议事会签
    driver.find_element(By.XPATH,"//span[text()='重要事项']/..").click()
    driver.find_element(By.XPATH,"//a[text()='议事会签']").click()
    driver.find_element(By.XPATH,"//span[text()='+ 发起会签']/..").click()
    meet_date=choice_date(driver)#会议时间
    meet_location=choice_location(driver)#会议地点
    meet_hostuser=choice_hostuser(driver)#主持人
    meet_recorduser=choice_recorduser(driver)#记录人
    meet_type=choice_countersigntype(driver)#会议类型
    meet_theme=meet_hostuser+'主持的'+meet_type+time.strftime('%H%M%S')
    meet_description='在'+meet_date+meet_location+'举行的由'+meet_hostuser+'主持的，'+meet_recorduser+'记录的'+meet_type+time.strftime('%H%M%S')
    driver.find_element(By.XPATH,"//textarea").send_keys(meet_theme)#会议主题
    js='var q=document.querySelector("#root > div > div > div > div.content___3gQPC.ant-layout-content").scrollTo(0,1000)'
    driver.execute_script(js)
    meet_related_personal(driver)
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='下一步']/..").click()
    time.sleep(1)
    #输入会议内容
    driver.find_element(By.XPATH,"//textarea[@class='ant-input']").send_keys(meet_description)
    time.sleep(1)
    submit(driver)
    time.sleep(1)
def meet_related_personal(driver):
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[text()='新增']").click()
    time.sleep(2)
    managerment=('校领导','总务部','安全保卫','人事部','教导处')
    managerment1=random.sample(managerment,1)
    managerment2="".join(managerment1)
    driver.find_element(By.XPATH,"//span[text()='"+managerment2+"']/../../span[2]/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='加入参会 >']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='确 定']/..").click()
def meet_asert(driver):
    user_name=driver.find_element(By.XPATH,"//div[@class='right___3YsQ0']/span[3]").text
    meet_name=driver.find_element(By.XPATH,"//div[@class='detail-content___2cApX']").text
    if user_name == meet_name:
        print('议事会签发起成功')
    else:
        return countersign(driver)
def choice_countersigntype(driver):#会议类型
    driver.find_element(By.XPATH,"//div[@id='countersignTypeId']/div/div").click()
    time.sleep(1)
    m_signtype=('行政会','校务会','教代会')
    m_signtype1=random.sample(m_signtype,1)
    m_signtype2="".join(m_signtype1)
    time.sleep(1)
    driver.find_element(By.XPATH,"//li[text()='"+ m_signtype2 +"']").click()
    return m_signtype2
def choice_recorduser(driver):#选记录人
    driver.find_element(By.XPATH,"//div[@id='recordUserId']/div/div").click()
#     time.sleep(1)
#     m_recorduser={'1':'管理员','2':'马化腾','3':'马云','4':'李彦宏','5':'丁磊','6':'张小龙','7':'张小虎','8':'张小军'}
#     m_recorduser1=str(random.randint(1,8))
#     m_recorduser2=m_recorduser[m_recorduser1]
#     m_recorduser1="//body/div[4]/div/div/div/ul/li["+m_recorduser1+"]"
#     time.sleep(1)
#     driver.find_element(By.XPATH,m_recorduser1).click()
#     return m_recorduser2
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@id='recordUserId']/div/div/div[3]/div/input").send_keys(Keys.ENTER)
def choice_hostuser(driver):#选主持人
    driver.find_element(By.XPATH,"//div[@id='hostUserId']/div/div").click()
    time.sleep(1)
    m_hostuser=('管理员','马化腾','马云','李彦宏','丁磊','张小龙','张小虎','张小军')
    m_hostuser1=random.sample(m_hostuser,1)
    m_hostuser2="".join(m_hostuser1)
    time.sleep(1)
    driver.find_element(By.XPATH,"//li[text()='"+ m_hostuser2 +"']").click()
    return m_hostuser2
def choice_date(driver):#选会议时间
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[@id='applyDate']/div/input").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//a[text()='今天']").click()
    meeting_time=driver.find_element(By.XPATH,"//span[@id='applyDate']/div/input").get_attribute('value')
    return meeting_time
def choice_location(driver):#选会议地点
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@id='location']").click()
    meeting_location=('北京','上海','广州','深圳','成都')
    meeting_location1=random.sample(meeting_location,1)
    meeting_location2="".join(meeting_location1)
    driver.find_element(By.XPATH,"//input[@id='location']").send_keys(meeting_location2+time.strftime('%D-%H%M%S'))
    return meeting_location2