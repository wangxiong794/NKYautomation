"""hrmanage test case basic event"""
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from service.bpm_service.common_funcation import submit


def main(driver, nky_url, username, password):
    driver.get(nky_url)
    driver.find_element(By.ID, "userName").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element_by_xpath("//button").click()
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, "//img[@id='pm-closeGuideViewButton']").click()
    except:
        pass


def add_message(driver, mname):
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[text()='+新增']/..").click()
    time.sleep(0.5)
    driver.find_element_by_id('name').send_keys(mname)
    driver.find_element_by_id('remark').send_keys('automation_remark')
    driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-primary"]').click()


def create_basic_data(driver):
    driver.find_element_by_xpath('//span[text()="基础数据"]/..').click()
    driver.find_element_by_xpath("//a[text()='人事管理设置']").click()
    # add person level
    driver.find_element_by_xpath("//li[text()='人员类别设置']").click()
    add_message(driver, 'person_level_' + str(time.asctime()))


def create_personnel(driver):
    driver.find_element(By.XPATH, '//span[text()="人事管理"]/..').click()
    driver.find_element(By.XPATH, '//a[text()="人员管理"]').click()
    time.sleep(0.5)
    # add person
    driver.find_element(By.XPATH, "//span[text()='新增人员']/..").click()
    name_parameter = str(time.time())
    name_parameter = name_parameter[11:]
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys('automatic' + name_parameter)  # personnel name
    driver.find_element(By.XPATH, "//div[@id='nationTypeId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='nationTypeId']").send_keys(Keys.ENTER)  # choose nation type
    driver.find_element(By.XPATH, "//div[@id='documentTypeId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='documentTypeId']").send_keys(Keys.ENTER)  # choose document type
    card_number_paramter = str(time.time)
    driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys(card_number_paramter)  # input card number
    driver.find_element(By.XPATH, "//div[@id='departmentId']/div/div").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//input[@id='departmentId']").send_keys(Keys.ENTER)  # choose department


def create_personnel_bill(driver):
    time.sleep(1)
    driver.find_element(By.XPATH, '//span[text()="人事管理"]/..').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//a[text()="人员管理"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//div[text()='档案变更']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary']").click()  # add personnel bill button
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[@id='executeMonth']/div/input").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//a[text()='九月']").click()
    description_parameter = str(time.asctime())
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys('automatic' + description_parameter)
    driver.find_element(By.XPATH, "//textarea[@id='remark']").send_keys('automatic' + description_parameter)
    # click person name
    driver.find_element(By.XPATH,
                        '//*[@id="root"]/div/section/section/main/div/div/div[3]/div[2]/div/section[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[2]/div').click()
    time.sleep(1)
    # choose the first person
    driver.find_element(By.XPATH,
                        "//div[@class='ant-table ant-table-default ant-table-scroll-position-left']/div/div[2]/div/div/table/tbody/tr[1]/td/span/label/span/input").click()
    driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
    # click change person budget
    time.sleep(1)
    driver.find_element(By.XPATH,
                        '//*[@id="root"]/div/section/section/main/div/div/div[3]/div[2]/div/section[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[5]/div/div/div').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//li[text()="职务类别"]').click()
    time.sleep(0.5)
    # choose the change after budget
    driver.find_element(By.XPATH,
                        '//*[@id="root"]/div/section/section/main/div/div/div[3]/div[2]/div/section[2]/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[7]/div/div').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//li[text()="中级职称"]').click()
    submit(driver)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()  # handle the window to biggest
    main(driver, 'http://47.93.245.21/nky', 'chendongxue', 'nky2018')
    create_personnel_bill(driver)
