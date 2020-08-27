import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import random

from service.bpm_service import common_funcation
from service.bpm_service.common_funcation import submit, agree, choiceapartment, choice_menu
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from service.bpm_service.pay import choice_detail_BA, choice_BA, BA_for_PR


def choice_PR(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[text()="采购管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='采购审批']").click()


def choice_AT(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[text()="采购管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='验收管理']").click()


def start_AT(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='发起验收']/..").click()


def choice_PRAT(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/span/label/span/input").click()
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()


def edit_detail(driver, i):
    i = str(i)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[" + i + "]/td[9]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[" + i + "]/td[9]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//div[@class='ant-table-body']/table/tbody/tr[" + i + "]/td[9]/div/div/div/div/div/div/input").send_keys(
        Keys.ENTER)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    try:
        driver.find_element(By.XPATH, "//textarea").send_keys('测试验收' + str(time.time()))
    except:
        i = int(i)
        i = i + 1
        return edit_detail(driver, i)


def edit_AT(driver):
    driver.find_element(By.XPATH, "//button[text()='新增验收人']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[@title='校领导']/../span[2]/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH,
                        "//div[@class='ant-modal-content']/div[2]/div/div[3]/div[1]/div[2]/div[2]/button[1]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()


def start_PR(driver):
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='+ 发起申请']/..").click()


def choice_BAPR(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        "//span[text()='事由']/../../../../../../../../../div[2]/div[2]/div/table/tbody/tr[1]/td/a").click()


def editpurchasedetail(driver):
    time.sleep(0.1)
    # 跳过明细，存在明细则填写信息
    try:
        driver.find_element(By.XPATH, "//a[text()='下一步']").click()
    except NoSuchElementException:
        print("原申请有明细，无法跳过")
        # 获取有多少条明细
        menubody = driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody")
        rowstr = menubody.find_elements_by_tag_name('tr')
        rows = int(len(rowstr))
        js = 'var q = document.querySelector("section:nth-child(2) > div > div > div > div > div > div > div.ant-table-scroll > div").scrollTo(1000,0)'
        driver.execute_script(js)
        for i in range(1, rows + 1):  # 遍历明细输入资产性质及政采目录
            # 资产性质
            i = str(i)
            print(i)
            driver.find_element(By.XPATH,
                                "//div[text()='产品名称']/../../../../../../../tbody/tr[" + i + "]/td[8]/div").click()
            time.sleep(0.1)
            driver.find_element(By.XPATH,
                                "//div[text()='产品名称']/../../../../../../../tbody/tr[" + i + "]/td[8]/div/div/div/div/div/div/input").send_keys(
                Keys.ENTER)
            # 政采目录 # 执行失败 用js代替
            time.sleep(0.1)
            #             driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr["+i+"]/td[9]").click(
            js = 'var q=document.querySelector("#root > div > div > div > div.antd-pro-layouts-basic-layout-layoutContent > div > div:nth-child(1) > div.antd-pro-components-v2-card-card-card > div.antd-pro-components-v2-card-view-card-wrapper > div > section:nth-child(2) > div > div > div > div > div > div > div.ant-table-scroll > div > table > tbody > tr:nth-child(' + i + ') > td:nth-child(9) > div").click()'
            driver.execute_script(js)
            time.sleep(0.1)
            driver.find_element(By.XPATH,
                                "//div[text()='产品名称']/../../../../../../../tbody/tr[" + i + "]/td[9]/div/div/div/div/div[2]/div/input").send_keys(
                Keys.ENTER)
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//button[2]").click()


#     driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[2]/div").click()
#     productname = driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[2]/div/span[1]/input").get_attribute("value")
#     if productname == "":   # 如果不存在明细，手动填写，否则就删除已有明细
#         if applyamount >= 500:    # 金额大于等于500就手动填，否则就跳过不填明细
#             # 产品名称
#             driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[2]/div").click()
#             driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[2]/div/span[1]/input").send_keys("产品"+str(time.strftime("%m%d%H%M%S")))
#             # 型号
#             driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[3]/div").click()
#             driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[3]/div/input").send_keys("XH-"+str(time.strftime("%M%S")))
#             # 计量单位
#             driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[4]/div").click()
#             driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[4]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
#             # 数量
#             driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[5]/div").click()
#             driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[5]/div/div/div/input").send_keys("5")
#             # 单价
#             driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[6]/div").click()
#             driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[6]/div/div/div[2]/input").send_keys("100")
#             # 金额 = 数量 * 单价
#             # 资产性质
#             driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[8]/div").click()
#             driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[8]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
#             # 政采目录
#             driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[9]/div").click()
#             driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[9]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
#             time.sleep(0.1)
#             driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
#         else:
#             try:
#                 driver.find_element(By.XPATH, "//a[text()='下一步']").click()
#             except NoSuchElementException:
#                 print("有采购明细，无法跳过")
#     else:
#         # noinspection PyBroadException
#         try:
#             driver.find_element(By.XPATH, "//div[text()='产品名称']/../../../../../../../tbody/tr[1]/td[10]/a").click()
#         except Exception:
#             print("删除采购明细出错")


def choice_PRlogid(driver):  # 选采购品目
    driver.find_element(By.XPATH, "//div[@id='purchaseCatalogId']/div/div").click()
    PRlog = ('货物类 ', '工程类', '服务类')
    PRlog = random.sample(PRlog, 1)
    PRlog = "".join(PRlog)
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='" + PRlog + "']").click()


def choice_purchaseMethod(driver):  # 选采购方式
    driver.find_element(By.XPATH, "//div[@id='purchaseMethodId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='purchaseMethodId']").send_keys(Keys.ENTER)


def choice_supplier(driver):  # 选供应商
    tbody = "//div[text()='供应商名称']/../../../../../../../tbody/"
    driver.find_element(By.XPATH, tbody+"tr/td[2]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//tr[@data-row-key='Supplier10000']").click()
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, tbody+"tr/td[5]/div").click()
    time.sleep(0.5)
    # driver.find_element(By.XPATH, "//li[text()='丁磊']").click()
    driver.find_element(By.XPATH, tbody + "tr/td[5]/div/div/div/div/ul/li/div/input").send_keys(Keys.ENTER)
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//a[text()='采选']").click()


