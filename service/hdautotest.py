# coding=utf-8
# 华为云海顿测试平台自动执行测试用例
# 初版目前先简单实现，用selenium
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from service.connectmysql import DB

from get_root_path import root_dir


class con:
    _code = 1

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

    def login(self):
        self.driver.get("https://console.huaweicloud.com/haydncsf/?region=cn-north-4#/console/index")
        time.sleep(1)
        self.dr(By.XPATH, "//input[@name='userAccount']").send_keys('cdxkkj')
        self.dr(By.XPATH, "//input[@ht='input_pwdlogin_pwd']").send_keys('neikongyi0203')
        self.dr(By.XPATH, "//span[@class='hwid-text-container']").click()
        time.sleep(1)

    def findWork(self):
        self.dr(By.XPATH, "//span[text()='工作代办']").click()
        self.dr(By.XPATH,
                "/html/body/div[3]/app-root/app-index/div/div/ti-tabs/div[2]/ti-tab[3]/div/app-table-work/div[2]/ti-table/table/tbody/tr[1]/td[7]/a").click()
        time.sleep(1)
        self.dr(By.XPATH,
                "/html/body/div[3]/app-root/layout-default/tp-layout-content/app-list-case/div/div/div[3]/div[2]/ti-table/div/table/tbody/tr[1]/td[13]/ti-actionmenu/ti-menu/a/section[1]").click()
        time.sleep(0.5)
        self.dr(By.XPATH, "//section[text()='执行']/..").click()
        time.sleep(0.5)

    def chooseTestCase(self):
        testState = self.dr(By.XPATH, "//ul[@id='ti_auto_id_207_child_list_0_0_0']/li[" + str(
            self._code) + "]/div/div/span[1]").text
        testName = self.dr(By.XPATH, "//ul[@id='ti_auto_id_207_child_list_0_0_0']/li[" + str(
            self._code) + "]/div/div/span[2]").text
        if testState == "执行完毕":
            self._code += 1
            print("测试用例【 %s 】已经执行" % testName)
            return self.chooseTestCase()
        else:
            self.dr(By.XPATH, "////ul[@id='ti_auto_id_207_child_list_0_0_0']/li[" + str(
                self._code) + "]/div/div/span[2]").click()
            with DB() as db:
                sql = "select case_result from hwtest where case_name='" + testName + "'"
                db.execute(sql)
                case_actual_result = list(db)[0]['case_result']
            self.dr(By.XPATH,
                    "/html/body/div[3]/app-root/layout-default/tp-layout-content/app-exec-case/div/div/div[3]/div[2]/ti-formfield/table/tbody/tr/td[2]/ti-item/ti-table/div/table/tbody/tr/td[4]/div").click()
            time.sleep(0.5)
            iframe = self.dr(By.XPATH,
                             "/html/body/ti-modal-wrapper/div/div/div/app-exccase-modal/ti-modal-footer/ti-formfield/div/div/div[1]/div[2]/ti-item/form/div/editor/div/div[1]/div[2]/div[1]/iframe")
            self.driver.switch_to.frame(iframe)
            self.dr(By.XPATH, "//body/p").send_keys(case_actual_result)
            self.dr(By.XPATH, "//button[text()=' 确定 ']").click()
            self.driver.switch_to.default_content()
            self.dr(By.XPATH,
                    "/html/body/div[3]/app-root/layout-default/tp-layout-content/app-exec-case/div/div/div[3]/div[4]/ti-formfield/table/tbody/tr/td[3]/ti-item/ti-select/ti-dominator/section[1]/section").click()
            self.dr(By.XPATH, "//span[text()='执行完毕']/../..").click()
            self.dr(By.XPATH,
                    "/html/body/div[3]/app-root/layout-default/tp-layout-content/app-exec-case/div/div/div[3]/div[4]/ti-formfield/table/tbody/tr[2]/td[3]/ti-item/ti-select/ti-dominator/section[1]/section").click()
            self.dr(By.XPATH, "//span[text()='通过']/../..").click()
            self.dr(By.XPATH, "//button[text()=' 确定 ']").click()
            self._code += 1


if __name__ == "__main__":
    a = con()
    a.login()
    a.findWork()
    a.chooseTestCase()
    a.driver.quit()
