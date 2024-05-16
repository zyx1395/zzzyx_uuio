from selenium import webdriver
from Common import NumOne
from test_data import data
from  selenium.webdriver.common.by import By
import sys
import os
curPath = os.path.abspath(os.path.dirname('D:\Myproject\python_project\test_resulet'))
rootPath = os.path.abspath(os.path.dirname(curPath) + os.path.sep + ".")
sys.path.append(rootPath)
driver=webdriver.Chrome()
driver.implicitly_wait(10)
url= data.url['url']
user= data.lonin_data['username']
pwd= data.lonin_data['password']
s_key= data.s_key['s_key']
resulet= NumOne.search_key(url=url, driver=driver, username=user, password=pwd,By=By,s_key=s_key)
if resulet=='381a2c6d5703518cea0330bbf14edde8':
    print('数据结果正确')
else:
    print('用例不通过')