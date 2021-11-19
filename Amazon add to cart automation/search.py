from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys

web=webdriver.Chrome("/home/milano/apps/chromedriver")
web.get("https://www.amazon.in")

#other way of finding element by ID

'''
- get search box xpath and ue search element by id
- click on it then inspect then see the highlighted code and look for id, copy it and add to our path
- then send input via send_keys
- wait
- variable find
and then pass x path link for the search button 

'''
searchbox= web.find_element_by_id("twotabsearchtextbox")
searchbox.send_keys("macbook pro")

#now wait for some tme
time.sleep(1)

find= web.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
find.click()

time.sleep(1)