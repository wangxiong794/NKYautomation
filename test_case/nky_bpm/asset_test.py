import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from service.bpm_service import common_funcation, asset

# TODO UI二期后，还需要进行改动


class ASSET(unittest.TestCase):
    """固定资产与低值易耗"""

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        cls.driver = webdriver.Chrome(chrome_options=chrome_options)
        # cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(15)
        cls.driver.set_window_size(1366, 768)
        common_funcation.login_code(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def setUp(self):
        pass
    
    def tearDown(self):
        self.driver.refresh()

    def test_01_product(self):
        """新建低值易耗品产品目录"""
        asset.lowcost_project(self.driver, '低值易耗品')
  
    def test_02_product(self):
        """新增固定资产产品目录"""
        asset.lowcost_project(self.driver, '固定资产')
 
    # def test_11_FASI(self):  # TODO
    #     """手动新增入库单"""
    #     asset.FASI_01(self.driver)
    #
    # def test_21_ac(self):  # TODO
    #     """新增固定资产卡片"""
    #     asset.ac_01(self.driver)
    #
    # def test_31_FART(self):  # TODO
    #     """新增固定资产退换单"""
    #     asset.FART_01(self.driver)
    #
    # def test_41_FARP(self):  # TODO
    #     """新增固定资产退换单"""
    #     asset.FARP_01(self.driver)
    #
    # def test_51_FADT(self):  # TODO
    #     """新增固定资产处置单"""
    #     asset.FADT_01(self.driver)
    #
    # def test_61_LCSI(self):  # TODO
    #     """新增低值易耗入库单"""
    #     asset.LCSI_01(self.driver)
    #
    # def test_71_LCSO(self):  # TODO
    #     """新增低值易耗出库单"""
    #     asset.LCSO_01(self.driver)


if __name__ == '__main__':
    unittest.main()
