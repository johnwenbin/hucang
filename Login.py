from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
import time


# 登录模块
class Login:

    def loginDevice(self, base_url, driver):
        driver.find_element_by_xpath("/html/body/div/div/div/p[1]/input").send_keys('admin')
        # driver.find_element_by_xpath("/html/body/div/div/div/p[2]/input").send_keys('Safery001com!')
        driver.find_element_by_xpath("/html/body/div/div/div/p[2]/input").send_keys('1111QQqq')
        driver.find_element_by_xpath("/html/body/div/div/div/button/span").click()


if __name__ == '__main__':
    Login().loginDevice()