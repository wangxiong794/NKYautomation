'''

'''
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from con_nky import common_funcation, pay

class apply(unittest.TestCase):

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
#     def test_00_BA_PR_CT_RI(self):
#         pass
#     def test_01_BA(self):
#         '''标准经费申请单'''
#         pay.standard_BA(self.driver)
#     def test_02_BA(self):
#         '''测算经费申请单'''
#         pay.choice_one_BA(self.driver)
#     def test_11_RI(self):
#         '''标准无经费报销单'''
#         pay.standard_NORI(self.driver)
    def test_12_RI(self):
        '''框架协议报销单'''
        pay.standart_AGRI(self.driver)
if __name__ == '__main__':
    unittest.main()
