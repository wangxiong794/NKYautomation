'''上传附件'''
from selenium.webdriver.common.by import By
import time
import os
from con_nky import common_funcation
from selenium import webdriver
from con_nky.constructionProject import choice_apartment
from con_nky.common_funcation import submit, agree
import random
def regulation(driver):
    driver.find_element(By.XPATH,"//ul/li[9]").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//a[text()='规章制度']").click()
    driver.find_element(By.XPATH,"//span[text()='上传文档']/..").click()
    time.sleep(1)
    os.system(r"E:\workspace\au\regulation.exe")
    time.sleep(1)
def BA_upload(driver):
    driver.find_element(By.XPATH,"//ul/li[5]").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//a[text()='经费申请']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='+ 发起申请']/..").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//tbody/tr[2]/td[1]/span[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//input").click()
    js='var q=document.querySelector("#root > div > section > section > main").scrollBy(0,1000)'
    driver.execute_script(js)
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='下一步']/..").click()
    driver.find_element(By.XPATH,"//input[@placeholder='请输入申请金额']").send_keys('99.99')
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[text()='下一步']/..").click()
    up_apartment=choice_apartment(driver)
    up_creatuser=driver.find_element(By.XPATH,"//div[@id='modifiedUserId']/div/div/div[1]").text
    up_description=up_creatuser+'为'+up_apartment+'申请用于补充附件的校验'+time.strftime('%F-%H%M%S')    
    driver.find_element(By.XPATH,"//span[text()='上传附件']/..").click()
    up_type=('需求明细','会议纪要','批复文件','会议通知','其他附件')
    up_type1=random.sample(up_type,1)
    up_type2="".join(up_type1)
    driver.find_element(By.XPATH,"//li[text()='"+up_type2+"']").click()
    os.system(r"E:\workspace\au\autest.exe")
    time.sleep(1)
    driver.find_element(By.XPATH,"//textarea[@id='description']").click()
    driver.find_element(By.XPATH,"//textarea[@id='description']").send_keys(up_description)
    submit(driver)
    agree(driver)
if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.implicitly_wait(15)
    common_funcation.login_code(driver)
    BA_upload(driver)
    time.sleep(1)
    regulation(driver)
    driver.quit()