# coding=utf-8

"""Page方法的最父级方法"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser
from selenium.webdriver.support.ui import WebDriverWait


class page(object):
    def __init__(self, interface=1, ):
        if interface == 1:
            self.driver = webdriver.Chrome(r"E:\eclipse\webdriver\chromedriver.exe")
        else:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(15)
        self.driver.set_window_size(1366, 1000)

    def element(self, _filename="", section='test', option='test'):
        cf = configparser.ConfigParser()
        cf.read(_filename, encoding="utf-8")
        locators = cf.get(section, option).split(':')
        print(locators)
        locMethod = locators[0]
        locExpression = locators[1]
        element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element(locMethod, locExpression),
                                                      message="定位超时")
        # element = WebDriverWait(self.driver, 5).until(self.driver.find_element_by_xpath(locExpression),message="定位超时")
        return element

    @staticmethod
    def readConfig(_option):
        cf = configparser.ConfigParser()
        cf.read('../elements/config.ini', encoding="utf-8")
        cf.get(section='config',option=_option)

    def login(self, _filename='../elements/pay.ini', section='login'):
        self.driver.get(self.readConfig('url'))
        self.element(_filename, section, 'username').send_keys(self.readConfig('username'))
        self.element(_filename, section, 'password').send_keys(self.readConfig('password'))
        self.element(_filename, section, 'loginButton').click()


if __name__ == "__main__":
    c = page()
    c.login()
