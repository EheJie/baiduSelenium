# coding:utf-8
import sys
sys.path.append('..')
from selenium import webdriver
from libs.ShareModules import InsertLog

url_portal = 'https://www.baidu.com/'

def browser(b='gc'):
    try:
        if b == 'gc':
            # 处理SSL证书问题 : usb_device_handle_win.cc:1048 Failed to read descriptor from node connection:
            # 连到系统上的设备没有发挥作用。
            options = webdriver.ChromeOptions();
            options.add_argument('--ignore-certificate-errors');
            options.add_argument('--ignore-ssl-errors');
            # 忽略无用日志
            options.add_experimental_option("excludeSwitches",['enable-automation','enable-logging']);
            # 打开浏览器
            driver = webdriver.Chrome(chrome_options=options);
        elif b == 'ff':
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Edge()
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver
    except BaseException as msg:
        InsertLog('error',msg)

def open_url(driver,url=url_portal):
    driver.get(url)


    

