# coding=utf-8
import os.path
import unittest
from selenium import webdriver
from get_root_path import root_dir
from service.bpm_service import common_funcation
from service.po_page import budgetApplicationPage
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException


class po_pay(unittest.TestCase):
    # pay = None
    # driver = webdriver.Chrome(executable_path=os.path.join(root_dir, 'chromedriver.exe'))
    pay = budgetApplicationPage.budgetApplication()
    log = common_funcation.caseLog()

    @classmethod
    def setUpClass(cls) -> None:
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # cls.driver = webdriver.Chrome(chrome_options=chrome_options)
        cls.pay.login()

    @classmethod
    def tearDownClass(cls):
        cls.pay.driver.close()

    def setUp(self):
        self.pay.driver.refresh()

    def tearDown(self):
        pass

    def test_po_BA_00(self):  # 20.4.28
        """事前申请单发起、撤回、复制、驳回、复制、通过、作废"""
        self.log.info("用例名称：" + self.__dict__['_testMethodDoc'])
        self.pay.menu()
        self.pay.add_budget()
        self.pay.edit_2()
        self.pay.edit_3(_description=str(self.__dict__['_testMethodDoc']))
        self.pay.button_QRTJ()
        self.pay.button_CKXQ()
    def test_po_a1(self):
        print("this test two")

if __name__ == '__main__':
    # unittest.main()
    a = po_pay()
    try:
        a.setUpClass()
        a.setUp()
        a.test_po_BA_00()
        a.tearDown()
        a.tearDownClass()
    except BaseException:
        a.tearDownClass()
