from selenium.webdriver.chrome.options import Options
import unittest
from selenium import webdriver
from con_nky import revenue, common_funcation
class Revenue(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
#         self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.set_window_size(1400,1000)
        common_funcation.login_code(self.driver)
    def tearDown(self):
        self.driver.quit()
    def test_01_CG(self):
        '''发起收费标准'''    
        revenue.standard_CG(self.driver)
    def test_11_RE(self):
        '''发起收费单'''
        revenue.standard_RE(self.driver)
    def test_21_IC(self):
        '''发起收入登记'''
        revenue.standard_IC(self.driver)
if __name__ == '__main__':
    unittest.main()