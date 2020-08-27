"""建设项目"""
import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from service.bpm_service import common_funcation, building


# UI二期改版后可使用
class DB(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        cls.driver = webdriver.Chrome(chrome_options=chrome_options)
        # cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(15)
        cls.driver.set_window_size(1920, 1080)
        cls.dp = building.DP(cls.driver)
        cls.bn = building.BN(cls.driver)
        cls.dp.login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.refresh()

    def tearDown(self):
        pass

    def test_01_dp(self):
        """项目申报单发起、通过"""
        self.dp.menu()
        self.dp.addDp()
        self.dp.editDp("项目申报单发起、通过")
        self.dp.submit()
        self.dp.agree()

    def test_02_dp(self):
        """项目申报单发起、驳回"""
        self.dp.menu()
        self.dp.addDp()
        self.dp.editDp("项目申报单发起、驳回")
        self.dp.submit()
        self.dp.refuse()

    def test_03_dp(self):
        """项目申报单发起、撤销、删除"""
        self.dp.menu()
        self.dp.addDp()
        self.dp.editDp("项目申报单发起、撤销、删除")
        self.dp.submit()
        self.dp.cancel()
        self.dp.delBill()

    def test_11_bn(self):
        """发起中标单位通报"""
        self.bn.menu()
        self.bn.addBn()
        self.bn.editBn("发起中标单位通报")
        self.bn.relateUser()
        self.bn.submit()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
