"""测试bureau项目本地客户端的压力测试"""


import threading
import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class workSpace(unittest.TestCase):

    def setUp(self) -> None:
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        firefox_options.add_argument('--disable-gpu')
        self.driver = webdriver.Firefox(options=firefox_options, executable_path='geckodriver.exe')
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.set_window_size(1920, 1080)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.img = """           // 首屏图片加载完成
                                    let mytiming = window.performance.timing;
                                    return window.lastImgLoadTime - mytiming.navigationStart ;
                        """
        self.intfaces = """   // https://blog.csdn.net/weixin_42284354/article/details/80416157
                // 接口完成加载完成
                                    let mytiming = window.performance.timing;
                                    return Report.SPEED.LASTCGI - mytiming.navigationStart ;
                        """
        self.DNS = """          // DNS查询耗时
                            let mytiming = window.performance.timing;
                            return mytiming.domainLookupEnd - mytiming.domainLookupStart ;
                """
        self.TCP = """          // TCP链接耗时
                            let mytiming = window.performance.timing;
                            return mytiming.connectEnd - mytiming.connectStart ;
                """
        self.request = """          // request请求耗时
                            let mytiming = window.performance.timing;
                            return mytiming.responseEnd  - mytiming.responseStart ;
                """
        self.dom = """          //  解析dom树耗时
                            let mytiming = window.performance.timing;
                            return mytiming.domComplete - mytiming.domInteractive ;
                """
        self.Ari = """          // 白屏时间
                            let mytiming = window.performance.timing;
                            return mytiming.responseStart - mytiming.navigationStart ;
                """

        self.domready = """          // domready时间
                            let mytiming = window.performance.timing;
                            return mytiming.domContentLoadedEventEnd   - mytiming.fetchStart ;
                """
        self.loadEventTime = """
                           let mytiming = window.performance.timing;
                           return mytiming.loadEventEnd - mytiming.navigationStart ;
                              """
        self.gather_data_dict = [
            {'UrlName': '绩效通',
             'Url': 'http://dev3.neikongyi.com/bureau',
             'number': 5}
        ]

    def test_untitled_test_case(self):
        # 返回结果
        result = []
        # 读取压测数数据，返回加载结果！
        for data in self.gather_data_dict:
            result_temp = {
                "UrlName": data["UrlName"],
                "Url": data["Url"],
                "number": data["number"],
                "NoCache": self.__get_page_load_time_NoCache(data['Url'], data['number']),
                # "Cache": self.__get_page_load_time_Cache(data['Url'], data['number'])
            }
            result.append(result_temp)
        with open('bureau.txt', 'a') as f:
            f.write(str(result)+'\n')
        print(result)

    def __get_page_load_time_NoCache(self, Url, number=1):
        """
        网页无缓存的情况下进行加载速度测试
        :param Url: 加载的网址
        :param number: 加载次数
        :return:
        """
        driver = self.driver
        page = []
        domready = []
        res_page = {}
        res_domready = {}
        for i in range(number):
            # 调用浏览器打开一个新窗口
            driver.execute_script("window.open('','_blank');")
            # 窗口定位到新打开的窗口
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(Url)
            self._login()
            time.sleep(0.5)
            page.append(int(driver.execute_script(self.loadEventTime)))
            domready.append(int(driver.execute_script(self.domready)))
            # image.append(int(driver.execute_script(self.img)))
            # a = driver.execute_script(self.img)
            # print(type(a),a)
            time.sleep(0.5)
            # 关闭窗口
            driver.execute_script("window.close();")
            # 窗口定位返回旧窗口
            driver.switch_to.window(driver.window_handles[-1])

        res_page['max'] = max(page)
        res_page['min'] = min(page)
        res_page['avg'] = sum(page) / len(page)
        # print(res_page)
        res_domready['max'] = max(domready)
        res_domready['min'] = min(domready)
        res_domready['avg'] = sum(domready) / len(domready)

        msg = {"页面加载时间": res_page,
               "DOM加载时间": res_domready,
               }
        # with open('bureau.txt', 'a') as f:
        #     f.write(str(msg)+'\n')
        return msg

    def __get_page_load_time_Cache(self, Url, number=4):
        """
        网页有缓存的情况下进行加载速度测试
        :param Url: 加载的网址
        :param number: 加载次数
        :return:
        """
        driver = self.driver
        page = []
        domready = []
        image = []
        res_page = {}
        res_domready = {}
        res_image = {}
        driver.get(Url)
        for i in range(number):
            driver.get(Url)
            self._login()
            page.append(int(driver.execute_script(self.loadEventTime)))
            domready.append(int(driver.execute_script(self.domready)))
            image.append(driver.execute_script(self.img))
            print(image)
            print(type(image))
            time.sleep(0.5)
            # 关闭窗口
            driver.execute_script("window.close();")
            # 窗口定位返回旧窗口
            driver.switch_to.window(driver.window_handles[-1])

        res_page['max'] = max(page)
        res_page['min'] = min(page)
        res_page['avg'] = sum(page) / len(page)

        res_domready['max'] = max(domready)
        res_domready['min'] = min(domready)
        res_domready['avg'] = sum(domready) / len(domready)

        res_image['Max'] = max(image)
        res_domready['min'] = min(image)
        res_domready['avg'] = sum(image) / len(image)

        return {"页面加载时间": res_page,
                "DOM加载时间": res_domready,
                "图片加载时间": res_image}

    def _login(self):
        driver = self.driver
        userName = driver.find_element_by_id("userName")
        action = ActionChains(driver)
        action.click(userName).send_keys("admin1").send_keys(Keys.TAB).send_keys("nky2018").send_keys(
            Keys.ENTER).perform()

    def tearDown(self):
        pass


class myThread1(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        # print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        # threadLock.acquire()
        # # 释放锁，开启下一个线程
        # threadLock.release()
        a = workSpace()
        a.setUp()
        a.test_untitled_test_case()
        a.tearDown()


def run_all():
    threadLock = threading.Lock()
    threads = []
    for i in range(1, 11):
        t1 = myThread1(i, "thread" + str(i), str(i))
        t1.start()
        threads.append(t1)
    # 等待所有线程完成
    for t in threads:
        t.join()
    print("退出主线程")
    with open('bureau.txt', 'a') as f:
        f.write('————————————————————分割线———————————————————\n')


if __name__ == "__main__":
    # unittest.main()
    run_all()