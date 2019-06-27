'''
预算调整单的5大类单据自审流程
'''
#调整申请的5种单据
import unittest
from selenium import webdriver
import time
from con_nky import budget,common_funcation
from selenium.webdriver.chrome.options import Options
amount='99.99'
class adjust(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
#         self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.set_window_size(1366,768)
        common_funcation.login_code(self.driver)
    def tearDown(self):
        self.driver.quit()
    def test_01_adjust(self):    
        '''预算调整单'''
        budget.adjust_before(self.driver)
        budget.adjust_budget1(self.driver, amount)
        budget.adjust_after(self.driver, "调增+调减"+time.strftime('%d%H%M'))
    def test_02_adjust(self):
        '''预算追加单'''
        budget.adjust_before(self.driver)
        budget.adjust_budget2(self.driver, amount)
        budget.adjust_after(self.driver, "预算追加"+time.strftime("%d%H%M"))
    def test_03_adjust(self):
        '''预算调减单'''
        budget.adjust_before(self.driver)
        budget.adjust_budget3(self.driver, amount)
        budget.adjust_after(self.driver, "预算调减"+time.strftime("%d%H%M"))
    def test_04_adjust(self):
        '''垫支预算调整'''
        budget.adjust_verification(self.driver, amount, "核销金额调整"+time.strftime('%d%H%M'))
    def test_05_adjust(self):
        '''核销金额调减'''
        budget.adjust_verification1(self.driver, amount, '核销金额调减'+time.strftime('%d%H%M'))
if __name__ == '__main__':
    unittest.main()