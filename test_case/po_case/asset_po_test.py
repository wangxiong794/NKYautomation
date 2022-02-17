# coding=utf-8
import unittest
from service.bpm_service import common_funcation
from service.po_page import assetPage

class po_asset(unittest.TestCase):
    log = common_funcation.caseLog()
    FASI = assetPage.asset_FASI()

    @classmethod
    def setUpClass(cls) -> None:
        cls.FASI.login()

    @classmethod
    def tearDownClass(cls):
        cls.FASI.driver.close()

    def setUp(self):
        self.FASI.driver.refresh()

    def tearDown(self):
        pass

    def test_01_FASI(self):
        """新增固定资产入库单"""
        self.FASI.addFASI()


if __name__ =="__main__":
    a = po_asset()
    try:
        a.setUpClass()
        a.setUp()
        a.test_01_FASI()
        a.tearDown()
        a.tearDownClass()

    except BaseException:
        a.tearDownClass()
