from selenium.webdriver.chrome.options import Options
import unittest
from selenium import webdriver
from service.bpm_service import meeting, common_funcation


class Meeting(unittest.TestCase):
    """重要事项"""

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

    def test_01_MA(self):
        """发起、撤销、删除事项申请"""
        meeting.cancel_MA(self.driver)

    def test_02_MA(self):
        """发起、驳回、复制、通过事项申请"""
        meeting.copy_MA(self.driver)

    def test_03_MA(self):
        """发起、通过、作废事项申请"""
        meeting.invalid_MA(self.driver)

    def test_11_CS(self):
        """新增会签"""
        meeting.CS(self.driver)
# TODO 差会签的撤销、复制、修改。可以参考matter.standard_CS


if __name__ == '__main__':
    unittest.main()
