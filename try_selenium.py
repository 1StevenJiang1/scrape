# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver
import  time
# create webdriver object
driver = webdriver.Chrome()
# get google.co.in
driver.get("https://baidu.com")
while True:
    time.sleep(1)
