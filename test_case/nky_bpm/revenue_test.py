
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from service.bpm_service import revenue, common_funcation
# UI2期改版后可运行


class Revenue(unittest.TestCase):
    """收入管理"""
    # run_again = False

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
        # common_funcation.quit_nky(cls.driver)
        # common_funcation.login_again(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.refresh()

    def tearDown(self):
        pass

    def test_01_CG(self):
        """收费标准单新增、撤销、删除"""
        revenue.cancel_CG(self.driver)

    def test_02_CG(self):
        """收费标准单新增、驳回、复制"""
        revenue.reject_CG(self.driver)

    def test_03_CG(self):
        """收费标准单新增、通过"""
        revenue.standard_CG(self.driver)

    def test_11_RE(self):
        """收费审批单新增、删除"""
        revenue.cancel_RE(self.driver)

    def test_12_RE(self):
        """收费审批单新增、驳回"""
        revenue.reject_RE(self.driver)

    def test_13_RE(self):
        """收费审批单新增、通过"""
        revenue.standard_RE(self.driver)

    def test_21_IC(self):
        """收入登记单新增、撤销、删除"""
        revenue.cancel_IC(self.driver)

    def test_22_IC(self):
        """收入登记单新增、驳回"""
        revenue.reject_IC(self.driver)

    def test_23_IC(self):
        """收入登记单新增、通过"""
        revenue.standard_IC(self.driver)


if __name__ == '__main__':
    unittest.main()
    # a = Revenue()
    # a.setUpClass()
    # a.setUp()
    # a.test_23_IC()
    # a.tearDown()
    # a.tearDownClass()