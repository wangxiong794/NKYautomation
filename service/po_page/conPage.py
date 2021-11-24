# coding=utf-8

"""Page方法的最父级方法"""
import os
import time

from selenium.webdriver.common.by import By

from config import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException, TimeoutException

from get_root_path import root_dir


class page:
    def __init__(self, interface=1):
        if interface == 1:
            self.driver = webdriver.Chrome(os.path.join(root_dir, "chromedriver.exe"))
        else:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.dr = self.driver.find_element
        self.driver.implicitly_wait(15)
        self.driver.set_window_size(1366, 1000)

    def element(self, _filename="", section='test', option='test'):
        try:
            cf = configparser.ConfigParser()
            cf.read(_filename, encoding="utf-8")
            locators = cf.get(section, option).split(':')
            # print(locators)
            locMethod = locators[0]
            locExpression = locators[1]
            element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element(locMethod, locExpression),
                                                          message="定位超时")
            # element = WebDriverWait(self.driver, 5).until(self.driver.find_element_by_xpath(locExpression),message="定位超时")
            return element
        except NoSuchElementException and InvalidArgumentException and TimeoutException:
            self.screenShot()

    def driverSetting(self):
        self.driver.implicitly_wait(15)
        self.driver.set_window_size(1680, 1050)

    @staticmethod
    def readConfig(_option):
        cf = configparser.ConfigParser()
        cf.read('../po_elements/config.ini', encoding="utf-8")
        return cf.get(section='config', option=_option)

    def login(self, _filename=os.path.join(root_dir, 'service//po_elements//conPage.ini'), section='login'):
        self.driver.get(test8)
        time.sleep(1)
        self.element(_filename, section, 'username').send_keys(test8_user)
        self.element(_filename, section, 'password').send_keys(test8_pass)
        self.element(_filename, section, 'org').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[@title='" + test8_org + "']").click()
        self.element(_filename, section, 'loginButton').click()
        welcomeText = str(self.element(_filename, section, 'welcome').text)
        assert "祝您开心每一天" in welcomeText
        self.driver.refresh()

    def screenShot(self, file_name=""):  # 截图
        # img文件夹路径
        img_path = os.path.join(root_dir, "img")
        # logName = os.path.join(img_path, '%s.' % time.strftime('%Y_%m_%d'))
        # img_path = os.path.join(r".\\..\\..\\img")
        # img文件夹不存在，新建该文件夹
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        # 获取当前日期
        local_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # 日期文件夹路径
        date_file_path = os.path.join(img_path, local_date)
        # 日期文件夹不存在，新建该文件夹
        if not os.path.exists(date_file_path):
            os.makedirs(date_file_path)
        # 截图存放路径
        local_time = time.strftime('%Y-%m-%d_%H%M%S', time.localtime(time.time()))
        jt_name = file_name + local_time + '.png'
        jt_path = os.path.join(date_file_path, jt_name)
        try:
            self.driver.get_screenshot_as_file(jt_path)
            print('截图保存成功')
        except TimeoutError:
            print('截图超时，请重新运行')
        print('Screenshot_Path：', jt_path)

    def check_budget_available(self, _number):
        amount_str = "//tbody[@class='ant-table-tbody']/tr[%s]/td[3]/div" % str(_number)
        _amount = str(self.dr(amount_str).text)
        if _amount == "":
            return 0
        else:
            return int(_amount.replace(',', ''))

    def choiceBudget(self, lan_number=1):
        # 判断行的aria-label的中文，若是展开行，则该行为末级项目，需要判断可用金额
        # 若是关闭行，则判断是下一行
        button_type_str = "//tbody[@class='ant-table-tbody']/tr[%s]/td[1]/button"
        project_str = "//tbody[@class='ant-table-tbody']/tr[%s]/td[1]"
        time.sleep(1)
        # try:
        print(button_type_str % str(lan_number))
        l1_str=button_type_str % str(lan_number)
        l1 = str(self.dr(By,l1_str).get_attribute("aria-label"))
        print(l1)

        if l1 == "展开行":
            available_amount = self.check_budget_available(lan_number)
            if available_amount == 0:
                return self.choiceBudget(lan_number + 1)
            else:
                self.dr(project_str % str(lan_number)).click()
                time.sleep(0.1)
                self.dr(project_str % str(lan_number + 1)).click()
        elif l1 == "关闭行":
            print(button_type_str % str(lan_number + 1))
            l2 = str(self.dr(button_type_str % str(lan_number + 1)).get_attribute(
                "aria-label"))
            if l2 == "展开行":
                available_amount = self.check_budget_available(lan_number+2)
                if available_amount == 0:
                    return self.choiceBudget(lan_number + 3)
                else:
                    self.dr(project_str % str(lan_number + 2)).click()
                    time.sleep(0.1)
                    self.dr(project_str % str(lan_number + 3)).click()
            else:
                l3 = str(self.dr(button_type_str % str(lan_number + 2)).get_attribute(
                    "aria-label"))
                if l3 == "展开行":
                    available_amount = self.check_budget_available(lan_number + 3)
                    if available_amount == 0:
                        return self.choiceBudget(lan_number + 4)
                    else:
                        self.dr(project_str % str(lan_number + 3)).click()
                        time.sleep(0.1)
                        self.dr(project_str % str(lan_number + 4)).click()
        time.sleep(0.5)
        self.dr("//span[text()='下一步']/..").click()
        # except NoSuchElementException and InvalidArgumentException and TimeoutException:
        #     self.screenShot()

    def button_QRTJ(self):
        self.element(os.path.join(root_dir, 'service//po_elements/conPage.ini'), 'button', 'button_QRTJ').click()

    def button_CKXQ(self):
        self.element(os.path.join(root_dir, 'service//po_elements/conPage.ini'), 'button', 'button_QRTJ').click()


if __name__ == "__main__":
    c = page()
    c.login()
    c.driver.close()
