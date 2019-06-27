
'''
框架协议的自审，撤销，驳回，变更
'''
import unittest
from selenium import webdriver
from con_nky import common_funcation,meeting
import time
from selenium.webdriver.chrome.options import Options
class frameworkAgreement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(frameworkAgreement, cls).setUpClass()
    @classmethod
    def tearDownClass(cls):
        super(frameworkAgreement,cls).tearDownClass()
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
#         self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.set_window_size(1366,1000)
        common_funcation.login_code(self.driver)
    def tearDown(self):
        self.driver.quit()
    def test_00_AG(self):#申请框架协议并审核
        '''申请框架协议并审核'''
        meeting.AG(self.driver,'框架协议'+time.strftime('%d%H%M'))
    def test_01_AG(self):#撤销+复制
        '''申请框架协议撤销+复制'''
        meeting.AG_cancel(self.driver,'框架协议'+time.strftime('%d%H%M%S'))
    def test_02_AG(self):#驳回+复制
        '''申请框架协议驳回+复制'''
        meeting.AG_refuse(self.driver,'框架协议'+time.strftime('%d%H%M%S'))    
    def test_03_AG(self):#变更
        '''申请框架协议变更'''
        AG_name1=meeting.AG(self.driver,'框架协议'+time.strftime('%d%H%M%S'))
        meeting.AG_change(self.driver, AG_name1)
    def test_11_MA(self):#自审同意
        '''重要事项自审'''
        meeting.MA_before(self.driver)
        common_funcation.agree(self.driver)  
    def test_12_MA(self):#撤销复制+自审同意
        '''撤销+复制重要事项'''
        MA_name=meeting.MA_before(self.driver)
        meeting.MA2(self.driver, MA_name)
        common_funcation.agree(self.driver) 
    def test_13_MA(self):#驳回复制+自审同意
        '''驳回+复制重要事项'''
        MA_name=meeting.MA_before(self.driver)
        meeting.MA3(self.driver, MA_name)
        common_funcation.agree(self.driver) 
    def test_21_conterSign(self):#发起议事会签
        '''发起议事会签'''
        meeting.countersign(self.driver)
        
if __name__ == '__main__':
    unittest.main()