def sure_supplier(driver):  # 已经有一条供应商，只需要采选即可
    js = 'var q = document.querySelector("#globalLayoutContent").scrollTo(0,1000)'
    driver.execute_script(js)
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div/div/div/div[2]/div/div/div[5]/div[2]/div/section[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[5]/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[text()='丁磊']").click()
    driver.find_element(By.XPATH, "//a[text()='采选']").click()


def edit_PR(driver):
    time.sleep(0.1)
    choice_purchaseMethod(driver)
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//textarea[@id='procurement']").send_keys('采购' + time.strftime('%m%d%H%M%S'))


def start_BA_PR(driver):  # 从详情页发起采购
    choice_BA(driver)
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]/td[3]").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//li[text()='申请采购']").click()


def PR_check_detail(driver):
    driver.refresh()
    time.sleep(0.5)
    js = 'var q=document.querySelector("#globalLayoutContent > div > div:nth-child(1) > ' \
         'div.antd-pro-components-v2-card-card-card > div.antd-pro-components-v2-card-view-card-wrapper > div > ' \
         'section:nth-child(2) > div > div > div > div > div > div > div.ant-table-scroll > div").scrollTo(1000,0) '
    driver.execute_script(js)
    time.sleep(1)
    # driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div/section["
    #                               "2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[8]/div").click()
    driver.find_element(By.XPATH, "//div[text()='资产性质']/../../../../../../../tbody/tr/td[8]/div").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//li[text()='固定资产']").click()
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()


def standard_PR(driver):  # 填写政采目录有问题，点击一下后会，下拉框会立即消失，导致无法选择政采目录
    choice_PR(driver)
    start_PR(driver)
    choice_BAPR(driver)
    editpurchasedetail(driver)
    edit_PR(driver)
    submit(driver)
    agree(driver)


def standard_AT(driver):
    choice_AT(driver)
    start_AT(driver)
    choice_BAPR(driver)
    edit_detail(driver, 1)
    edit_AT(driver)
    time.sleep(0.5)
    driver.execute_script(
        'var q=document.querySelector("#root > div > div > div > div.content___3gQPC.ant-layout-content").scrollTo(0,1000)')
    submit(driver)


def apply_detail_BA_PR(driver):  # 事前申请有明细
    choice_detail_BA(driver)
    start_BA_PR(driver)
    # PR_check_detail(driver)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    edit_PR(driver)
    sure_supplier(driver)  # 资产性质加载不出、会出现白屏
    submit(driver)
    agree(driver)
    choice_PR(driver)
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//tbody/tr[1]").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.01)
    driver.find_element(By.XPATH, "//button[text()='发起验收']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    edit_AT(driver)
    time.sleep(0.5)
    submit(driver)



def no_detail_BA_PR(driver):  # 无明细采购
    BA_for_PR(driver)
    start_BA_PR(driver)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    edit_PR(driver)
    time.sleep(0.5)
    driver.execute_script('var q = document.querySelector("#globalLayoutContent").scrollTo(0,1000)')
    choice_supplier(driver)
    # sure_supplier(driver)
    submit(driver)
    agree(driver)
    choice_menu(driver, "采购管理", "采购审批")
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]/td[1]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='作废']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='删除']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    time.sleep(5)
    # 等待右上角的提示消失

def no_detail_BA_PR1(driver):  # 无明细采购
    BA_for_PR(driver)
    time.sleep(0.5)
    start_BA_PR(driver)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='下一步']/..").click()
    edit_PR(driver)
    time.sleep(0.5)
    driver.execute_script('var q = document.querySelector("#globalLayoutContent").scrollTo(0,1000)')
    choice_supplier(driver)
    # sure_supplier(driver)
    submit(driver)
    agree(driver)
    choice_menu(driver, "采购管理", "采购审批")
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//div[@class='ant-table-body']/table/tbody/tr[1]/td[1]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='作废']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    driver.refresh()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='更多']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='删除']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    common_funcation.login_code(driver)
    apply_detail_BA_PR(driver)