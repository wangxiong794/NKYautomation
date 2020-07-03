"""资产卡片"""
from selenium.webdriver.common.by import By
import time
from service.bpm_service.common_funcation import submit, agree, choice_apartment, agree_new
import random
from selenium.webdriver.common.keys import Keys


def choice_ac(driver):  # 选建卡菜单
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='固定资产']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//a[text()='资产卡片']").click()


def start_ac(driver):  # 新建卡片
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//button[text()='新建卡片']").click()


def choice_data(driver):  # 选分类
    # 选资产分类
    time.sleep(3)
    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//tbody/tr[2]/td[1]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//tbody/tr[3]/td[1]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//tbody/tr[4]/td[1]/div/label/span/input").click()
    # 下一步
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()


def edit_ac(driver):  # 编辑资产卡片
    # 资产名称
    time.sleep(1)
    # driver.find_element(By.XPATH, "//input[@id='name']/../span/i").click()
    driver.find_element(By.XPATH, "//input[@id='name']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys(str(time.time()))
    # 入账形式
    driver.find_element(By.XPATH, "//div[@id='isEntryAccount']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='未入账']").click()
    driver.find_element(By.XPATH, "//input[@id='useUserId']").click()
    driver.find_element(By.XPATH, "//input[@id='useUserId']").send_keys(Keys.ENTER)
    # 财政资金
    driver.find_element(By.XPATH, "//input[@id='financeFund']").send_keys('100')
    driver.find_element(By.XPATH, "//input[@id='noFinanceFund']").send_keys('100')
    # 使用年限
    driver.find_element(By.XPATH, "//input[@id='deadline']").send_keys('840')


def choice_FASI(driver):  # 选资产入库的菜单到入库单列表
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='固定资产']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//a[text()='资产入库']").click()
    driver.refresh()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[text()='入库单']").click()


def start_FASI(driver):  # 新增入库单
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='新增入库']/..").click()


def edit_FASI(driver):  # 编辑入库单
    time.sleep(0.5)
    choice_operuser(driver)  # 选采购经办人
    # 选审批流程
    driver.find_element(By.XPATH, "//div[@id='billFlowDefineId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='固定资产入库申请单自审']").click()


def edit_FASI_detail(driver):  # 手动新增入库明细
    tbody = "//div[text()='资产名称']/../../../../../../../tbody/tr/"
    driver.find_element(By.XPATH, tbody+"td[2]/div").click()
    time.sleep(0.1)
    FASI_name = '入库新增明细' + time.strftime('%m%d%H%M%S')
    driver.find_element(By.XPATH, tbody+"td[2]/div/input").send_keys(FASI_name)
    # 计量单位
    driver.find_element(By.XPATH, tbody+'td[3]/div').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, tbody+'td[3]/div').click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//li[text()='个']").click()
    # 数量
    driver.find_element(By.XPATH, tbody+'td[4]/div').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, tbody+'td[4]/div').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, tbody+'td[4]/div/div/div[2]/input').send_keys('10')
    time.sleep(1)
    # 单价
    driver.find_element(By.XPATH, tbody+'td[5]/div').click()
    driver.find_element(By.XPATH, tbody+'td[5]/div').click()
    time.sleep(1)
    driver.find_element(By.XPATH, tbody+'td[5]/div/div/div[2]/input').send_keys(Keys.BACK_SPACE)
    time.sleep(0.1)
    driver.find_element(By.XPATH, tbody+'td[5]/div/div/div[2]/input').send_keys(Keys.BACK_SPACE)
    time.sleep(0.1)
    driver.find_element(By.XPATH, tbody+'td[5]/div/div/div[2]/input').send_keys(Keys.BACK_SPACE)
    time.sleep(0.1)
    driver.find_element(By.XPATH, tbody+'td[5]/div/div/div[2]/input').send_keys('10')
    # 备注
    time.sleep(0.1)
    driver.find_element(By.XPATH, tbody+'td[7]/div').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, tbody+'td[7]/div').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, tbody+'td[7]/div/input').send_keys('自动生成')


def choice_operuser(driver):  # 选采购经办人
    driver.find_element(By.XPATH, "//div[@id='operUserId']/div/div").click()
    time.sleep(0.5)
    # p_user = ('马化腾', '马云', '李彦宏', '叶伟刚', '张小龙', '张小虎', '张小军')
    # p_user1 = random.sample(p_user, 1)
    # p_user2 = "".join(p_user1)
    # driver.find_element(By.XPATH, "//li[text()='" + p_user2 + "']").click()
    driver.find_element(By.XPATH, "//input[@id='operUserId']").send_keys(Keys.ENTER)


