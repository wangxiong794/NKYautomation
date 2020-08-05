"""UI二期建设项目"""
from selenium.webdriver.common.by import By
import time
from service.bpm_service.common_funcation import agree, submit, refuse, cancel, delete_bill, con
from selenium.webdriver.common.keys import Keys
import random


class DP(con):
    def menu(self):
        self.choice_menu("建设项目", "项目申报")

    def addDp(self):
        time.sleep(0.5)
        self.dr("//span[text()='申报项目']/..").click()

    def editDp(self, DpDes='项目'):
        time.sleep(0.1)
        # 项目类别
        self.dr("//div[@id='buildingItemTypeId']/div/div").click()
        time.sleep(0.1)
        self.dr("//li[text()='标准项目']").click()
        # 项目负责人
        self.dr("//div[@id='managerId']/div/div").click()
        time.sleep(0.1)
        self.dr("//input[@id='managerId']").send_keys(Keys.ENTER)
        # 经费来源
        self.dr("//div[@id='capitalSourceId']/div/div").click()
        time.sleep(0.1)
        self.dr("//li[text()='全额拨款']").click()
        # 拟选公司
        self.dr("//div[@id='companies']/div/div").click()
        time.sleep(0.1)
        self.dr("//li[text()='永辉超市']").click()
        # 项目名称
        self.dr("//input[@id='name']").send_keys(DpDes)
        # 项目介绍
        self.dr("//textarea[@id='description']").send_keys('test' + str(time.strftime('%m%d%H%M%S')))
        # 备注说明
        self.dr("//textarea[@id='remark']").send_keys('备注' + str(time.strftime('%m%d%H%M%S')))
        # 概算金额
        self.dr("//input[@id='amount']").send_keys('500')


class BN(con):
    def menu(self):
        self.choice_menu("建设项目", "中标单位通报")

    def addBn(self):
        time.sleep(0.5)
        self.dr("//span[text()='通报中标']/..").click()

    def editBn(self, remark="备注"):
        self.dr("//div[@id='buildingPermitId']/div/div").click()
        time.sleep(0.5)
        self.dr("//input[@id='buildingPermitId']").send_keys(Keys.ENTER)
        self.enterDepart()
        # 采购方式
        self.dr("//div[@id='purchaseMethodId']/div/div").click()
        time.sleep(0.5)
        self.dr("//input[@id='purchaseMethodId']").send_keys(Keys.ENTER)
        # 中标单位
        self.dr("//div[@id='supplierId']/div/div").click()
        time.sleep(0.5)
        self.dr("//li[text()='永辉超市']").click()
        # 中标金额
        self.dr("//input[@id='amount']").send_keys('500')
        # 代理机构
        self.dr("//input[@id='proxyOrganization']").send_keys('机构' + str(time.strftime('%m%d%H%M%S')))
        # 备注
        self.dr("//textarea[@id='remark']").send_keys(remark + str(time.strftime('%m%d%H%M%S')))

    def relateUser(self,_department='校领导'):
        time.sleep(0.1)
        self.dr("//button[text()='新增相关人员']").click()
        time.sleep(0.5)
        self.dr("//span[text()='" + _department + "']/../../span[2]/span").click()
        time.sleep(0.1)
        self.dr("//span[text()='加入通报 >']/..").click()
        time.sleep(0.1)
        self.dr("//span[text()='确 定']/..").click()

