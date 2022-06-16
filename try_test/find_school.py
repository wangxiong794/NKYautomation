# coding=utf-8
import os
import time

from selenium.webdriver.firefox.options import Options

from service.logger import Log
import xlrd
from selenium import webdriver


def read(row):
    book = xlrd.open_workbook(r"F:\workspace\公司项目\双高招投标收集\197所国双高名单.xls")
    sheet = book.sheet_by_index(0)
    # print(sheet.cell_value(1, 1))
    return [sheet.cell_value(row, 1), sheet.cell_value(row, 2)]


def sg(keyword="中期自评报告"):
    log = Log()
    for i in range(1, 198):
        cname = read(i)
        name = cname[0]
        url = str(cname[1])
        log.info("正在查找："+str(name))
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='../chromedriver.exe')
        firefox_options = Options()
        firefox_options.add_argument('--headless')
        firefox_options.add_argument('--disable-gpu')
        driver = webdriver.Firefox(options=firefox_options, executable_path='../geckodriver.exe')
        # driver = webdriver.Chrome(executable_path='../chromedriver.exe')
        try:
            driver.get(url)
            time.sleep(1)
            a = driver.execute_script("return document.documentElement.outerHTML")
        # print(a)
            if keyword in str(a):
                # print(str(name)+":"+str(url))
                log.info(str(name)+"单位存在报告：《"+str(url)+"》")
                with open(r'log-last.txt', 'a+', encoding='utf-8') as f:
                    f.write(str(time.strftime('%Y%m%d-%H:%M:%S: '))+str(name)+"单位存在报告：《"+str(url)+"》\n")
                    f.close()
                driver.quit()
            else:
                log.warning(str(name) + "单位不存在")
                driver.quit()
        except:
            driver.quit()
            log.warning(str(name)+"单位打开失败，域名是"+str(url))
        os.system('taskkill /F /iM firefox.exe')


if __name__ == "__main__":
    # a=read(1)
    # print(a[0])
    a = input("请输入关键字(默认中期自评报告)：")
    if a is None:
        sg()
    else:
        sg(str(a))
