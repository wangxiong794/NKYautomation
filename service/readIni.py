# coding=utf-8
# encoding: utf-8

import time

from selenium.webdriver.support.ui import WebDriverWait
import configparser
import os
from selenium import webdriver

root_dir = os.path.dirname(os.path.abspath(__file__))
cf = configparser.ConfigParser()

class getElement:
    def __init__(self, elementFile):
        self.elementPath = os.path.join(root_dir, "po_elements")
        self.elementIni = os.path.join(self.elementPath, elementFile)
        print(self.elementPath)

    def getElement(self, driver, section, option):
        try:
            f = configparser.ConfigParser()
            f.read(self.elementIni,encoding='utf-8')  # 读配置文件内容到内存中
            locators = f.get(section, option).split(':')
            # 获取定位方式
            locMethod = locators[0]
            # 获取定位表达式
            locExpression = locators[1]
            # 通过显示等待的方式获取页面的元素
            element = WebDriverWait(driver, 5).until(lambda x: x.find_element(locMethod, locExpression), message="定位超时")
        except Exception as e:
            raise e
        else:
            return element


def confParam(_filename=root_dir, flag="Test",_name='test'):
    cf.read(_filename, encoding="utf-8")

    # 获取配置文件中所有section
    secs = cf.sections()

    # 获取某个section名下所对应的键
    options = cf.options(flag)

    # 返回配置文件中name所对应的值
    return cf.get(flag, _name)


if __name__ == "__main__":
    url = confParam(_filename="./po_elements/pay.ini",flag='login', _name='username')
    print(url)


