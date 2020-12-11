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


class SystemGroupUnitTest(unittest.TestCase):

    def setUp(self):
        self.path = 'ScreenShot'
        self.driver = webdriver.Chrome()
        # self.base_url = 'http://140.249.154.2:9005/'
        self.base_url = 'http://192.168.1.64:8090/'

    def test_systemGroup(self):
        # 获取截图文件夹路径
        path = dF.DeviceFunction().currentDir(self.path)
        print('获取截图文件夹路径：' + path)
        # 开始浏览器操作
        self.driver.implicitly_wait(10)  # 隐式等待，当脚本执行到某个元素定位时，如果元素可定位那么继续执行，如果元素定位不到，那么它将以轮询的方式不断的判断元素是否被定位到
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        # 调用登录操作
        lg.Login().loginDevice(self.base_url, self.driver)
        # 调用接口新增系统环境组
        systemCheckGroupId = dI.DeviceInterface().systemGroupAdd()
        self.driver.find_element_by_xpath('/html/body/div[1]/div/aside/div/nav/dl[2]/dt').click()                       # 点击设备软件
        self.driver.find_element_by_xpath('/html/body/div[1]/div/aside/div/nav/dl[2]/dd/a[4]').click()                  # 点击系统环境组
        self.driver.get_screenshot_as_file(path + "\\DM11-新增系统环境组.png")                                           # 截图
        self.driver.get_screenshot_as_file(path + "\\DM12-默认系统环境组.png")                                           # 截图
        # 调动接口修改环境组
        dI.DeviceInterface().systemGroupUpdate(systemCheckGroupId)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/div[2]/button[1]/span').click()    # 点击查询按钮
        self.driver.get_screenshot_as_file(path + "\\DM13-修改系统环境组.png")                                            # 截图
        # 查询部门
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[2]/div/div/div[2]/table/tbody/tr[1]'
                                          '/td[6]/div/div/button[3]').click()                                           # 点击发布到计算机
        WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath("/html/body/div[9]/div[2]/div/div/div[2]"
                                                                               "/main/div[1]/div[1]/div/div[1]/div[1]/input"))  # 显性等待，等待查询按钮元素出现
        self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div[2]/main/div[1]/div[1]'
                                          '/div/div[1]/div[1]/input').click()
        WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath("/html/body/div[9]/div[2]/div/div/div[2]"
                                                                               "/main/div[1]/div[1]/div/div[2]/div/span/ul/li[3]"))  # 显性等待，等待查询按钮元素出现
        self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div[2]/main/div[1]/div[1]'
                                          '/div/div[2]/div/span/ul/li[3]').click()
        self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div[2]/main/div[1]/div[5]/button[1]').click() # 点击查询按钮
        self.driver.get_screenshot_as_file(path + "\\DM15-部门查询.png")                                           # 截图

        # 查询pcid
        # self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div[2]/main/div[1]/div[1]/div/'
        #                                   'div[1]/i[1]').click()                                                        # 清空部门信息
        # self.driver.refresh()
        # time.sleep(1000)
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[2]/div/div/div[2]/table/tbody/tr[1]'
        #                                   '/td[6]/div/div/button[3]').click()                                           # 点击发布到计算机
        # time.sleep(1000)
        # self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/main/div[1]/div[2]/div/input').send_keys('c687b5cdb793d7b75b60e6772ca81cae')                        # pcid框输入内容
        # time.sleep(1000)
        # self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/main/div[1]/div[5]/button[1]').click() # 点击查询按钮
        # time.sleep(1000)
        # self.driver.get_screenshot_as_file(path + "\\DM16-pcid查询.png")                                           # 截图
        # 选择全部
        # self.driver.refresh()                                                                                           # 刷新页面
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[2]/div/div/div[2]/table/tbody/tr[1]'
        #                                   '/td[6]/div/div/button[3]').click()                                           # 点击发布到计算机
        # self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div[2]/main/div[1]/div[5]/button[2]/span').click()
        # self.driver.get_screenshot_as_file(path + "\\DM17-选择全部.png")
        # # 取消选择全部
        # self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div[2]/main/div[1]/div[5]/button[3]').click()
        # self.driver.get_screenshot_as_file(path + "\\DM18-取消选择全部.png")
        # 已绑定PC
        # self.driver.refresh()                                                                                           # 刷新页面
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[2]/div/div/div[2]/table/tbody/tr[1]'
        #                                   '/td[6]/div/div/button[3]').click()                                           # 点击发布到计算机
        # # WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath("/html/body/div[9]/div[2]/div/div/div[2]"
        # #                                                                        "/main/div[1]/div[6]/span"))             # 显性等待，等待查询按钮元素出现
        # self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div[2]/main/div[1]/div[6]/span').click()
        # self.driver.get_screenshot_as_file(path + "\\DM19-已绑定PC.png")
        self.driver.refresh()                                                                                           # 刷新页面
        # 调用接口新增系统环境检测
        checkItemId = dI.DeviceInterface().systemGroupCheckAdd(systemCheckGroupId)
        # 开始浏览器操作
        self.driver.find_element_by_xpath('/html/body/div[1]/div/aside/div/nav/dl[2]/dd/a[5]').click()                  # 点击系统环境检测
        self.driver.get_screenshot_as_file(path + "\\DM21-新增系统环境检测项.png")                                          # 截图
        # 调用接口修改系统环境检测
        dI.DeviceInterface().systemGroupCheckUpdate(checkItemId)
        # 开始浏览器操作
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]'
                                          '/button[1]/span').click()                                                    # 点击查询按钮
        self.driver.get_screenshot_as_file(path + "\\DM22-修改系统环境检测项.png")                                       # 截图
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[2]/div[2]/div/div[4]/div[2]/table/'
                                          'tbody/tr/td[1]/div/div/button[2]').click()                                   # 点击文件列表按钮
        self.driver.get_screenshot_as_file(path + "\\DM23-查看系统环境检测项文件详情.png")
        self.driver.refresh()                                                                                           # 刷新页面
        self.driver.implicitly_wait(10)
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[2]/div[2]/div/div[4]/div[2]/table/'
        #                                  'tbody/tr/td[1]/div/div/button[3]').click()                                   # 点击检测项删除按钮
        # self.driver.find_element_by_class_name('ivu-btn ivu-btn-primary ivu-btn-small').click()                       # 点击确定按钮————————————————————获取不到元素
        # 调用接口删除系统环境检测
        dI.DeviceInterface().systemGroupCheckDelete(checkItemId)
        self.driver.refresh()
        WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div"
                                                                               "[2]/div[1]/div[2]/button[1]"))          # 显性等待，等待查询按钮元素出现
        self.driver.get_screenshot_as_file(path + "\\DM24-删除系统环境检测项.png")                                       # 截图
        # 调用接口删除系统环境组
        dI.DeviceInterface().systemGroupDelete(systemCheckGroupId)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/aside/div/nav/dl[2]/dd/a[4]').click()                  # 点击系统环境组
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/div[2]/button[1]').click()         # 点击查询按钮
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[2]/div/div/div[2]/table/tbody/'
        #                                  'tr[1]/td[6]/div/div/button[4]').click()                                      # 点击环境组删除按钮
        # self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/footer/button[2]').click()           # 点击确定按钮

        self.driver.get_screenshot_as_file(path + "\\DM14-删除系统环境组.png")                                            # 截图

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()