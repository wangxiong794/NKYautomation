# coding=utf-8
import unittest
from service.bpm_service import common_funcation
from service.po_page import assetPage

class po_asset(unittest.TestCase):
    log = common_funcation.caseLog()
    asset = assetPage.asset()

    @classmethod
    def setUpClass(cls) -> None:
        cls.asset.login()

    @classmethod
    def tearDownClass(cls):
        cls.asset.driver.close()

    def setUp(self):
        self.asset.driver.refresh()

    def tearDown(self):
        pass

    # def test_01_FASI(self):
    #     """新增固定资产入库单"""
    #     self.asset.addAssetWarehouse(self.__dict__['_testMethodDoc'])

    # def test_11_FARP(self):
    #     """新增固定资产领用单"""
    #     self.asset.addAssetConsumer(self.__dict__['_testMethodDoc'])

    # def test_21_FARP(self):
    #     """新增固定资产退还单"""
    #     self.asset.addAssetHandBack(self.__dict__['_testMethodDoc'])

    # def test_81_inWarehouse(self):
    #     """新增低值易耗入库单"""
    #     self.asset.addInWarehouse(self.__dict__['_testMethodDoc'])

    def test_91_inWarehouse(self):
        """新增低值易耗领用出库单"""
        self.asset.addOutWarehouse(self.__dict__['_testMethodDoc'])

if __name__ =="__main__":
    unittest.main()
    # a = po_asset()
    # try:
    #     a.setUpClass()
    #     a.setUp()
    #     # a.test_01_FASI()
    #     a.test_11_FARP()
    #     a.tearDown()
    #     a.tearDownClass()
    #
    # except BaseException:
    #     a.tearDownClass()
