# -*- coding: utf-8 -*-
import platform

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class workSpace(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.allTime = """
                                    let mytiming = window.performance.timing;
                                    return mytiming;
                                    """

    def _open(self):
        self.driver.get("http://dev3.neikongyi.com/bureau")

    def _noCache(self):
        userName = self.driver.find_element_by_id("userName")
        action = ActionChains(self.driver)
        action.click(userName).send_keys("admin1").send_keys(Keys.TAB).send_keys("nky2018").send_keys(
            Keys.ENTER).perform()

    def main(self):
        # self.__init__()
        # 调用浏览器打开一个新窗口
        self.driver.execute_script("window.open('','_blank');")
        # 窗口定位到新打开的窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self._open()
        self._noCache()
        allTime = self.driver.execute_script(self.allTime)
        self.driver.execute_script("window.close();")
        # 窗口定位返回旧窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return allTime


# a = platform.architecture()[1]
# if "Windows" in a:
#     print(a)
# else:
#     print("linux")
# a={1,9,5,0}
# print(sorted(a))
