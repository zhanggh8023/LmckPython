# -*- coding: utf-8 -*-
# @Time    : 2021/12/2 19:42
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: webdriver.py
# @Software: PyCharm

from selenium import webdriver
import requests

driver = webdriver.Chrome(port=7000)
url = 'http://www.baidu.com'

server_url = 'http://127.0.0.1:7000/session/{}/url'.format(driver.session_id)
res = requests.post(server_url, json={'url': url}).json()
print(res)
