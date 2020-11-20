import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from service.bpm_service import common_funcation, asset
from service.bpm_service.asset import LowCost, asset, dataAsset


# TODO UI二期后，还需要进行改动


class ASSET(unittest.TestCase):
    """固定资产与低值易耗"""

    @classmethod
    def setUpClass(cls):
        # cls.driver = driver
        cls.driver = webdriver.Chrome()
        cls.lc = LowCost(cls.driver)
        cls.zc = asset(cls.driver)
        cls.dt = dataAsset(cls.driver)
        cls.driver.implicitly_wait(15)
        cls.driver.set_window_size(1920, 1080)
        cls.lc.login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.refresh()

    def tearDown(self):
        pass

    def test_01_product(self):  # TODO
        """新建产品目录、编辑、停用、删除"""
        self.dt.menu()
        nameProduct = self.dt.add()
        # self.dt.edit(nameProduct)
        # msg = self.dt.delProduct()
        # self.assertEqual(msg, '没有找到任何数据哦~')

    def test_11_FASI(self):  # TODO
        """入库单新增、通过、作废、删除"""
        self.zc.menuIn()
        self.zc.addIn()
        self.zc.operator()
        self.zc.remark("入库单新增、通过、作废、删除")
        self.zc.detailIn()
        self.zc.submit()
        self.zc.agree()
        self.zc.menuIn()
        self.zc.inView()
        self.zc.void()
        self.zc.delBill()

    def test_12_FASI(self):
        """入库单新增、驳回"""
        self.zc.menuIn()
        self.zc.addIn()
        self.zc.operator()
        self.zc.remark("入库单新增、驳回")
        self.zc.detailIn()
        self.zc.submit()
        self.zc.refuse()

    def test_13_FASI(self):
        """入库单新增、撤销"""
        self.zc.menuIn()
        self.zc.addIn()
        self.zc.operator()
        self.zc.remark("入库单新增、撤销")
        self.zc.detailIn()
        self.zc.submit()
        self.zc.cancel()

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

    def test_61_LCSI(self):
        """低值易耗入库单发起、通过、作废、删除"""
        self.lc.menu()
        self.lc.add()
        self.lc.operator()
        self.lc.remark("低值易耗入库单发起、通过、作废、删除")
        self.lc.detail(20)
        self.lc.submit()
        self.lc.agree()
        self.lc.menu()
        self.lc.inView()
        self.lc.void()
        self.lc.delBill()

    def test_62_LCSI(self):
        """低值易耗入库单发起、撤销、删除"""
        self.lc.menu()
        self.lc.add()
        self.lc.operator()
        self.lc.remark("低值易耗入库单发起、撤销、删除")
        self.lc.detail(20)
        self.lc.submit()
        self.lc.cancel()
        self.lc.delBill()

    def test_63_LCSI(self):
        """低值易耗入库单发起、驳回"""
        self.lc.menu()
        self.lc.add()
        self.lc.operator()
        self.lc.remark("低值易耗入库单发起、撤销、删除")
        self.lc.detail(20)
        self.lc.submit()
        self.lc.refuse()

    def test_71_LCSO(self):
        """低值易耗入库单发起、通过、出库发起、通过、作废、删除"""
        self.lc.menu()
        self.lc.add()
        self.lc.operator()
        self.lc.remark("低值易耗入库单发起、撤销、删除")
        self.lc.detail(20)
        self.lc.submit()
        self.lc.agree()
        self.lc.menuOut()
        self.lc.addOut()
        self.lc.detailOut()
        self.lc.submit()
        self.lc.agree()
        self.lc.menuOut()
        self.lc.inView()
        self.lc.void()
        self.lc.delBill()

    def test_72_LCSO(self):
        """出库发起、撤销、删除"""
        self.lc.menuOut()
        self.lc.addOut()
        self.lc.detailOut()
        self.lc.submit()
        self.lc.cancel()
        self.lc.delBill()

    def test_73_LCSO(self):
        """出库发起、驳回"""
        self.lc.menuOut()
        self.lc.addOut()
        self.lc.detailOut()
        self.lc.submit()
        self.lc.refuse()
        self.assertIn("outStorageView", self.driver.current_url)


if __name__ == '__main__':
    unittest.main()
    # a = ASSET()
    # a.setUpClass()
    # a.setUp()
    # a.test_13_FASI()
    # a.tearDown()
    # a.tearDownClass()