def choice_FART(driver):  # 选退换单的菜单
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='固定资产']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='资产退还']").click()


def start_FART(driver):  # 新增退还
    driver.find_element(By.XPATH, "//span[text()='新增退还']/..").click()


def edit_FART(driver):  # 编辑资产退换单
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@id='backUserId']/div/div").click()
    # 选退还人
    f_user = ('马化腾', '马云', '陈东雪',)
    f_user1 = random.sample(f_user, 1)
    f_user2 = "".join(f_user1)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//li[text()='" + f_user2 + "']").click()
    # 选退换部门
    choice_apartment(driver)
    # 获取制单人
    c_user = driver.find_element(By.XPATH, "//div[@id='createUserName']/div/div").text
    # 输入事由
    c_des = c_user + '为' + f_user2 + '退还' + str(time.time())
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys(c_des)
    # 退还明细
    driver.find_element(By.XPATH, "//*[@id='root']/div/section/section/main/div/div[3]/div[2]/\
    div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[3]/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@aria-label='Close']/../div[2]/div/div/div/div[2]/\
    div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span/label/span/input").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    # 选存放位置
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div/div[3]/div[2]/\
    div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[9]/div').click()
    driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div/div[3]/div[2]/\
    div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[9]/div/div/div/div/div[2]/div/input').send_keys(Keys.ENTER)


def choice_FARP(driver):  # 选菜单
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='固定资产']").click()
    driver.refresh()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//a[text()='资产领用']").click()


def start_FARP(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='新增领用']/..").click()


def edit_FARP(driver):  # 编辑领用单
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@id='consumerUserId']/div/div").click()
    # 选领用人
    f_user = ('马化腾', '马云', '李彦宏', '叶伟刚', '张小龙', '张小虎', '张小军')
    f_user1 = random.sample(f_user, 1)
    f_user2 = "".join(f_user1)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//li[text()='" + f_user2 + "']").click()
    # 选领用部门
    choice_apartment(driver)
    # 获取制单人
    c_user = driver.find_element(By.XPATH, "//div[@id='createdUserId']/div/div/div[1]").text
    # 输入事由
    c_des = c_user + '为' + f_user2 + '领用' + str(time.time())
    driver.find_element(By.XPATH, "//input[@id='description']").send_keys(c_des)
    # 领用明细
    driver.find_element(By.XPATH, "//*[@id='root']/div/section/section/main/div/div[3]/div[2]/\
    div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[3]/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@aria-label='Close']/../div[2]/div/div/div/div[2]/\
    div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span/label/span/input").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    # 选存放位置
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div/div[3]/div[2]/\
    div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[8]/div').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div/div[3]/div[2]/\
    div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[8]/div/div/div/div/div[2]/div/input').send_keys(Keys.ENTER)


def choice_FADT(driver):  # 固定处置单
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='固定资产']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='资产处置']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[text()='处置单']").click()


def start_FADT(driver):  # 新增固定资产处置单
    driver.find_element(By.XPATH, "//span[text()='新增处置']/..").click()


def edit_FADT(driver):  # 编辑基本信息
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//textarea").send_keys('资产处置' + str(time.time()))


def edit_FADT_detail(driver):  # 处置明细f
    # 点资产明细
    driver.find_element(By.XPATH, "//div[@class='ant-table-content']/div[1]/div/table/tbody/tr/td[3]/div").click()
    time.sleep(1)
    # 选第一条资产
    driver.find_element(By.XPATH,
                        "//span[text()='资产编号']/../../../../../../../../div[2]/table/tbody/tr[1]/td["
                        "1]/span/label/span/input").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, "//div[@role='document' and @class='ant-modal ant-modal-confirm "
                            "ant-modal-confirm-confirm']/div[2]/div/div/div[2]/button[2]").click()
    except:
        driver.find_element(By.XPATH,
                            "//div[@role='document' and @class='ant-modal ant-modal-confirm "
                            "ant-modal-confirm-confirm']/div[2]/div/div/div[2]/button[2]").click()


