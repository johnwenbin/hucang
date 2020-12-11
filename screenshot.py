from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, os
from DMAutoTestReport import Login

def screenshot(driver, file_path = None):
    #用户没有传参数
    if file_path == None:
        project_path = os.path.dirname(os.getcwd())
        print (project_path)
        file_path = project_path + "/image/"
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        images_name = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        file_path = file_path + images_name + ".png"
        print(file_path)
    driver.save_screenshot(file_path)

try:
    Login.login()



