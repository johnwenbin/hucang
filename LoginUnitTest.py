# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
import time


class LoginUnitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'http://58.215.200.58:19668/'

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        # 登录
        driver.find_element_by_xpath("/html/body/div/div/div/p[1]/input").send_keys('admin')
        driver.find_element_by_xpath("/html/body/div/div/div/p[2]/input").send_keys('123456')
        driver.find_element_by_xpath("/html/body/div/div/div/button/span").click()
        time.sleep(3)

        # 退出
        driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div/div[2]/button").click()
        t = driver.get_screenshot_as_file("E:\\deviceManage\\DMAutoTestReport\\ScreenShot\\test.png")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[2]/footer/button[2]/span").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