def lowcost_project(driver, assetProperty):  # 新增产品目录
    # 新增在一款产品目录
    time.sleep(1)
    js = 'var q=document.querySelector("#root > div > div > nav > div.antd-pro-components-side-bar-index-nav-content").scrollTo(0,1000)'
    driver.execute_script(js)
    driver.find_element(By.XPATH, "//span[text()='基础数据']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//a[text()='产品目录设置']").click()
    driver.find_element(By.XPATH, "//span[text()='新 增']/..").click()
    time.sleep(0.5)
    # 编辑产品目录
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys(assetProperty + str(time.strftime("%m$d$H%M%S")))
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='specification']").send_keys('型号' + str(time.strftime("%M%S")))
    # 计量单位
    driver.find_element(By.XPATH, "//div[@id='unitId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@id='unitId']/div/div/div/div/input").send_keys(Keys.ENTER)
    # 库存单位
    driver.find_element(By.XPATH, "//div[@id='invenUnitId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@id='invenUnitId']/div/div/div/div/input").send_keys(Keys.ENTER)
    # 参考单价
    driver.find_element(By.XPATH, "//input[@id='price']").send_keys('100')
    # 政采目录
    driver.find_element(By.XPATH, "//div[@id='governmentPurchaseCatalogueId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='governmentPurchaseCatalogueId']").send_keys(Keys.ENTER)
    # 资产性质--低值易耗品
    driver.find_element(By.XPATH, "//div[@id='assetPropertyId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='" + assetProperty + "']").click()
    # 保存并新增
    driver.find_element(By.XPATH, "//span[text()='保 存']/..").click()


def LCSI_01(driver):  # 低值易耗品入库单
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='低值易耗品']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//a[text()='入库管理']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[text()='入库单']").click()
    driver.find_element(By.XPATH, "//span[text()='新增入库单']/..").click()
    time.sleep(0.5)
    # 经办人
    driver.find_element(By.XPATH, "//div[@id='operUserId']/div/div").click()
    p_operuser = ('陈东雪', '雷军', '张小龙', '马云')
    p_operuser = random.sample(p_operuser, 1)
    p_operuser = "".join(p_operuser)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//li[text()='" + p_operuser + "']").click()
    # 备注
    driver.find_element(By.XPATH, "//textarea[@id='remark']").send_keys('automation created ' + str(time.asctime()))
    # 入库明细
    driver.find_element(By.XPATH, "//div[@class='ant-table-content']/div[1]/div/table/tbody/tr/td[3]/div").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/\
    div/div/table/tbody/tr[1]/td/span/label/span/input").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//div[@class='ant-table-content']/div[1]/div/table/tbody/tr/td[9]/div").click()
    driver.find_element(By.XPATH, "//div[@class='ant-table-content']/div[1]/div/table/tbody/tr/td[9]/div/div/div["
                                  "2]/input").send_keys('100')
    submit(driver)
    agree_new(driver)


def LCSO_01(driver):  # 新增领用出库单
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='低值易耗品']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//a[text()='领用出库']").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='+ 新增出库']/..").click()
    # 备注
    driver.find_element(By.XPATH, "//textarea[@id='remark']").send_keys('automation created ' + str(time.asctime()))
    # 出库明细
    driver.find_element(By.XPATH, "//div[@class='ant-table-content']/div[1]/div/table/tbody/tr/td[3]/div").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/\
    div/table/tbody/tr[1]/td/span/label/span/input").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//div[@class='ant-table-content']/div[1]/div/table/tbody/tr/td[6]/div").click()
    driver.find_element(By.XPATH, "//div[@class='ant-table-content']/div[1]/div/table/tbody/tr/td[6]/div/div/div["
                                  "2]/input").send_keys('100')
    submit(driver)
    agree_new(driver)


def FART_01(driver):  # 固定资产出库单
    choice_FART(driver)
    start_FART(driver)
    edit_FART(driver)
    time.sleep(1)
    submit(driver)
    agree(driver)


def FARP_01(driver):  # 固定资产领用单
    choice_FARP(driver)
    start_FARP(driver)
    edit_FARP(driver)
    time.sleep(1)
    submit(driver)
    agree(driver)


def FADT_01(driver):  # 固定资产处置单
    choice_FADT(driver)
    start_FADT(driver)
    edit_FADT(driver)
    edit_FADT_detail(driver)
    submit(driver)
    agree(driver)


def FASI_01(driver):  # 固定资产入库单
    choice_FASI(driver)  # 选菜单
    start_FASI(driver)  # 发起入库
    edit_FASI(driver)  # 编辑入库单基本信息
    edit_FASI_detail(driver)  # 编辑入库单入库明细
    time.sleep(1)
    submit(driver)  # 确认提交
    agree(driver)  # 自审同意


def ac_01(driver):
    choice_ac(driver)
    start_ac(driver)
    choice_data(driver)
    edit_ac(driver)
    submit(driver)
    time.sleep(5)
