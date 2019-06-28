
'''
Created on 2019年1月30日

@author: 13348
'''
import unittest
from selenium import webdriver
from con_nky import common_funcation,contract
from selenium.webdriver.chrome.options import Options
class contractQuery(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(contractQuery, cls).setUpClass()
    @classmethod
    def tearDownClass(cls):
        super(contractQuery, cls).tearDownClass()
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
#         self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.set_window_size(1366,1000)
        common_funcation.login_code(self.driver)
    def tearDown(self):
        self.driver.quit()
        #合同申请--报销申请--经费核销 
    def test_01_contract(self):#1期付款计划合同
        '''1期付款计划合同'''
        money=contract.contract_before(self.driver,'I') 
        contract.contract1(self.driver,money)
        contract.contract_after(self.driver) 
    def test_02_contract(self):#2期付款计划合同
        '''2期付款计划合同'''
        money=contract.contract_before(self.driver, "II")
        contract.contract2(self.driver,money)
        contract.contract_after(self.driver)
    def test_03_CT(self):#两期合同+变更
        '''两期合同+变更'''
        money=contract.contract_before(self.driver,"II前")
        contract.contract2(self.driver,money)
        contract.contract_after(self.driver)
        contract.contract_change(self.driver)
    def test_04_CT(self):#撤销合同+复制
        '''撤销合同+复制'''
        money=contract.contract_before(self.driver,"II前")
        contract.contract2(self.driver,money)
        n_text=contract.CT_copy(self.driver,"II后")
        self.assertEqual(n_text,'同 意',msg='复制失败')
    def test_05_CT(self):#驳回+复制
        '''驳回合同+复制'''
        money=contract.contract_before(self.driver,'II前')
        contract.contract2(self.driver,money)
        n_text=contract.CT_refuse(self.driver,'II后')
        self.assertEqual(n_text,'同 意',msg='复制失败')
    def test_06_CT(self):#撤销+复制+讨论
        '''撤销+复制+讨论'''
        money=contract.contract_before(self.driver,"II前")
        contract.contract2(self.driver,money)
        n_text=contract.CT_copy_discussion(self.driver,'II后')
        self.assertEqual(n_text,'暂无数据',msg='复制合同将讨论复制过来了')

if __name__ == '__main__':
    unittest.main()