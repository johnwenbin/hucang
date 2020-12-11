# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import unittest
import time
import requests
from selenium.webdriver.support.wait import WebDriverWait
import DMAutoTestReport.Login
import DMAutoTestReport.DeviceInterface as dI
import DMAutoTestReport.Login as lg
import DMAutoTestReport.deviceFunction as dF


# 新增设备类型检测
class DeviceTypeUnitTest(unittest.TestCase):

    def setUp(self):
        self.path = 'ScreenShot'
        # self.base_url = 'http://140.249.154.2:9005/'
        self.base_url = 'http://192.168.1.64:8090/'
        # self.chrome_options = Options()
        # self.chrome_options.add_argument('--no-sandbox')
        # self.chrome_options.add_argument('--disable-dev-shm-usage')
        # self.chrome_options.add_argument('--headless')
        # self.chrome_options.add_argument('--disable-gpu')
        # # self.chrome_options.binary_location = r"C:\Users\h7814\AppData\Local\Google\Chrome\Application\chromedriver.exe"
        # self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        self.driver = webdriver.Chrome()

    def test_deviceType(self):
        path = dF.DeviceFunction().currentDir(self.path)      # 获取截图文件夹路径
        print('获取截图文件夹路径：' + path)
        # 开始浏览器操作
        self.driver.implicitly_wait(10)     # 隐式等待，当脚本执行到某个元素定位时，如果元素可定位那么继续执行，如果元素定位不到，那么它将以轮询的方式不断的判断元素是否被定位到
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        # 调用登录操作
        lg.Login().loginDevice(self.base_url, self.driver)
        WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div"
                                                                               "[2]/div[1]/div/div[1]"))                # 显性等待，等待元素出现，适合截图
        self.driver.get_screenshot_as_file(path + "\\DM01-登录成功.png")                                                 # 截图
        # 点击设备类型检测
        self.driver.find_element_by_xpath('/html/body/div[1]/div/aside/div/nav/dl[2]/dt').click()                       # 点击设备软件
        self.driver.find_element_by_xpath('/html/body/div[1]/div/aside/div/nav/dl[2]/dd/a[1]').click()                  # 点击设备类型
        self.driver.get_screenshot_as_file(path + "\\DM05-查看设备类型.png")                                             # 截图
        # 调用接口新增设备类型检测项
        checkItemId = dI.DeviceInterface().deviceTypeAdd()
        self.driver.find_element_by_xpath('/html/body/div[1]/div/aside/div/nav/dl[2]/dd/a[2]').click()                  # 点击设备类型检测
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/nav/ul/li[5]').click()             # 点击高拍仪
        self.driver.get_screenshot_as_file(path + "\\DM06-新增设备类型检测项.png")                                       # 截图
        # 文件详情截图
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[2]/div[2]/div/div[4]/div[2]/table/'
                                          'tbody/tr[1]/td[1]/div/div/button[2]').click()       # 点击文件详情
        WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath("/html/body/div[10]/div[2]/div/"
                                                                               "div/div[1]"))                           # 显性等待，等待文件详情元素出现
        self.driver.get_screenshot_as_file(path + "\\DM09-查看设备类型检测文件详情.png")                                  # 截图

        # self.driver.switch_to.default_content()
        # self.driver.find_elements_by_xpath('/html/body/div[8]/div[2]/div/div/div[3]/footer/button/span')              # 点击关闭
        # 调动接口修改设备类型检测项
        dI.DeviceInterface().deviceTypeCheckUpdate(checkItemId)
        self.driver.refresh()       # 刷新页面
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/nav/ul/li[5]').click()             # 点击高拍仪
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/button[1]/span').click()     # 点击查询按钮
        self.driver.get_screenshot_as_file(path + "\\DM08-修改设备类型检测项.png")                                       # 截图
        # 删除设备类型检测
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[2]/div[2]/div/div[4]/div[2]'
                                                            '/table/tbody/tr[1]/td[1]/div/div/button[3]').click()      # 点击删除按钮
        self.driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[2]/footer/button[2]').click()           # 点击确定
        self.driver.get_screenshot_as_file(path + "\\DM10-删除设备类型检测项.png")                                       # 截图

        # 退出登录
        # driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div/div[2]/button").click()
        # t = driver.get_screenshot_as_file("E:\\deviceManage\\DMAutoTestReport\\ScreenShot\\test.png")
        # time.sleep(2)
        # driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[2]/footer/button[2]/span").click()
        # time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
