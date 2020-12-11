# -*- coding:utf-8 -*-
from selenium import webdriver
import os
import unittest
import time
import requests
import DMAutoTestReport.Login
import DMAutoTestReport.DeviceInterface as dI
import DMAutoTestReport.Login as lg
import DMAutoTestReport.deviceFunction as dF
import DMAutoTestReport.deviceFunction as function


# 新增设备类型检测
class SupplierDeviceUnitTest(unittest.TestCase):

    def setUp(self):
        self.path = 'ScreenShot'
        self.driver = webdriver.Chrome()
        # self.base_url = 'http://140.249.154.2:9005/'
        self.base_url = 'http://192.168.1.64:8090/'

    def test_supplierDevice(self):
        # 获取截图文件夹路径
        path = dF.DeviceFunction().currentDir(self.path)
        print('获取截图文件夹路径：' + path)
        # 开始浏览器操作
        self.driver.implicitly_wait(10)  # 隐式等待，当脚本执行到某个元素定位时，如果元素可定位那么继续执行，如果元素定位不到，那么它将以轮询的方式不断的判断元素是否被定位到
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        # 调用登录操作
        lg.Login().loginDevice(self.base_url, self.driver)
        # 调用新增供应商接口
        supplierId = dI.DeviceInterface().supplierAdd()
        self.driver.find_element_by_xpath('/html/body/div[1]/div/aside/div/nav/dl[2]/dt').click()                       # 点击设备软件
        self.driver.find_element_by_xpath('/html/body/div[1]/div/aside/div/nav/dl[2]/dd/a[7]').click()                  # 点击供应商管理
        self.driver.get_screenshot_as_file(path + "\\DM25-新增供应商.png")
        # 调用修改供应商接口
        dI.DeviceInterface().supplierUpdate(supplierId)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/div[2]/button[1]').click()         # 点击查询按钮
        self.driver.implicitly_wait(10)
        self.driver.get_screenshot_as_file(path + "\\DM26-修改供应商.png")
        # 调用新增供应商设备接口
        supplierDevicesId = dI.DeviceInterface().deviceAdd(supplierId)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/aside/div/nav/dl[2]/dd/a[8]').click()                  # 点击供应商设备
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/nav/ul/li[2]').click()             # 点击新建的供应商设备
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[3]/div[1]/div[2]/button[1]').click()  # 点击查询按钮
        self.driver.implicitly_wait(10)
        self.driver.get_screenshot_as_file(path + "\\DM29-新增供应商设备.png")
        # 调用修改供应商设备接口
        dI.DeviceInterface().deviceUpdate(supplierDevicesId, supplierId)
        # 刷新
        self.driver.refresh()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/nav/ul/li[2]').click()             # 点击修改的供应商设备
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[3]/div[1]/div[2]/button[1]').click()  # 点击查询按钮
        self.driver.get_screenshot_as_file(path + "\\deviceUpdate.png")
        # 调用删除供应商设备接口
        dI.DeviceInterface().deviceDelete(supplierDevicesId)
        # 刷新
        self.driver.refresh()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/nav/ul/li[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[3]/div[1]/div[2]/button[1]').click()  # 点击查询按钮
        self.driver.implicitly_wait(10)
        self.driver.get_screenshot_as_file(path + "\\DM31-删除供应商设备.png")
        # 调用新增供应商设备检测接口
        checkItemId = dI.DeviceInterface().deviceCheckAdd(supplierId)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/aside/div/nav/dl[2]/dd/a[9]').click()                  # 点击供应商设备检测
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[3]/div[1]/div[2]/button[1]').click()  # 点击查询按钮
        self.driver.implicitly_wait(10)
        self.driver.get_screenshot_as_file(path + "\\DM30-新增供应商设备检测项.png")
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[3]/div[2]/div/div[4]/div[2]/table/'
                                          'tbody/tr[1]/td[1]/div/div/button[2]').click()                                # 点击文件列表
        self.driver.get_screenshot_as_file(path + "\\DM34-供应商设备检测项文件详情.png")
        # 调用修改供应商设备检测接口
        dI.DeviceInterface().deviceCheckUpdate(supplierId, checkItemId)
        # 刷新
        self.driver.refresh()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[3]/div[1]/div[2]/button[1]').click()  # 点击查询按钮
        self.driver.implicitly_wait(10)
        self.driver.get_screenshot_as_file(path + "\\DM33-修改供应商设备检测项.png")
        # 调用删除供应商设备检测接口
        dI.DeviceInterface().deviceCheckDelete(checkItemId)
        self.driver.refresh()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[3]/div[1]/div[2]/button[1]').click()  # 点击查询按钮
        self.driver.implicitly_wait(10)
        self.driver.get_screenshot_as_file(path + "\\DM35-删除供应商设备检测项.png")
        # 调用删除供应商接口
        dI.DeviceInterface().supplierDelete(supplierId)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/aside/div/nav/dl[2]/dd/a[7]').click()                  # 点击供应商设备
        self.driver.implicitly_wait(10)
        self.driver.get_screenshot_as_file(path + "\\DM27-删除供应商.png")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()