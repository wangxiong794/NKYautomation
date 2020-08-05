"""
Created on 2019年1月30日

@author: 13348
"""
import unittest
from selenium import webdriver
from service.bpm_service import common_funcation, contract
from selenium.webdriver.chrome.options import Options


class contractQuery(unittest.TestCase):
    """合同管理"""
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

    def test_01_CT(self):
        """发起事前、通过、发起合同、通过、发起报销、通过、领用、核销"""
        contract.BA_CT_RI(self.driver)

    def test_02_CT(self):
        """无申请合同发起、通过、报销、领用、核销"""
        contract.NO_CT_RI(self.driver)

    def test_03_CT(self):
        """无申请合同发起、通过、变更、通过、报销、领用、核销"""
        contract.change_CT_RI(self.driver)

    def test_11_AG(self):
        """协议发起、通过、变更、通过"""
        contract.change_AG(self.driver)


if __name__ == '__main__':
    unittest.main()
