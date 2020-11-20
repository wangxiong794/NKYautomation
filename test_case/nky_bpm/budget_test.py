"""
预算调整单的5大类单据自审流程
"""
# 调整申请的5种单据
import unittest
from selenium import webdriver
import time
from service.bpm_service import budget, common_funcation
from selenium.webdriver.chrome.options import Options

amount = '100'


class adjust(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        cls.driver = webdriver.Chrome(chrome_options=chrome_options)
        # cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(15)
        cls.driver.set_window_size(1366, 1000)
        common_funcation.login_code(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.refresh()

    def tearDown(self):
        pass

    def test_01_AD(self):
        """预算追加发起、通过、作废、删除"""
        budget.budget_up(self.driver)

    def test_02_AD(self):
        """预算追加发起、撤销、复制单据、通过"""
        budget.budget_up1(self.driver)

    def test_03_AD(self):
        """预算追加发起、撤销、删除"""
        budget.budget_up2(self.driver)

    def test_04_AD(self):
        """预算追加发起、驳回、删除"""
        budget.budget_up3(self.driver)

    def test_11_AD(self):
        """预算调减发起、通过、作废、删除"""
        budget.budget_down(self.driver)

    def test_12_AD(self):
        """预算调减发起、撤销、复制单据、通过"""
        budget.budget_down1(self.driver)

    def test_13_AD(self):
        """预算调减发起、撤销、删除"""
        budget.budget_down2(self.driver)

    def test_14_AD(self):
        """预算调减发起、驳回、删除"""
        budget.budget_down3(self.driver)

    def test_21_AD(self):
        """无申请报销、发起、核销、核销调减发起、通过、作废、删除"""
        budget.budget_ri_down(self.driver)

    def test_22_AD(self):
        """无申请报销、发起、核销、核销调减发起、撤销、复制单据、通过"""
        budget.budget_ri_down1(self.driver)

    def test_23_AD(self):
        """无申请报销、发起、核销、核销调减发起、撤销、删除"""
        budget.budget_ri_down2(self.driver)

    def test_24_AD(self):
        """无申请报销、发起、核销、核销调减发起、驳回、删除"""
        budget.budget_ri_down3(self.driver)


if __name__ == '__main__':
    unittest.main()
    # a = adjust()
    # a.setUpClass()
    # a.setUp()
    # a.test_21_AD()
    # a.tearDown()
    # a.tearDownClass()