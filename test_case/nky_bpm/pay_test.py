"""

"""
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from service.bpm_service import common_funcation, pay
from service.bpm_service.pay import Pay
from service.connectmysql import DB


class apply(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        cls.driver = webdriver.Chrome(chrome_options=chrome_options)
        cls.driver = webdriver.Chrome()
        cls.log = common_funcation.caseLog()
        cls.ba = Pay(cls.driver)
        cls.ba.driverSetting()
        common_funcation.login_code(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.refresh()

    def tearDown(self):
        pass

    def test_00_BA(self):  # 20.4.28
        """事前申请单发起、撤回、复制、驳回、复制、通过、作废"""
        # pay.standard_BA_copy(self.driver)
        self.log.info("用例名称："+self.__dict__['_testMethodDoc'])
        self.ba.menu()
        self.ba.add()
        self.ba.choiceBudget()
        budgetName = self.ba.getBudgetName()
        bd = self.ba.budgetData(budgetName)
        self.log.info("预算项初始【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.editMoney('1000')
        self.ba.choicePath('事前申请单自审')
        self.ba.editDescription('事前申请单发起、撤回、复制、驳回、复制、作废')
        self.ba.submit()
        bd = self.ba.budgetData(budgetName)
        self.log.info("提交事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.cancel()
        bd = self.ba.budgetData(budgetName)
        self.log.info("撤销事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.copyCancelBill()
        self.ba.submit()
        bd = self.ba.budgetData(budgetName)
        self.log.info("复制已撤销【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.refuse()
        bd = self.ba.budgetData(budgetName)
        self.log.info("驳回新单据【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.menu()
        self.ba.copyRefuseBill()
        self.ba.submit()
        bd = self.ba.budgetData(budgetName)
        self.log.info("复制被驳回【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.agree()
        bd = self.ba.budgetData(budgetName)
        self.log.info("通过事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.menu()
        self.ba.void()
        bd = self.ba.budgetData(budgetName)
        self.log.info("作废事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))

    def test_01_BA(self):  # 20.4.28
        """无测算事前申请单发起、通过、报销、核销"""
        # pay.standard_BA(self.driver)
        self.log.info("用例名称：" + self.__dict__['_testMethodDoc'])
        self.ba.menu()
        self.ba.add()
        self.ba.choiceBudget()
        budgetName = self.ba.getBudgetName()
        bd = self.ba.budgetData(budgetName)
        self.log.info("预算项初始【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.editMoney('1000')
        self.ba.choicePath('事前申请单自审')
        self.ba.editDescription('无测算事前申请单发起、通过、报销、核销')
        self.ba.submit()
        bd = self.ba.budgetData(budgetName)
        self.log.info("提交事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.agree()
        bd = self.ba.budgetData(budgetName)
        self.log.info("通过事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.menu()
        self.ba.inView()
        self.ba.viewAddReimburse()
        self.ba.editReimburse()
        self.ba.submitReimburse()
        bd = self.ba.budgetData(budgetName)
        self.log.info("提交报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.agree()
        bd = self.ba.budgetData(budgetName)
        self.log.info("通过报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.useCheck()
        bd = self.ba.budgetData(budgetName)
        self.log.info("核销报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))

    def test_02_BA(self):  # 20.4.27
        """培训费测算事前申请单发起、通过、报销、核销"""
        # pay.train_BA_RI(self.driver)
        self.log.info("用例名称：" + self.__dict__['_testMethodDoc'])
        self.ba.menu()
        self.ba.add()
        self.ba.choiceBudget()
        budgetName = self.ba.getBudgetName()
        bd = self.ba.budgetData(budgetName)
        self.log.info("预算项初始【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.trainBA()
        self.ba.editMoney('1000')
        self.ba.choicePath('事前申请单自审')
        self.ba.editDescription(self.__dict__['_testMethodDoc'])
        self.ba.submit()
        self.log.info("提交事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.agree()
        bd = self.ba.budgetData(budgetName)
        self.log.info("通过事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.menu()
        self.ba.inView()
        self.ba.viewAddReimburse()
        self.ba.trainRI()
        self.ba.editReimburse()
        self.ba.submitReimburse()
        bd = self.ba.budgetData(budgetName)
        self.log.info("提交报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.agree()
        bd = self.ba.budgetData(budgetName)
        self.log.info("通过报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.useCheck()
        bd = self.ba.budgetData(budgetName)
        self.log.info("核销报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))

    def test_03_BA(self):  # 20.4.28
        """接待费测算事前申请单发起、通过、报销、核销"""
        # pay.official_BA_RI(self.driver)
        self.log.info("用例名称：" + self.__dict__['_testMethodDoc'])
        self.ba.menu()
        self.ba.add()
        self.ba.choiceBudget()
        budgetName = self.ba.getBudgetName()
        bd = self.ba.budgetData(budgetName)
        self.log.info("预算项初始【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.officialBA()
        self.ba.editMoney('1000')
        self.ba.choicePath('事前申请单自审')
        self.ba.editDescription(self.__dict__['_testMethodDoc'])
        self.ba.submit()
        self.log.info("提交事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.agree()
        bd = self.ba.budgetData(budgetName)
        self.log.info("通过事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.menu()
        self.ba.inView()
        self.ba.viewAddReimburse()
        self.ba.officialRI()
        self.ba.editReimburse()
        self.ba.submitReimburse()
        bd = self.ba.budgetData(budgetName)
        self.log.info("提交报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.agree()
        bd = self.ba.budgetData(budgetName)
        self.log.info("通过报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.useCheck()
        bd = self.ba.budgetData(budgetName)
        self.log.info("核销报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))

    def test_04_BA(self):  # 20.4.28
        """会议费测算事前申请单发起、通过、报销、核销"""
        # pay.meeting_BA_RI(self.driver)
        self.log.info("用例名称：" + self.__dict__['_testMethodDoc'])
        self.ba.menu()
        self.ba.add()
        self.ba.choiceBudget()
        budgetName = self.ba.getBudgetName()
        bd = self.ba.budgetData(budgetName)
        self.log.info("预算项初始【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.meetingBA()
        self.ba.editMoney('1000')
        self.ba.choicePath('事前申请单自审')
        self.ba.editDescription(self.__dict__['_testMethodDoc'])
        self.ba.submit()
        self.log.info("提交事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.agree()
        bd = self.ba.budgetData(budgetName)
        self.log.info("通过事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.menu()
        self.ba.inView()
        self.ba.viewAddReimburse()
        self.ba.meetingRI()
        self.ba.editReimburse()
        self.ba.submitReimburse()
        bd = self.ba.budgetData(budgetName)
        self.log.info("提交报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.agree()
        bd = self.ba.budgetData(budgetName)
        self.log.info("通过报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.useCheck()
        bd = self.ba.budgetData(budgetName)
        self.log.info("核销报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))

    def test_05_BA(self):  # 20.4.28
        """差旅费测算事前申请单发起、通过、报销、核销"""
        # pay.travel_BA_RI(self.driver)
        self.log.info("用例名称：" + self.__dict__['_testMethodDoc'])
        self.ba.menu()
        self.ba.add()
        self.ba.choiceBudget()
        budgetName = self.ba.getBudgetName()
        bd = self.ba.budgetData(budgetName)
        self.log.info("预算项初始【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.travelBA()
        self.ba.editMoney('1000')
        self.ba.choicePath('事前申请单自审')
        self.ba.editDescription(self.__dict__['_testMethodDoc'])
        self.ba.submit()
        self.log.info("提交事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.agree()
        bd = self.ba.budgetData(budgetName)
        self.log.info("通过事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.menu()
        self.ba.inView()
        self.ba.viewAddReimburse()
        self.ba.travelRI()
        self.ba.editReimburse()
        self.ba.submitReimburse()
        bd = self.ba.budgetData(budgetName)
        self.log.info("提交报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.agree()
        bd = self.ba.budgetData(budgetName)
        self.log.info("通过报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.useCheck()
        bd = self.ba.budgetData(budgetName)
        self.log.info("核销报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))

    def test_06_BA(self):  # 20.4.28
        """劳务费测算事前申请单发起、通过、报销、核销"""
        # pay.labor_BA_RI(self.driver)
        self.log.info("用例名称：" + self.__dict__['_testMethodDoc'])
        self.ba.menu()
        self.ba.add()
        self.ba.choiceBudget()
        budgetName = self.ba.getBudgetName()
        bd = self.ba.budgetData(budgetName)
        self.log.info("预算项初始【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.laborBA()
        self.ba.editMoney('2000')
        self.ba.choicePath('事前申请单自审')
        self.ba.editDescription(self.__dict__['_testMethodDoc'])
        self.ba.submit()
        self.log.info("提交事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.agree()
        bd = self.ba.budgetData(budgetName)
        self.log.info("通过事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.menu()
        self.ba.inView()
        self.ba.viewAddReimburse()
        self.ba.laborRI()
        self.ba.editReimburse()
        self.ba.submitReimburse()
        bd = self.ba.budgetData(budgetName)
        self.log.info("提交报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.agree()
        bd = self.ba.budgetData(budgetName)
        self.log.info("通过报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.useCheck()
        bd = self.ba.budgetData(budgetName)
        self.log.info("核销报销单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))

    def test_07_BA(self):  # 20.4.28
        """申请明细事前申请单发起、通过"""
        # pay.apply_detail_BA(self.driver)
        self.log.info("用例名称：" + self.__dict__['_testMethodDoc'])
        self.ba.menu()
        self.ba.add()
        self.ba.choiceBudget()
        budgetName = self.ba.getBudgetName()
        bd = self.ba.budgetData(budgetName)
        self.log.info("预算项初始【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.detailInput()
        self.ba.editMoney('1000')
        self.ba.choicePath('事前申请单自审')
        self.ba.editDescription(self.__dict__['_testMethodDoc'])
        self.ba.submit()
        self.log.info("提交事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))
        self.ba.agree()
        bd = self.ba.budgetData(budgetName)
        self.log.info("通过事前单【预算项：%s，调整后金额：%s，已发生金额：%s，冻结金额：%s，在途金额：%s，可用预算：%s】" %
                      (bd['name'], bd['adjustment'], bd['actual'], bd['frozen'], bd['transit'], bd['available']))

    def test_11_RI(self):  # 20.4.28
        """无申请+劳务报销单发起、撤销、复制、通过、核销"""
        pay.standard_NORI(self.driver)
        # self.log.info("用例名称：" + self.__dict__['_testMethodDoc'])

    def test_12_RI(self):  # 20.4.28
        """无申请报销单发起、撤销、复制、通过、核销"""
        pay.standard_NORI1(self.driver)

    def test_13_RI(self):
        """无申请+公务接待报销单发起、撤销、复制、通过、核销"""
        pay.standard_NORI2(self.driver)

    def test_14_RI(self):
        """无申请+公务接待+关联事项报销单发起、撤销、复制、通过、核销"""
        pay.standard_NORI3(self.driver)

    def test_15_RI(self):  # 20.4.28
        """无申请报销单发起、通过、作废、删除"""
        pay.invalid_NO_RI(self.driver)

    def test_16_RI(self):  # 20.4.28
        """无申请+劳务报销单发起、通过、作废、删除"""
        pay.invalid_NO_RI1(self.driver)

    def test_17_RI(self):  # 20.4.28
        """无申请+公务接待报销单发起、通过、作废、删除"""
        pay.invalid_NO_RI2(self.driver)

    def test_21_RI(self):
        """框架协议+劳务报销单发起、通过、核销"""
        pay.standard_AGRI(self.driver)

    def test_22_RI(self):
        """框架协议报销单发起、通过、核销"""
        pay.standard_AGRI(self.driver)

    def test_30_RI(self):
        """发起事前、通过、列表页发起预付、通过、发起报销、通过、核销"""
        pay.IM0(self.driver)

    def test_31_RI(self):
        """发起事前、通过、详情页发起预付、通过、发起报销、通过、核销"""
        pay.IM1(self.driver)

    def test_32_IM(self):
        """发起事前、通过、列表发起预付、撤销、删除"""
        pay.IM2(self.driver)

    def test_33_IM(self):
        """发起事前、通过、详情页发起预付、驳回、删除"""
        pay.IM3(self.driver)

    def test_41_BA(self):  # TODO
        """标准流程审批"""
        self.ba.menu()
        self.ba.add()
        self.ba.choiceBudget()
        self.ba.budgetMoney()
        self.ba.choicePath('事前申请单')
        self.ba.editDescription('标准流程')
        self.ba.submit()
        name1 = self.ba.nextReviewer('部门负责人')
        self.ba.quit()
        self.ba.reLogin(name1)
        self.ba.menu()
        self.ba.inView()
        self.ba.agree()
        self.ba.assertNkyUrl('dashboard/prcptodo')
        self.ba.menu()
        self.ba.inView()
        name2 = self.ba.nextReviewer('财务负责人')
        self.ba.quit()
        self.ba.reLogin(name2)
        self.ba.menu()
        self.ba.inView()
        self.ba.agree()
        self.ba.assertNkyUrl('dashboard/prcptodo')
        self.ba.menu()
        self.ba.inView()
        name3 = self.ba.nextReviewer('校长')
        self.ba.quit()
        self.ba.reLogin(name3)
        self.ba.menu()
        self.ba.inView()
        self.ba.agree()
        self.ba.menu()
        self.ba.inView()
        self.ba.viewAddReimburse()
        self.ba.editReimburse()
        self.ba.submitReimburse()
        self.ba.agree()
        self.ba.useCheck()


if __name__ == '__main__':
    unittest.main()
    # a = apply()
    # a.setUpClass()
    # a.setUp()
    # a.test_07_BA()
    # a.tearDown()
    # a.tearDownClass()
