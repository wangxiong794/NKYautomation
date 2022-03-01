# coding=utf-8
# selenium网络爬虫
import logging
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pyquery import PyQuery as pq
from selenium.webdriver.common.keys import Keys
import time

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# dr = webdriver.Chrome(chrome_options=chrome_options)
root_dir = os.path.dirname(os.path.abspath(__file__))


class NetCrawler():
    def __init__(self):

        self.dr = webdriver.Chrome(os.path.join(root_dir, "chromedriver.exe"))
        self.dr.implicitly_wait(15)
        self.dr.set_window_size(1366, 900)
        self.log = Log()

    def only_test(self):

        self.dr.get("http://39.106.158.149/nky")
        self.dr.find_element(By.XPATH, "//input[@id='userName']").send_keys('chendongxue')
        self.dr.find_element(By.XPATH, "//input[@id='password']").send_keys('nky2018')
        self.dr.find_element(By.XPATH, "//input[@id='orgnizationId']").click()
        self.dr.find_element(By.XPATH, "//div[text()='200遂宁船山区集团校']").click()
        time.sleep(0.5)
        self.dr.find_element(By.XPATH, "//button[@data-test-id='LogInButton']").click()
        time.sleep(3)
        self.dr.find_element(By.XPATH, "//ul/li[4]").click()
        self.dr.find_element(By.XPATH, "//a[text()='事前申请']/..").click()
        self.dr.refresh()
        time.sleep(1)
        total = self.dr.find_element(By.XPATH, "//ul[@class='ant-pagination']/li[9]/a").text
        self.get_product()
        return total

    def next_page(self, page_number):
        input_n = self.dr.find_element(By.CSS_SELECTOR,
                                       "#ui-table-footer > ul > li.ant-pagination-options > div.ant-pagination-options-quick-jumper > input[type=text]")
        input_n.send_keys(page_number)
        input_n.send_keys(Keys.ENTER)
        self.get_product()

    def get_product(self):
        html = self.dr.page_source
        doc = pq(html)
        items = doc('.ant-table-tbody').items()
        for item in items:
            product = item.find('.ant-table-row-level-0').text()
            a = product.split()
            #         product = [a[1],a[6],a[],a[15],a[20],a[25],a[30],a[35],a[40],a[45]]
            product = [a[0], a[5], a[10], a[15], a[20], a[25], a[30], a[35], a[40], a[45]]
            # print(product)
            self.log.info(product)

    def main(self):
        total = int(self.only_test())
        for i in range(2, total + 1):
            self.next_page(i)
        self.dr.quit()


class Log:
    def __init__(self, log_path=os.path.join(root_dir, "logs")):

        # 文件的命名
        self.log_path = log_path
        self.logName = os.path.join(self.log_path, '%s.log' % time.strftime('%Y_%m_%d'))

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logName, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


if __name__ == '__main__':
    a = NetCrawler()
    a.main()
