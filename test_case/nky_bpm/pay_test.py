"""

"""
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from service.bpm_service import common_funcation, pay


class apply(unittest.TestCase):

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

    def test_00_BA(self):  # 20.4.28
        """事前申请单发起、撤回、复制、驳回、复制、作废"""
        pay.standard_BA_copy(self.driver)

    def test_01_BA(self):  # 20.4.28
        """无测算事前申请单发起、通过、报销、核销"""
        pay.standard_BA(self.driver)

    def test_02_BA(self):   # 20.4.27
        """培训费测算事前申请单发起、通过、报销、核销"""
        pay.train_BA_RI(self.driver)

    def test_03_BA(self):   # 20.4.28
        """接待费测算事前申请单发起、通过、报销、核销"""
        pay.official_BA_RI(self.driver)

    def test_04_BA(self):     # 20.4.28
        """会议费测算事前申请单发起、通过、报销、核销"""
        pay.meeting_BA_RI(self.driver)

    def test_05_BA(self):   # 20.4.28
        """差旅费测算事前申请单发起、通过、报销、核销""" 
        pay.travel_BA_RI(self.driver)

    def test_06_BA(self):   # 20.4.28
        """劳务费测算事前申请单发起、通过、报销、核销"""
        pay.labor_BA_RI(self.driver)

    def test_07_BA(self):   # 20.4.28
        """申请明细事前申请单发起、通过。本用于采购，可采购白屏走不下去"""
        pay.apply_detail_BA(self.driver)

    def test_11_RI(self):   # 20.4.28
        """无申请+劳务报销单发起、撤销、复制、通过、核销"""
        pay.standard_NORI(self.driver)

    def test_12_RI(self):   # 20.4.28
        """无申请报销单发起、撤销、复制、通过、核销"""
        pay.standard_NORI1(self.driver)

    def test_13_RI(self):
        """无申请+公务接待报销单发起、撤销、复制、通过、核销"""
        pay.standard_NORI2(self.driver)

    def test_14_RI(self):
        """无申请+劳务报销+公务接待+关联事项报销单发起、撤销、复制、通过、核销"""
        pay.standard_NORI3(self.driver)

    def test_15_RI(self):   # 20.4.28
        """无申请报销单发起、通过、作废、删除"""
        pay.invalid_NO_RI(self.driver)

    def test_16_RI(self):   # 20.4.28
        """无申请+劳务报销单发起、通过、作废、删除"""
        pay.invalid_NO_RI1(self.driver)

    def test_17_RI(self):   # 20.4.28
        """无申请+公务接待报销单发起、通过、作废、删除"""
        pay.invalid_NO_RI2(self.driver)

    def test_21_RI(self):
        """框架协议+劳务报销单发起、通过、核销"""
        pay.standard_AGRI(self.driver)

    def test_22_RI(self):
        """框架协议报销单发起、通过、核销"""
        pay.standard_AGRI(self.driver)

    def test_30_RI(self):
        """发起事前、通过、列表页发起预付、通过、发起报销、通过、核销"""
        pay.IM0(self.driver)

    def test_31_RI(self):
        """发起事前、通过、详情页发起预付、通过、发起报销、通过、核销"""
        pay.IM1(self.driver)

    def test_32_IM(self):
        """发起事前、通过、列表发起预付、撤销、删除"""
        pay.IM2(self.driver)

    def test_33_IM(self):
        """发起事前、通过、详情页发起预付、驳回、删除"""
        pay.IM3(self.driver)


if __name__ == '__main__':
    unittest.main()
