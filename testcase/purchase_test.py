'''
Created on 2019年4月25日

@author: wx138
'''

import unittest
from selenium import webdriver
from con_nky import common_funcation, purchase
from selenium.webdriver.chrome.options import Options
class Purchase(unittest.TestCase):
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
        self.driver.set_window_size(1400,900)
        common_funcation.login_code(self.driver)
    def tearDown(self):
        self.driver.quit()
    def test_01_PR(self):
        purchase.standard_PR(self.driver)
    def test_11_AT(self):
        purchase.standard_AT(self.driver)
if __name__ == '__main__':
    unittest.main()