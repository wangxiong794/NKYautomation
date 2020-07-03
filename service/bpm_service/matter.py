"""UI2期后的重要事项"""
import random
import time

from selenium.webdriver.common.keys import Keys

from service.bpm_service.common_funcation import submit, cancel, input_apartment, agree, deletebill, refuse

from selenium.webdriver.common.by import By


def choice_CS(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[text()="重要事项"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='议事会签']").click()


def start_CS(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='+ 发起会签']/..").click()


def choice_date(driver):  # 选会议时间
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[@id='applyDate']/div/input").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[text()='今天']").click()
    meeting_time = driver.find_element(By.XPATH, "//span[@id='applyDate']/div/input").get_attribute('value')


def choice_location(driver):  # 填写会议地点
    # noinspection PyBroadException
    try:
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='location']").click()
        meeting_location = ('北京', '上海', '广州', '深圳', '成都')
        meeting_location1 = random.sample(meeting_location, 1)
        meeting_location2 = "".join(meeting_location1)
        driver.find_element(By.XPATH, "//input[@id='location']").send_keys(
            meeting_location2 + time.strftime('%D-%H%M%S'))
    except Exception:
        print("填写会议地点失败")


def choice_hostuser(driver):  # 选主持人
    driver.find_element(By.XPATH, "//div[@id='hostUserId']/div/div").click()
    # noinspection PyBroadException
    try:
        driver.find_element(By.XPATH, "//input[@id='hostUserId']").send_keys(Keys.ENTER)
    except Exception:
        print("选主持人失败")


def choice_recorduser(driver):
    driver.find_element(By.XPATH, "//div[@id='recordUserId']/div/div").click()
    # noinspection PyBroadException
    try:
        driver.find_element(By.XPATH, "//input[@id='recordUserId']").send_keys(Keys.ENTER)
    except Exception:
        print("选记录人失败")


def choice_countersignType(driver):
    driver.find_element(By.XPATH, "//div[@id='countersignTypeId']/div/div").click()
    # noinspection PyBroadException
    try:
        driver.find_element(By.XPATH, "//input[@id='countersignTypeId']").send_keys(Keys.ENTER)
    except Exception:
        print("选会议类型失败")


def meet_related_personal(driver):
    driver.find_element(By.XPATH, "//button[text()='新增参会人员']").click()
    time.sleep(1)
    # noinspection PyBroadException
    try:
        managerment = ('校领导', '总务部', '安全保卫', '人事部', '教导处')
        managerment1 = random.sample(managerment, 1)
        managerment2 = "".join(managerment1)
        driver.find_element(By.XPATH, "//span[text()='" + managerment2 + "']/../../span[2]/span").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[text()='加入参会 >']/..").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    except Exception:
        print("选择参会人员失败")


def editcs(driver):
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//textarea").send_keys("会签" + str(time.strftime('%m%d%H%M%S')))


def modify(driver):  # 修改议事会签
    # noinspection PyBroadException
    try:
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[text()='更多']").click()
        driver.find_element(By.XPATH, "//button[text()='修改内容']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//textarea").send_keys("修改内容")
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//span[text()='确 定']").click()
    except Exception:
        print("修改内容失败")


def copycs(driver):
    # noinspection PyBroadException
    try:
        time.sleep(5)  # 提示信息挡住了操作，需要等待
        driver.find_element(By.XPATH, "//button[text()='复制']").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@id='description']").send_keys("复制")
        driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//textarea").send_keys("复制")
    except Exception:
        print("复制议事会签失败")


def standard_CS(driver):  # 新增议事会签
    choice_CS(driver)
    start_CS(driver)
    choice_date(driver)  # 会议时间
    choice_location(driver)  # 会议地点
    choice_hostuser(driver)  # 主持人
    choice_recorduser(driver)  # 记录人
    choice_countersignType(driver)
    driver.find_element(By.XPATH, "//input[@id='description']").send_keys(
        "会签" + str(time.strftime('%m%d%H%M%S')))  # 会议主题
    meet_related_personal(driver)
    editcs(driver)
    submit(driver)
    modify(driver)


def cancel_CS(driver):  # 撤销、修改、复制会签
    choice_CS(driver)
    start_CS(driver)
    choice_date(driver)  # 会议时间
    choice_location(driver)  # 会议地点
    choice_hostuser(driver)  # 主持人
    choice_recorduser(driver)  # 记录人
    choice_countersignType(driver)
    driver.find_element(By.XPATH, "//input[@id='description']").send_keys(
        "会签" + str(time.strftime('%m%d%H%M%S')))  # 会议主题
    meet_related_personal(driver)
    editcs(driver)
    submit(driver)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    driver.find_element(By.XPATH, "//button[text()='撤销申请']").click()
    modify(driver)
    copycs(driver)
    submit(driver)


"""==============================================================================================================="""


def choiceMA(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[text()="重要事项"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='事项申请']").click()


def startMA(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='+ 发起申请']/..").click()


def editMA(driver):     # 编辑页
    input_apartment(driver)
    driver.find_element(By.XPATH, "//input[@id='amount']").send_keys('500')
    driver.find_element(By.XPATH, "//div[@id='billFlowDefineId']/div/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//li[text()='事项申请单自审']").click()
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys("事项申请"+str(time.strftime('%m%d%H%M%S')))
    driver.find_element(By.XPATH, "//textarea[@id='remark']").send_keys("事项申请备注"+str(time.strftime('%m%d%H%M%S')))


def copyMA(driver):     # 复制单据
    time.sleep(1)
    driver.back()  # 返回上一步操作
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    driver.find_element(By.XPATH, "//button[text()='复制单据']").click()
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys("驳回复制")
    driver.find_element(By.XPATH, "//textarea[@id='remark']").send_keys("驳回复制"+str(time.strftime('%m%d%H%M%S')))


def standard_MA(driver):  # 新增同意事项申请
    choiceMA(driver)
    startMA(driver)
    editMA(driver)
    submit(driver)
    agree(driver)


def cancel_MA(driver):      # 新增申请，撤销删除
    choiceMA(driver)
    startMA(driver)
    editMA(driver)
    submit(driver)
    cancel(driver)
    deletebill(driver)


def reject_MA(driver):      # 新增申请，驳回复制
    choiceMA(driver)
    startMA(driver)
    editMA(driver)
    submit(driver)
    refuse(driver)
    copyMA(driver)
    submit(driver)