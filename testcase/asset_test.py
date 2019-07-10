'''固定资产入库单的用例'''
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from con_nky import common_funcation, asset
class contractQuery(unittest.TestCase):
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
        self.driver.set_window_size(1920,1080)
        common_funcation.login_code(self.driver)
    def test_01_product(self):
        #新建低值易耗品产品目录
        asset.lowcost_project(self.driver, '低值易耗品')
    def test_02_product(self):
        #新增固定资产产品目录
        asset.lowcost_project(self.driver, '固定资产')
    def test_11_FASI(self):
        #手动新增入库单
        asset.FASI_01(self.driver)
    def test_21_ac(self):
        #新增固定资产卡片
        asset.ac_01(self.driver)
    def test_31_FART(self):
        #新增固定资产退换单
        asset.FART_01(self.driver)
    def test_41_FARP(self):
        #新增固定资产退换单
        asset.FARP_01(self.driver)
    def test_51_FADT(self):
        #新增固定资产处置单
        asset.FADT_01(self.driver)
    def test_61_LCSI(self):
        #新增低值易耗入库单
        asset.LCSI_01(self.driver)
    def test_71_LCSO(self):
        #新增低值易耗入库单
        asset.LCSO_01(self.driver)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()