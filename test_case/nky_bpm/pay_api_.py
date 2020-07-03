"""

"""
import time
import unittest
from service import login
from service.bpm_service import pay_api


class apply_bpm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cookie = login.get_cookie_login()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_00_BA(self):  # 20.6.28
        """事前申请单发起、撤回、复制、驳回、复制、作废"""
        pay_api.BA_stand_bpm(self.cookie)

    def test_01_BA(self):  # 20.6.28
        """事前申请单发起、通过、报销、核销、关闭"""
        pay_api.BA_bpm2(self.cookie)

    def test_02_BA(self):  # 20.6.28
        """事前申请单发起、通过、采购、验收、报销、核销、关闭"""
        pay_api.BA_bpm3(self.cookie)

    def test_03_BA(self):  # 20.6.28
        """事前申请单发起、通过、采购、合同、报销、核销"""
        pay_api.BA_bpm4(self.cookie)

    def test_11_RI(self):  # 20.6.28
        """无申请报销单发起、撤销、复制、通过、核销"""
        pay_api.ri_bpm1(self.cookie)

    def test_12_RI(self):  # 20.6.28
        """无申请报销申请单发起、通过、作废、删除"""
        pay_api.ri_bpm2(self.cookie)

    # def test_13_RI(self):
    #     """框架协议报销单发起、通过、核销"""
    #     pass


if __name__ == '__main__':
    unittest.main()
