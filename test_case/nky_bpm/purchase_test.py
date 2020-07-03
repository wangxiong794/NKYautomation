

import unittest
from selenium import webdriver
from service.bpm_service import common_funcation, purchase
from selenium.webdriver.chrome.options import Options


class Purchase(unittest.TestCase):
    """采购管理"""
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        cls.driver = webdriver.Chrome(chrome_options=chrome_options)
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(15)
        cls.driver.set_window_size(1400, 900)
        common_funcation.login_code(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.refresh()

    def tearDown(self):
        pass

    def test_01_PR(self):
        """发起有明细事前单通过、发起采购、通过、验收"""
        purchase.apply_detail_BA_PR(self.driver)

    def test_02_PR(self):
        """无明事前单发起、通过、发起采购、通过、作废、删除"""
        purchase.no_detail_BA_PR(self.driver)

    def test_03_PR(self):
        """无明事前单发起、通过、发起采购、通过、驳回、删除"""
        purchase.no_detail_BA_PR1(self.driver)

if __name__ == '__main__':
    unittest.main()
