'''
Created on 2019年4月24日

@author: wx138
'''
import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from con_nky import common_funcation, constructionProject

class ConstructionProject(unittest.TestCase):

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
    def test_01_DP(self):    
        '''建设项目'''
        constructionProject.DP(self.driver)
    def test_11_BN(self):
        '''中标单位通报'''
        constructionProject.BN(self.driver)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()