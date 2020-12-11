# -*- coding:utf-8 -*-
from selenium import webdriver
import os
import unittest
import time
import requests
from selenium.webdriver.support.wait import WebDriverWait

import DMAutoTestReport.Login
import DMAutoTestReport.DeviceInterface as dI
import DMAutoTestReport.Login as lg
import DMAutoTestReport.deviceFunction as dF
import DMAutoTestReport.deviceFunction as function


class DeptPCIDUnitTest(unittest.TestCase):

    def setUp(self):
        self.path = 'ScreenShot'
        self.driver = webdriver.Chrome()
        # self.base_url = 'http://140.249.154.2:9005/'
        self.base_url = 'http://192.168.1.64:8090/'

    def test_DeptPCID(self):
        # 获取截图文件夹路径
        path = dF.DeviceFunction().currentDir(self.path)
        print('获取截图文件夹路径：' + path)
        # 开始浏览器操作
        self.driver.implicitly_wait(10)  # 隐式等待，当脚本执行到某个元素定位时，如果元素可定位那么继续执行，如果元素定位不到，那么它将以轮询的方式不断的判断元素是否被定位到
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        # 调用登录操作
        lg.Login().loginDevice(self.base_url, self.driver)
        # 营业厅PC查询
        self.driver.find_element_by_xpath('/html/body/div[1]/div/aside/div/nav/dl[2]/dt').click()                       # 点击设备软件
        self.driver.find_element_by_xpath('/html/body/div[1]/div/aside/div/nav/dl[2]/dd/a[11]').click()                 # 点击营业厅PC
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/div[15]/button').click()           # 点击查询按钮
        WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div'
                                            '[2]/div/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/button[2]'))  # 显性等待，等待详情按钮元素出现
        self.driver.get_screenshot_as_file(path + "\\DM36-营业厅PC查询.png")                                             # 截图
        # 单条件查询
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/div[10]/div/input').send_keys(
                                                        'c687b5cdb793d7b75b60e6772ca81cae')                             # PCID栏输入内容
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/div[15]/button').click()           # 点击查询按钮
        WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div'
                                            '[2]/div/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/button[2]'))  # 显性等待，等待详情按钮元素出现
        self.driver.get_screenshot_as_file(path + "\\DM37-营业厅PC单条件查询.png")                                       # 截图
        # 多条件查询
        self.driver.refresh()                                                                                           # 刷新页面
        WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div'
                                            '[2]/div/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/button[2]'))  # 显性等待，等待详情按钮元素出现
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/div[9]/div/input').send_keys('6')  # 核数栏输入内容
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/div[8]/div/input').send_keys('3')  # 主频栏输入内容
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/div[7]/div/input').send_keys('16') # 内存栏输入内容
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/div[15]/button').click()           # 点击查询按钮
        self.driver.implicitly_wait(10)
        time.sleep(3)
        self.driver.get_screenshot_as_file(path + "\\DM38-营业厅PC多条件查询.png")                                       # 截图
        # 查看PC详情
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[2]/div/div[1]/div[5]/div[2]/table/'
                                          'tbody/tr[1]/td[1]/div/div/button[2]').click()                                # 点击详情
        self.driver.implicitly_wait(10)
        time.sleep(3)
        self.driver.get_screenshot_as_file(path + "\\DM39-营业厅PC详情.png")                                             # 截图
        # # 刷新页面
        # self.driver.refresh()
        # self.driver.implicitly_wait(10)
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/aside/div/nav/dl[2]/dd/a[13]').click()                 # 点击设备登记审核
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div/div[1]/div[2]/table/tbody/tr[1]/td'
        #                                   '[2]/div/div/a')                                                              # 点击查看PID_VID
        # self.driver.get_screenshot_as_file(path + "\\DM40-查看PID_VID.png")                                             # 截图
        # self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[1]/main/div/div[1]/div[2]/table/tbody/tr'
        #                                   '[1]/td[4]/div/div/button')                                                   # 点击添加
        # self.driver.get_screenshot_as_file(path + "\\DM41-设备审核.png")                                                # 截图

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()