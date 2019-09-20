#!/usr/bin/python3
from selenium import webdriver
import time
import atexit
import sys


sys.tracebacklimit = 0

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


driver = webdriver.Chrome('D://chromedriver.exe',
                          chrome_options=chrome_options)
driver.get('http://gstatic.com/generate_204')
print(driver.current_url)
try:

    user_name = driver.find_element_by_css_selector('#un')
    user_name.send_keys('.....')

    pswd = driver.find_element_by_css_selector('#pd')
    pswd.send_keys('......')
    pswd.submit()

    print('\nPress ctrl+c to exit\n')

    while True:
        time.sleep(800)
        driver.refresh()


except:
    print('\nexiting or logged in or not connectd\n')


finally:

    driver.get('http://172.16.1.11:1000/logout?030b0d0f05020b21')
    print('bye bye')
