# encoding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Page(object):
    """
    基础类，用于页面对象类的继承
    """
    login_url = 'http://mail.163.com'

    def __init__(self, driver, base_url=login_url):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def target_page(self):
        return self.driver.current_url == self.base_url

    def _open(self, url):
        url = self.base_url
        self.driver.get(url)
        print(self.driver.current_url)

    def open(self):
        self._open(self.base_url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)


class LoginPage(Page):
    """
    126邮箱登陆页面，页面对象类
    """
    url = '/'
    """
    此处我们暂时称页面元素为对象，虽然本代码并非那么像对象，后续的框架中我们更高度的封装它便是个可操作的对象
    """
    username_loc = (By.NAME, "email")  # 页面控件对象：输入用户名的input控件
    password_loc = (By.NAME, "password")  # 页面控件对象：输入密码的input控件
    submit_loc = (By.ID, "dologin")  # 页面控件对象：登陆按钮的button控件

    """
    为每个页面元素对象封装其相对应的方法
    """
    def input_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)  # 输入用户名

    def input_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)  # 输入密码

    def click_submitbutton(self):
        self.find_element(*self.submit_loc).click()  # 点击登陆按钮


def user_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    sleep(5)
    driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='loginDiv']/iframe"))
    login_page.input_username(username)
    sleep(3)
    login_page.input_password(password)
    sleep(3)
    login_page.click_submitbutton()


def main():
    try:
        driver = webdriver.Chrome()
        username = 'xxxxxx'  # 登陆邮箱需要的真实账号
        password = 'xxxxxx'  # 登陆邮箱需要的真实密码
        user_login(driver, username, password)  # 调用前面封装好的user_login方法
        sleep(3)  #  等待3秒
        driver.switch_to.default_content()  # 切换出iframe
        assert_string = driver.find_element_by_xpath("/html/body/div[1]/nav/div[1]/ul/li[1]/span[2]").text
        print(assert_string)
        assert (assert_string == '收 信')  # 断言关键字
    finally:
        driver.quit()  # 关闭浏览器窗口


if __name__ == '__main__':
    main()