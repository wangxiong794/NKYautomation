# coding=utf-8
import unittest
from service.bpm_service import common_funcation
from service.po_page import matterApplyPage

class po_asset(unittest.TestCase):
    log = common_funcation.caseLog()
    asset = matterApplyPage.matterApply()

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

    def test_01_FASI(self):
        """新增议事会签单"""
        self.asset.countersign(self.__dict__['_testMethodDoc'])


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
