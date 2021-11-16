# coding=utf-8
import threading

from selenium import webdriver
from selenium.webdriver.common.by import By

from get_root_path import root_dir
import os
import time


# chrome_options = webdriver.FirefoxOptions()

def test():
    for a in range(0, 100):
        print("第" + str(a) + "轮")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(os.path.join(root_dir,"chromedriver.exe"),chrome_options=chrome_options)
        # driver = webdriver.Chrome(os.path.join(root_dir, "chromedriver.exe"))
        driver.implicitly_wait(60)
        driver.get("http://58.118.2.63/bureau")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='userName']").send_keys('cwk')
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys('Abcd@1234')
        driver.find_element(By.XPATH, "//button[@data-test-id='LogInButton']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[text()='我的国拨']").click()
        time.sleep(3)
        try:
            for i in range(0, 100):
                # time.sleep(15)
                driver.find_element(By.XPATH,
                                    '//*[@id="globalLayoutContent"]/div/div/div/div[2]/div[1]/div[1]/div/div[3]/div[4]/div[2]/section/div/div/div/div/div/div/div/div/table/tbody/tr[1]').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//button[text()="同意"]').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys("同意")
                time.sleep(0.1)
                driver.find_element(By.XPATH, '//span[text()="确 定"]/..').click()
                time.sleep(0.5)
                print(i)
        except:
            driver.quit()
        driver.quit()


def czAgree(a=1):
    """待财政审批"""

    print("第" + str(a) + "轮")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(os.path.join(root_dir,"chromedriver.exe"),chrome_options=chrome_options)
    # driver = webdriver.Chrome(os.path.join(root_dir, "chromedriver.exe"))
    driver.implicitly_wait(60)
    driver.set_window_size(1688,800)
    driver.get("http://58.118.2.63/bureau")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='userName']").send_keys('cz')
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys('nky2018')
    driver.find_element(By.XPATH, "//button[@data-test-id='LogInButton']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[text()='我的预算']").click()
    time.sleep(3)
    try:
        for i in range(0, 100):
            # time.sleep(15)
            time.sleep(0.5)
            driver.find_element(By.XPATH,
                                '//*[@id="globalLayoutContent"]/div/div/div/div[2]/div[1]/div[1]/div/div[3]/div['
                                '4]/div[2]/section/div/div/div/div/div/div/div/table/tbody/tr['+str(a)+']').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//button[text()="同意"]').click()
            time.sleep(0.1)
            driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys("同意")
            time.sleep(0.1)
            driver.find_element(By.XPATH, '//span[text()="确 定"]/..').click()
            time.sleep(0.5)
            # driver.find_element(By.XPATH,'//span[text()="工作台"/..').click()
            driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/nav/div[1]/ul/li[1]').click()
            print(i)
    except:
        driver.quit()


def main(flag,cz=0):
    if flag =='cwk':
        try:
            test()
        except:
            test()
        finally:
            test()
    elif flag == 'cz':
        try:
            czAgree(cz+1)
        except:
            czAgree(cz+2)
        finally:
            czAgree(cz+3)


if __name__ == '__main__':
    for i in range(0,5):
        main('cz',i)