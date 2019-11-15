import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.headless = True
driver = webdriver.Chrome(chrome_options = options)
driver.get('https://dojo.code.ninja/students/cn-nj-westfield')

time.sleep(5)

username = driver.find_element_by_id("signInName")
username.send_keys("############")

password = driver.find_element_by_id("password")
password.send_keys("############")

submitButton = driver.find_element_by_id("next")
submitButton.click()

time.sleep(5)

sideBar = driver.find_element_by_xpath("//*[@id='belt-selection']/div[2]/span")
sideBar.click()

time.sleep(1.5)
gradeSite = driver.find_element_by_xpath("//*[@id='mySidenav']/div/ul/li[1]/a")
gradeSite.click()

time.sleep(2)
driver.get('https://gdp.code.ninja/Grading/?searchTerm=&pageNum=2&pageSize=10000&includeGraded=true&slug=undefined&sort=')

content = driver.page_source

fileOut = open('index.html', 'w+');

fileOut.write(content)
fileOut.close()
